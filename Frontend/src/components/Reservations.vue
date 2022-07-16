<template>
    <div >
      <b-nav tabs justified>
        <b-nav-item :to = "{ name: 'main' }">메인</b-nav-item>
        <b-nav-item :to = "{ name: 'reservations' }">예약현황</b-nav-item>
        <b-nav-item :to = "{ name: 'buildingmng' }">건물관리</b-nav-item>
        <b-nav-item :to = "{ name: 'facilitymng' }">시설물관리</b-nav-item>    
        <b-nav-item :to = "{ name: 'login'}" @click="logoutSubmit">logout</b-nav-item>
      </b-nav>
        <div class="row">
            <h2>{{ $store.state.userStore.uid }}님의 예약현황</h2>
            <div class="col">
                    <v-data-table
                    :headers="headers"
                    :items="reservations"
                    :items-per-page="10"
                    item-key="rid"
                    class="elevation-1"
                    :footer-props="{
                      showFirstLastPage: true,
                      firstIcon: 'mdi-arrow-collapse-left',
                      lastIcon: 'mdi-arrow-collapse-right',
                      prevIcon: 'mdi-minus',
                      nextIcon: 'mdi-plus'
                    }"
                    @click="buildadd = true"
                  ></v-data-table>
            </div>
                <form @submit.prevent="senddelete">
                <div class="row" style="width:20%">
                  <span class="title_content">예약번호</span>
                  <input class="txtfield" type="text" name="id" v-model="id">
                  <b-button type="submit" v-on:click="oneDelete(id)">취소하기</b-button>
                </div>
                </form>
        </div>
    </div>
</template>


<script>
  export default {
    name: "Resvations",
    data() {
      return {
        headers: [{
          text: '예약번호',
          align: 'start',
          value: 'rid'
        },
        { text: '시설물 이름', value: 'fid' },
        { text: '상세내용', value: 'rcontents' },
        { text: '시작시간', value: 'rstarttime' },
        { text: '마감시간', value: 'rendtime' },
        { text: '참석자', value: 'attendees' },
        ],
        reservations: [],
        posts:{
          ruser:null,
          fid:null,
          rstarttime:null,
          rendtime:null,
          rcontents:null,
          attendees:null
        },
        id: ''
      }
    },
    methods:
    {
      getData(){
        this.axios.get('http://192.168.16.28:30800/reservation/' + `${localStorage.getItem('uid')}`).then((result)=>{
          this.reservations = result.data
        })
      },
      logoutSubmit() {
        this.$store.commit('logout')
        localStorage.clear()
        alert("로그아웃 했습니다.")
      },
      oneDelete(id){
        this.axios.delete('http://192.168.16.28:30800/reservation/' + id , {headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`,}} ).then((result)=>{
          this.buildings = result.data
          this.getData()
          alert("취소되었습니다.")
        })
      },
    },
    mounted: function() {
    this.getData()
    }
  }
</script>

<style scoped>
body{
  margin :0
}
div{
    box-sizing: border-box;
}
.right.black-bg{
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}
.white-bg{
  width: 100%; background: white;
  border-radius: 8px;
  padding: 20px;
}
.left {
    width: 50%;
    float: left;
    box-sizing: border-box;
    
    /* background: #ff0; */
}
.right {
    width: 50%;
    float: right;
    box-sizing: border-box;
}
h1{
    font-size: 50px;
    text-align: center;
    padding: 10px 0;
    margin-top: 20px;
}
row_wrap{
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.row {
    display: flex;
    padding: 10px 0;
}
div.row{
    display: flex;
    text-align: center;
}
.title_content{
    display: flex;
    align-items: center;
    width: 100px;
    height: 50px;
    font-weight: bold; 
}
.txtfield{
      flex: 1;
    align-items: center;
    background-color: white;
    width: 300px;
    height: 50px;
    font-size: 13px;
    padding: 10px;
    border-style: solid;
    box-sizing: border-box;
}
.txtfield_img{
      flex: 2;
    background-color: white;
    align-items: center;
    height: 50px;
    font-size: 13px;
    padding: 10px;
    border-style: solid;
    box-sizing: border-box;
    position: static;
    left: 30px;
}
.menu{
  text-align: center
}
.button_style{
    width: 300px;
    height: 50px;
    padding: 10px;
    float: right;
    margin: 1em;
}
.button_cls{
    width: 100px;
    height: 50px;
    padding: 10px;
    float: right;
    margin: 1em;  
}
.b_buttonadd{
    padding: 10px;
    margin: 1em;
}
.b_buttondel{
    padding: 10px;
    margin: 1em;
}
</style>