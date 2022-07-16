import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'
import Vuetify from 'vuetify'
import router from './router/index.js'
import store from './store/index.js'


import 'vuetify/dist/vuetify.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App.vue'

Vue.use(Vuetify)
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(VueRouter)

const opts = {}

export default new Vuetify(opts)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
  vuetify: new Vuetify()
}).$mount('#app')
