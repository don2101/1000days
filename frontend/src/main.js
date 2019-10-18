import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import Swal from 'sweetalert2'
import 'expose-loader?$!expose-loader?jQuery!jquery'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import vuetify from './plugins/vuetify';

new Vue({
  vuetify,
  Swal,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
