import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import moduleName from './module_moduleName'

const modules = {
    moduleName,
}

const plugins= [
    createPersistedState({
        paths:[
        'moduleName',
        ]
        })
    ];

Vue.use(Vuex);

export default new Vuex.Store({
    modules,
    plugins
});
