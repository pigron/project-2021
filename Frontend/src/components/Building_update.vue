<template>
        
    <div>
        <h1> 건물상세정보 </h1>
        {{ oneData($route.query.id) }}
        <div style="weigh=20px" >
        <v-card>
            <v-img :src= '`${buildings.bimage}`' ></v-img>
            <v-card-title>
                {{ buildings.bname }}
            </v-card-title>
            <v-card-subtitle>
                {{ buildings.bcontents }}
            </v-card-subtitle>
        </v-card>
    </div>
    </div>
</template>

<script>
const API_URL = "http://192.168.16.28:30800/"

  export default {
    data() {
      return {
        buildings: [],
        posts:{
          bid:null,
          bname:null,
          bcontents:null,
          bimage:null,
        },
      }
    },
    methods:{
      oneData(id){
        this.axios.get(`${API_URL}building/${id}` , {headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`,}} ).then((result)=>{
          this.buildings = result.data
        })
      }
    },
    mounted: function() {
      this.oneData()
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