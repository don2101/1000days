import Vue from 'vue'
import Router from 'vue-router'

import HomePage from './views/HomePage'
import AccountPage from './views/AccountPage'
import ConfirmPage from './views/ConfirmPage'
import RegisterPage from './views/RegisterPage'
import LoginPage from './views/LoginPage'
import BabyInfoPage from './views/BabyInfoPage'
import PersonalPage from "./views/PersonalPage";
import WritingPage from "./views/WritingPage"

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
        {
            path: '/babyinfo',
            name: 'BabyInfoPage',
            component: BabyInfoPage
        },
        {
            // test 자리에 username이 들어가도록 함
            path:'/test/mydiary',
            name: 'PersonalPage',
            component: PersonalPage
        },
        {
            path:'/mydiary/new',
            name: 'WritingPage',
            component: WritingPage
        }
    ]
})
