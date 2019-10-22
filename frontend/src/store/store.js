import Vue from 'vue';
import Vuex from 'vuex';
import data from './modules/data'
import auth from './modules/auth'

Vue.use(Vuex);

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {
        data,
        auth
    }
});