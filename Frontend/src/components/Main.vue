<template>
   <div>
       <b-nav tabs justified>
        <b-nav-item :to = "{ name: 'main' }">메인</b-nav-item>
        <b-nav-item :to = "{ name: 'reservations' }">예약현황</b-nav-item>
        <b-nav-item :to = "{ name: 'buildingmng' }">건물관리</b-nav-item>
        <b-nav-item :to = "{ name: 'facilitymng' }">시설물관리</b-nav-item>
        <b-nav-item :to = "{ name: 'login'}" @click="logoutSubmit">logout</b-nav-item>
      </b-nav>

      <span style="">
        <v-card style="width: 10%; position: absolute; margin: 20px; background-color: #E6E6E6">
          <v-card-title>
            <h3 v-if="$store.state.userStore.uid != 0">{{ $store.state.userStore.uid }} 님</h3>
            <h3 v-else>관리자 님</h3>
          </v-card-title>
        </v-card>
      </span>
   <img
        src="https://ync.ac.kr/_UPLOAD/IMAGE/PopupMgr/PopupZoneUpload/2020/12/a6gv8hPBm48KJonW.JPG"
        style="height:30%; width:100%"
        alt=""
    />

      <div v-for="building in buildings" :key="building.bid" >
        <v-card style="width:20%; float:left;">
          <v-img :src=building.bimage ></v-img>
          <v-card-title>
            {{ building.bname }}
          </v-card-title>
          <v-card-subtitle>
            {{ building.bcontents }}
          </v-card-subtitle>
          <v-btn block @click="clickList(building.bname, building.bid, building.bcontents, building.bimage)">
            예약하기
          </v-btn>
        </v-card>
      </div>

    </div>
</template>

<script>
const API_URL = "http://192.168.16.28:30800/building/"
export default {
    name: 'App',
    data() {
      return {
        loginstate: ['로그인','로그아웃'],
        buildings: [],
        id: null,
        }
    },
    methods:{
      clickList(name, id, contents, image) {
        this.$router.push({ name: 'reservation', query: {name: name , id: id, contents: contents ,image: image} })
      },
      getData(){
        this.axios.get(`${API_URL}`).then((result)=>{
          this.buildings = result.data
        })
      },
      logoutSubmit() {
        this.$store.commit('logout')
        localStorage.clear()
        alert("로그아웃 했습니다.")
      },
    },
    mounted: function() {
        this.getData()
    }
}

</script>


<style>

.logina{
  margin: 0;
  position: absolute;
  top: 50%;
  width: 200px;
  -ms-transform: translate(50%, 50%);
  transform: translate(30%, 40%);
}

</style>