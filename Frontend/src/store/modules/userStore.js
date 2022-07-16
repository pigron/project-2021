import router from '@/router'

const userStore = {
    state: {
        token: '',
        uid: '',
        auth: '',
        token_type:''
    },
    mutations: {
        login (state, payload) {
            state.token = payload.access_token
            state.uid = payload.uid
            state.auth = payload.auth
            state.token_type = payload.token_type
        },
        loginCheck (state) {
            if (!state.token) {
                router.push({
                    name: 'login'
                }).catch(error => {
                    console.log(error)
                })
            }
        },
        logout (state) {
            state.token = ''
            state.uid = ''
            state.auth = ''
            state.token_type = ''
        }
    }
}

export default userStore