<template>
    <v-app style="background-color: #E6E6E6">
        <v-main>
            <v-container
                style="position: relative; top: 20%; margin-left: 15%; background-color: #E6E6E6"
                class="text-xs-center"
            >
                <v-layout row wrap class="text-xs-center">
                    <v-flex>
                        <v-card flat class="mx-auto" max-width="30%" max-height="50%">
                            <v-row style="margin-top: 10px; background-color: #E6E6E6">
                                <v-col>
                                    <v-form style="width: 500px; height: 300px;">
                                        <v-card 
                                            elevation="2"
                                            style="background-color: #FFFFFF;">
                                            <v-card-subtitle>
                                            <v-img
                                                height="90" 
                                                src="https://ync.ac.kr/homepage/kor/_Img/Layout/logo.png">
                                            </v-img>
                                            </v-card-subtitle>
                                            <v-card-title>
                                                YNC예약관리시스템 로그인
                                            </v-card-title>
                                            <v-card-text>
                                                <div class="mx-3">
                                                    <h3>email</h3>
                                                    <div class="mx-1">
                                                        <v-text-field
                                                            placeholder="email"
                                                            v-model="username"
                                                            required
                                                        ></v-text-field>
                                                    </div>
                                                </div>
                                                <div class="mx-3">
                                                    <h3>password</h3>
                                                    <div class="mx-1">
                                                        <v-text-field
                                                            placeholder="password"
                                                            type="password"
                                                            v-model="password"
                                                            required
                                                        ></v-text-field>
                                                    </div>
                                                </div>
                                            </v-card-text>
                                            <v-card-actions style="width:50px">
                                                <v-btn
                                                    color="#2E64FE"
                                                    dark
                                                    large
                                                    @click="loginSubmit"
                                                    >로그인</v-btn
                                                >
                                                <v-btn
                                                    color="#2E64FE"
                                                    dark
                                                    large
                                                    @click="registerGo"
                                                    
                                                    >회원가입</v-btn
                                                >
                                            </v-card-actions>
                                            <v-card-actions>
                                                
                                            </v-card-actions>
                                        </v-card>
                                        
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
const HOST = "http://192.168.16.28:30800/login"

export default {
    data() {
        return {
            username: '',
            password: '',
        };
    },

    methods: {
        async test() {
            await this.$bvToast.toast(`비밀번호가 틀렸습니다.`, {
                title: 'hello',
                toaster: 'b-toaster-top-center',
                variant: 'primary',
                solid: true,
                noAutoHide: true,
                noCloseButton: true
            })
        },
        loginSubmit() {
            const params = new URLSearchParams()
            params.append('username', this.username)
            params.append('password', this.password)

            if (this.username == '') {
                alert("이메일을 입력해주세요")
            } else if (this.password == '') {
                alert("비밀번호를 입력해주세요")
            } else {
                try {
                    this.axios
                        .post(`${HOST}`, params,  {
                            headers: {
                                "Content-Type": `application/x-www-form-urlencoded`,
                            },
                        })
                        .then((res) => {
                            if (res.status === 200) {
                                localStorage.setItem("token", res.data.access_token);
                                localStorage.setItem("uid", res.data.uid);
                                this.$store.commit("login", res.data);
                                this.$router.push("/main");
                                alert("로그인 했습니다.")
                            }
                        })
                        .catch((err) => {
                            const errMsg = err.response.data.detail;
                            if (errMsg === 'Incorrect password') {
                                alert(`비밀번호가 틀렸습니다.`)
                            }
                        });
                } catch (error) { return }
            }
        },
        registerGo() {
            this.$router.push("/register");
        },
    },
};
</script>

<style>
    v-card {
        background-color: #FFFFFF;
    }
</style>