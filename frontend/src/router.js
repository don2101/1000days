import Vue from 'vue'
import Router from 'vue-router'
import store from './store/index'
import HomePage from './views/HomePage'
import AccountPage from './views/AccountPage'
import ConfirmPage from './views/ConfirmPage'
import RegisterPage from './views/RegisterPage'
import LoginPage from './views/LoginPage'

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
            path: '/mypage',
            name: 'AccountPage',
            component: AccountPage,
        },
         {
            path: '/access',
            name: 'ConfirmPage',
            component: ConfirmPage
        },

             {
            path: '/signup',
            name: 'RegisterPage',
            component: RegisterPage
        },
          {
            path: '/login',
            name: 'LoginPage',
            component: LoginPage
        },
    ]
})
