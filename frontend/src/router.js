import Vue from 'vue'
import Router from 'vue-router'
import store from './store/index'
import HomePage from './views/HomePage'
import MainPage from './views/MainPage'
import AccountPage from './views/AccountPage'
import ConfirmPage from './views/ConfirmPage'

Vue.use(Router)

export default new Router({

    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'HomePage',
            component: HomePage
        },
         {
            path: '/main',
            name: 'MainPage',
            component: MainPage
        },
                 {
            path: '/mypage',
            name: 'AccountPage',
            component: AccountPage,
        },
             {
            path: '/access',
            name: 'ConfirmPage',
            component: ConfirmPage
        },
    ]
})
