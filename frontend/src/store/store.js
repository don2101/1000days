import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate'

import data from './modules/data'
import auth from './modules/auth'
//import moduleName from "./module_moduleName";

Vue.use(Vuex);

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {
        data,
        auth
    }
});




// 아래: 1차 merge 전 index.js 내용

// const modules = {
//     moduleName,
// }
//
// const plugins= [
//     createPersistedState({
//         paths:[
//         'moduleName',
//         ]
//         })
//     ];
//
// Vue.use(Vuex);
//
// export default new Vuex.Store({
//     modules,
//     plugins
// });
