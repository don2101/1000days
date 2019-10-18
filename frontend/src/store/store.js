import Vue from 'vue';
import Vuex from 'vuex';
import auth from 'modules/auth'
import data from 'modules/data'
import modules from './modules'

Vue.use(Vuex);

const store = new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    auth,
    data,
    modules
});

for (const moduleName of Object.keys(modules)) {
    if (modules[moduleName].actions && modules[moduleName].actions.initStore) {
        store.dispatch(`${moduleName}/initStore`)
    }
}

export default store;