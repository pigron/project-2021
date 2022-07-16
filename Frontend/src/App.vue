<template>
  <div id="back">
    <div >
      <router-view></router-view>
    </div>      
  </div>
</template>

<script>

export default {
  loginck: false,
  name: 'App',
  data() {
      return {
          loginstate: ['login','logout'],
        }
      },
      methods: {
      logoutSubmit() {
        this.$store.commit('logout')
        localStorage.clear()
        alert("로그아웃 했습니다.")
      },
    },
}
</script>

<style>
h4{
text-align: right;
}
.logina{
  width: 100px;
  height: 50px;
  padding: 10px;
  margin: 1em;
  position: absolute;
  top: 20px;
  right: 30px;
}
.back {
  background-color: #A4A4A4;
}
</style>