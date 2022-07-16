import Vue from 'vue'
import Vuex from 'vuex'
import Router from 'vue-router'

import Main from '../components/Main.vue';
import Buildingmng from '../components/Building_mng.vue';
import Facilitymng from '../components/Facility_mng.vue';
import Login from '../components/LoginPage.vue'
import Reservation from '../components/Reservation.vue';
import Reservations from '../components/Reservations.vue';
import Register from '../components/Register.vue'
import BuildingUpdate from '../components/Building_update.vue'
import Store from '@/store/'

Vue.use(Router)
Vue.use(Vuex)

const requireAuth = () => (to, from, next) => {
    if (Store.state.userStore.uid !== '') {
        return next();
    }
    next('/');
}

const adminAuth = () => (to, from, next) => {
    if (localStorage.getItem('uid') === '0') {
        return next();
    }
    alert('관리자만 사용가능합니다.');
}

export default new Router ({
    mode: 'history',
    routes: [
        {
            path: '/main',
            component: Main,
            name: 'main',
            beforeEnter: requireAuth()
        },
        {
            path: '/buildingmng',
            component: Buildingmng,
            name: 'buildingmng',
            beforeEnter: adminAuth()
        },
        {
            path: '/facilitymng',
            component: Facilitymng,
            name: 'facilitymng',
            beforeEnter: adminAuth(),
        },
        {
            path: '/',
            component: Login,
            name: 'login'
        },
        {
            path: '/reservation/',
            component: Reservation,
            name: 'reservation',
            beforeEnter: requireAuth(),
        },
        {
            path: '/reservations',
            component: Reservations,
            name: 'reservations',
            beforeEnter: requireAuth()
        },
        {
            path: '/register',
            component: Register,
            name: 'register',
        },
        {
            path: '/buildingUpdate',
            component: BuildingUpdate,
            name: 'BuildingUpdate',
            beforeEnter: requireAuth()
        },
    ]
})