import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage'
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