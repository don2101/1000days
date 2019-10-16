import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import 'expose-loader?$!expose-loader?jQuery!jquery'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

const Swal = require('sweetalert2')

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
