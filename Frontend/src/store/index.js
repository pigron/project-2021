import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

import userStore from '@/store/modules/userStore.js';

const store = new Vuex.Store({
    modules: {
        userStore: userStore,
    },
    plugins: [createPersistedState({
        paths: ["userStore"]
    })]
})

export default store