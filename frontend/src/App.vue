<template>
<!--    <v-app v-if="!loginedUserInfo">-->
<!--        <LandingView />-->
<!--    </v-app>-->

    <v-app>
        <Header/>
        <router-view/>
        <Footer/>
    </v-app>
</template>

<script>
    import {mapGetters} from 'vuex'
    import Header from './components/Header'
    import Footer from './components/Footer'
    import LandingView from './components/LandingView'

    export default {
        name: 'App',
        components: {
            Header,
            Footer,
            LandingView
        },
        methods:{

        },
        mounted: {

        },
        computed: {
            // 로그인한 유저가 없으면 Landing-view를 띄워주고 있으면 Header, Footer, router-view 를 띄워준다
            ...mapGetters('data', ['loginedUserInfo'])
        }
    };
</script>
