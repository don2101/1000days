import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'expose-loader?$!expose-loader?jQuery!jquery'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

const Swal = require('sweetalert2')

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
