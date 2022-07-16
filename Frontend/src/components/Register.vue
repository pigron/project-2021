<template>
    <v-app id="app">
        <v-main>
            <v-container
                style="position: relative; top: 10%; margin-left: 25%"
                class="text-xs-center"
            >
                <v-layout row wrap class="text-xs-center">
                    <v-flex>
                        <v-card flat class="mx-auto" max-width="70%">
                            <v-row style="margin-top: 20px">
                                <v-col>
                                    <v-form style="width: 600px; height: 300px">
                                        <div class="mx-3">
                                            <h2>학번</h2>
                                            <div class="mx-1">
                                                <v-text-field
                                                    placeholder="uid"
                                                    v-model="posts.uid"
                                                    required
                                                ></v-text-field>
                                            </div>
                                        </div>
                                        <div class="mx-3">
                                            <h2>비밀번호</h2>
                                            <div class="mx-1">
                                                <v-text-field
                                                    placeholder="password"
                                                    type="password"
                                                    v-model="posts.password"
                                                    required
                                                ></v-text-field>
                                            </div>
                                        </div>
                                        <div class="mx-3">
                                            <h2>email</h2>
                                            <div class="mx-1">
                                                <v-text-field
                                                    placeholder="email"
                                                    v-model="posts.email"
                                                    required
                                                ></v-text-field>
                                            </div>
                                        </div>
                                        <div class="mx-3">
                                            <h2>학과</h2>
                                            <div class="mx-1">
                                                <v-select
                                                    v-model="posts.department"
                                                    :items="departments"
                                                    :rules="[v => !!v || 'department is required']"
                                                    label="학과"
                                                    required
                                                ></v-select>
                                            </div>
                                        </div>
                                        <div class="mx-3">
                                            <h2>학년</h2>
                                            <div class="mx-1">
                                                <v-select
                                                    v-model="posts.grade"
                                                    :items="grade"
                                                    :rules="[v => !!v || 'grade is required']"
                                                    label="학년"
                                                    required
                                                ></v-select>
                                            </div>
                                        </div>
                                        <div class="mx-3">
                                            <h2>전화번호</h2>
                                            <div class="mx-1">
                                                <v-text-field
                                                    placeholder="pnumber"
                                                    v-model="posts.pnumber"
                                                    required
                                                ></v-text-field>
                                            </div>
                                        </div>
                                        <div class="mx-3">
                                            <h2>직업</h2>
                                            <div class="mx-1">
                                                <v-select
                                                    v-model="posts.auth"
                                                    :items="auth"
                                                    :rules="[v => !!v || 'auth is required']"
                                                    label="직업"
                                                    required
                                                ></v-select>
                                            </div>
                                        </div>

                                        <v-card-actions>
                                            <v-btn
                                                color="#2c4f91"
                                                dark
                                                large
                                                block
                                                @click="postData"
                                                >회원가입</v-btn
                                            >
                                        </v-card-actions>
                                    </v-form>
                                </v-col>
                            </v-row>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
const API_URL = "http://192.168.16.28:30800/register/"

  export default {
    name: "register",
    data:() => {
      return {
        posts:{
          uid:null,
          password:null,
          email:null,
          department:null,
          grade:null,
          pnumber:null,
          auth:null,
        },
        departments: [
            '사이버보안과',
            '간호학과',
            '기계과',
            '전자과'
        ],
        grade: [
            '1학년',
            '2학년',
            '3학년',
            '4학년'
        ],
        auth: [
            '1',
            '2',
            '3',
        ]
      }
    },

    methods:
    {
      postData(e){
          this.axios.post(`${API_URL}` + `?department=${this.posts.department}&grade=${this.posts.grade}&auth=${this.posts.auth}`, { uid:this.posts.uid, password:this.posts.password, email:this.posts.email, phonenumber:this.posts.pnumber })
            .then((result)=>{
              console.warn(result);
              alert("생성되었습니다.")
            })
            .catch((err) => {
              alert(err.response.data.detail[0].msg)
            })
        e.preventDefault();
      },
    },
  }

</script>