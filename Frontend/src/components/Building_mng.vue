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
            <b-button class="b_buttonadd" @click="buildadd = true, builddel = false">건물 등록하기</b-button>
            <b-button class="b_buttondel" @click="builddel = true, buildadd = false">건물 삭제하기</b-button>
            <v-data-table
              :headers="headers"
              :items="buildings"
              :items-per-page="10"
              item-key="id"  
              class="elevation-1"
              :footer-props="{
                showFirstLastPage: true,
                firstIcon: 'mdi-arrow-collapse-left',
                lastIcon: 'mdi-arrow-collapse-right',
                prevIcon: 'mdi-minus',
                nextIcon: 'mdi-plus'
              }"
              @click:row="getoneadd = true"
            ></v-data-table>
          </div>


          



          <div class="right">
            <div class="black-bg" v-if="buildadd == true">
              <div class="white-bg">
              <form>
              <h1>건물 등록</h1>
                <div class="row">
                  <span class="title_content">건물 ID</span>
                  <input class="txtfield" type="text" name="bid" v-model="posts.bid">
                </div>
                <div class="row">
                  <span class="title_content">건물이름</span>
                  <input class="txtfield" type="text" name="bname" v-model="posts.bname">
                </div>
                <div class="row">
                  <span class="title_content">상세내용</span>
                  <input class="txtfield" type="text" value="asdf" name="bcontents" v-model="posts.bcontents">
                </div>
                <div class="row">
                  <span class="title_content">건물사진</span>
                  <v-file-input label="File input" @change="selectFile"></v-file-input>
                </div>
                  <b-button class="button_cls" @click="buildadd = false" >닫기</b-button>
                  <b-button class="button_cls" @click="submit">등록하기</b-button>
              </form>
              </div>
            </div>
          </div>





          <div class="right">
            <div class="black-bg" v-if="builddel == true">
              <div class="white-bg">
              <form @submit.prevent="postData" method="post">
              <br><br><br>
                <h1>건물 삭제</h1>
                <form @submit.prevent="senddelete">
                <div class="row">
                  <span class="title_content">건물 ID</span>
                  <input class="txtfield" type="text" name="id" v-model="id">
                </div>
                  <b-button class="button_cls" @click="builddel = false" >닫기</b-button>
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
    name: "Building",
    data() {
      return {
        getoneadd: false,
        buildadd: false,
        builddel: false,
        buildings: [],
        headers: [{
          text: 'ID',
          align: 'start',
          value: 'bid'
        },
        { text: '건물이름', value: 'bname' },
        ],
        modalopen: false,
        posts:{
          bid:null,
          bname:null,
          bcontents:null,
          bimage:null,
        },
        id: null,
      }
    },
    methods:{
      getData(){
        this.axios.get(`${API_URL}building/`).then((result)=>{
          this.buildings = result.data
        })
      },
      deleteBuilding(id){
          this.axios.delete(`${API_URL}building/` + id , {headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`,}})
        .then(()=>{
          this.getData();
          alert("삭제되었습니다.")
        })
        .catch((err)=>{
          alert(err.response.data.detail)
        })
      },
      oneBuilding(id){
        this.$router.push({ name: 'BuildingUpdate', query: {id : id} })
      },
      selectFile(file) {
        this.posts.bimage = file;
      },
      async submit() {
        const formData = new FormData();
        formData.append('bid', this.posts.bid)
        formData.append('bname', this.posts.bname)
        formData.append('bcontents', this.posts.bcontents)
        formData.append('bimage', this.posts.bimage)

        try {
          const { data } = await this.axios.post(`${API_URL}building/`, formData, {
            headers: {
              'Content-Type' : 'multipart/form-data',
              'Authorization' : `Bearer ${localStorage.getItem('token')}`,
            }
          });
          console.log(data);
          alert("생성되었습니다.")
          this.getData();
        } catch(err) {
          console.log(err);
        }
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