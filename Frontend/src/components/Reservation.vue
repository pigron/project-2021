<template>
   <div>
        <b-nav tabs justified>
            <b-nav-item :to = "{ name: 'main' }">메인</b-nav-item>
            <b-nav-item :to = "{ name: 'reservations' }">예약현황</b-nav-item>
            <b-nav-item :to = "{ name: 'buildingmng' }">건물관리</b-nav-item>
            <b-nav-item :to = "{ name: 'facilitymng' }">시설물관리</b-nav-item>    
            <b-nav-item :to = "{ name: 'login'}" @click="logoutSubmit">logout</b-nav-item>
        </b-nav>
        <b-card>
            <div class="left">
                <b-img thumbnail
                :src='$route.query.image'
                alt="Image 1"
                style="width:100%">
                </b-img>
            </div>
            <div class="right">
                <div style="margin: 1em">
                    <b-card-title>
                        <h1><b>건물 이름 : {{ $route.query.name }}</b></h1>
                        <h6>해당 건물 과 : {{ $route.query.contents }}</h6>
                    </b-card-title>
                </div>
                <div style="margin: 2em"> 
                    <div class="left" style="padding: 0 0 0 7em ">건물명 :
                        <select v-model="selected_fields" style="border: 1px solid black;">
                        <option v-for="classna in classname" :key="classna" v-bind:value=classna.ftypeid >{{ classna.ftypename }}</option></select>
                    </div>
                    <div  >시설물 :
                        <select v-model="posts.fid" style="border: 1px solid black;">
                        <option v-for="fac in faSelected" v-bind:key="fac" v-bind:value=fac.fid>
                                {{ fac.fname }}  
                        </option>
                        </select>
                    </div>
                </div>
            </div>

                <div>
                    <form @submit.prevent="postData" method="post">
                        <div class="left" style="padding: 1em 0 0 1em">
                            학번 : {{ $store.state.userStore.uid }} <br>
                        </div>
                        <div class="left" style="padding: 1em">
                            대여 사유 :
                            <b-form-textarea
                                id="textarea-no-resize"
                                
                                rows="0"
                                class="txtfield"
                                type="text" 
                                name="fid" v-model="posts.rcontents"
                                no-resize
                            ></b-form-textarea>  <br>  

                            본인포함 참석자 :
                            <b-form-textarea
                                id="textarea-state"
                                class="txtfield"
                                type="text" 
                                name="attendees" v-model="posts.attendees"
                                
                                rows="1">
                            </b-form-textarea>  <br>  

                            <div class= "time-label">
                                <label class="time-text" for="rstarttime">시작 시간: </label>
                                    <input class="time-box" type="datetime-local" id="rstarttime"
                                        name="rstarttime" value="2021-11-09T05:00"
                                        min="2021-11-09T00:00" max="2021-11-31T11:30"
                                        v-model="posts.rstarttime" style="border: 1px solid black;">
                                
                                <label class="time-text" for="rendtime">끝난 시간: </label>
                                    <input class="time-box" type="datetime-local" id="rendtime"
                                        name="rendtime" value="2021-11-09T05:00"
                                        min="2021-11-09T00:30" max="2022-12-01T00:00"
                                        v-model="posts.rendtime" style="border: 1px solid black;">
                            </div>
                            <b-card-footer>
                                <div class="button">
                                    <b-button type="submit">예약하기</b-button>
                                </div>
                            </b-card-footer>
                        </div>
                    </form>
                </div>
        </b-card>
    </div>
</template>

<script>
const API_URL = "http://192.168.16.28:30800/"

  export default {
    name: "Reservation",
    data() {
      return {
        classname: [],
        facility: [],
        selected_fields: '',
        text: '',
        reservation: [],
        posts:{
          ruser: this.$store.state.userStore.uid ,
          fid:null,
          rstarttime:null,
          rendtime:null,
          rcontents:null,
          attendees:null,
        }
      }
    },
    computed: {
        faSelected() {
            return this.facility.filter(data => data.ftypeid === this.selected_fields)
        }
    },
    methods:
    {
      getFtype(){
        this.axios.get('http://192.168.16.28:30800/ftype/').then((result)=>{
          this.classname = result.data
        })
      },
      postData(e){
          this.axios.post('http://192.168.16.28:30800/reservation/', this.posts)
              .then((result)=>{
                  console.warn(result);
                  alert("예약되었습니다.")
                  this.$router.push("/reservations");
          })
        e.preventDefault();
      },
      getFacility(){
        this.axios.get(`${API_URL}facility/`).then((result)=>{
          this.facility = result.data
        })
      },
    },
    mounted: function() {
        this.getFtype(),
        this.getFacility()
    }
  }
</script>

<style>
.b-card-title{
    margin: 0 0 0 1em;
    border: 1px solid;
    border-color: black;
    border-radius: 5px;
    padding: .3em;
}
select {
    width: 25%; /* 원하는 너비설정 */
    padding: .8em .5em; /* 여백으로 높이 설정 */
    border: 3px solid;
    border-color: black;
    border-radius: 3px; /* iOS 둥근모서리 제거 */
    -webkit-appearance: none; /* 네이티브 외형 감추기 */
    -moz-appearance: none;
    appearance: none;
    text-align: center;
}
option{
    border-radius: 2px;
}
.right.div.left{
    border: 1px solid;
    border-color: black;
    border-radius: 5px;
}
h1{
    text-align: center;    
}
h6{
    text-align: center;    
}
.button
{
    text-align: right;
    margin: 0 0 0 5em;
}
.time-label{
    text-align: left;
}
.time-text{
    text-align: center;
    width: 10%;
    margin: 0 1em 0 2em; 
}
.time-box{
    width: 33%;

}
.left {
    width: 50%;
    float: left;
    box-sizing: border-box;
}
.right {
    width: 50%;
    float: right;
    box-sizing: border-box;
}
li {
    list-style-type: none;
}

</style>