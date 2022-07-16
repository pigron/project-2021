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
        <b-card-body>
          <div class="left">
            <b-button class="f_buttonadd" @click="facilityadd = true">시설물 등록하기</b-button>
            <b-button class="f_buttonadd" @click="facilitydel = true">시설물 삭제하기</b-button>
            <v-data-table
              :headers="headers"
              :items="facilitys"
              :items-per-page="10"
              item-key="fid"
              class="elevation-1"
              :footer-props="{
                showFirstLastPage: true,
                firstIcon: 'mdi-arrow-collapse-left',
                lastIcon: 'mdi-arrow-collapse-right',
                prevIcon: 'mdi-minus',
                nextIcon: 'mdi-plus'
              }"
            ></v-data-table>
          </div>


          <div class="right">
            <div class="black-bg" v-if="facilityadd == true">
              <div class="white-bg">
              <form>
              <h1>시설물 등록</h1>
                <div class="row">
                  <span class="title_content">시설물 ID</span>
                  <input class="txtfield" type="text" name="fid" v-model="posts.fid">
                </div>
                <div class="row">
                  <span class="title_content">시설물이름</span>
                  <input class="txtfield" type="text" name="fname" v-model="posts.fname">
                </div>
                <div class="row">
                  <span class="title_content">상세내용</span>
                  <input class="txtfield" type="text" name="fcontents" v-model="posts.fcontents">
                </div>
                <div class="row">
                  <span class="title_content">시설물사진</span>
                  <v-file-input label="File input" @change="selectFile"></v-file-input>
                <div class="row">
                  <span class="title_content">건물 선택</span>
                    <b-form-select 
                      :options="buildings" 
                      v-model="posts.bid"
                      text-field="bname"
                      class="txtfield"
                      value-field="bid"
                      disabled-field="notEnabled"
                    ></b-form-select>
                </div>
                <div class="row">
                  <span class="title_content">시설물타입</span>
                  <b-form-select 
                      :options="type" 
                      v-model="posts.ftypeid"
                      text-field="name"
                      class="txtfield"
                      value-field="typeid"
                      disabled-field="notEnabled"
                    ></b-form-select>
                </div>
                </div>
                  <b-button class="button_cls" @click="facilityadd = false" >닫기</b-button>
                  <b-button class="button_cls" @click="submit">등록하기</b-button>
              </form>
              </div>
            </div>
          </div>


          <div class="right">
            <div class="black-bg" v-if="facilitydel == true">
              <div class="white-bg">
              <form @submit.prevent="postData" method="post">
              <br><br><br>
                <h1>시설물 삭제</h1>
                <form @submit.prevent="senddelete">
                <div class="row">
                  <span class="title_content">시설물 ID</span>
                  <input class="txtfield" type="text" name="id" v-model="id">
                </div>
                  <b-button class="button_cls" @click="facilitydel = false" >닫기</b-button>
                  <b-button class="button_cls" type="submit" v-on:click="deleteBuilding(id)">삭제하기</b-button>
                </form>
              </form>
              </div>
            </div>
          </div>
        </b-card-body>
        </b-card>
    </div>
</template>

<script>
const API_URL = "http://192.168.16.28:30800/"

  export default {
    name: "Facility",
    data() {
      return {
        facilityadd: false,
        facilitydel: false,
        facilitys: [],       
        buildings: [], 
        headers: [{
          text: 'ID',
          align: 'start',
          value: 'fid'
        },
        { text: '시설물', value: 'fname' },
        ],
        type: [
          { typeid: '01', name: '휴게실' },
          { typeid: '02', name: '강의실' },
          { typeid: '03', name: '회의실' }
        ],
        posts:{
          fid:null,
          fname:null,
          fcontents:null,
          fimage:null,
          bid:null,
          ftypeid:null
        },
        id: null
      }
    },

    methods: {
      getBuilding(){
        this.axios.get(`${API_URL}building/`).then((result)=>{
          this.buildings = result.data
        })
      },
      getData(){
        this.axios.get(`${API_URL}facility/`).then((result)=>{
          this.facilitys = result.data
        })
      },
      deleteBuilding(id){
          this.axios.delete(`${API_URL}facility/` + id , {headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`,}})
        .then(()=>{
          this.getData();
          alert("삭제되었습니다.")
        })
        .catch((err)=>{
          alert(err.response.data.detail)
        })
      },
      selectFile(file) {
        this.posts.fimage = file;
      },
      postData(e){
          this.axios.post(`${API_URL}facility/`, this.posts , {headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`,}})
            .then((result)=>{
              console.warn(result);
              alert("생성되었습니다.")
            })
            .catch((err) => {
              alert(err.response.data.detail[0].msg)
            })
        e.preventDefault();
      },
      async submit() {
        const formData = new FormData();
        formData.append('fid', this.posts.fid)
        formData.append('fname', this.posts.fname)
        formData.append('fcontents', this.posts.fcontents)
        formData.append('fimage', this.posts.fimage)
        formData.append('ftypeid', this.posts.ftypeid)
        formData.append('bid', this.posts.bid)

        try {
          const { data } = await this.axios.post(`${API_URL}facility/`, formData, {
            headers: {
              'Content-Type' : 'multipart/form-data',
              'Authorization' : `Bearer ${localStorage.getItem('token')}`,
            }
          });
          console.log(data);
          alert("생성되었습니다.")
        } catch(err) {
          console.log(err);
        }
      },
    },
    mounted: function() {
      this.getData()
      this.getBuilding()
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
.f_buttonadd{
    padding: 10px;
    margin: 1em;
}
.f_buttondel{
    padding: 10px;
    margin: 1em;
}
</style>