import Vue from 'vue'
import App from './App.vue'
import router from './router'

import Swal from 'sweetalert2'
import 'expose-loader?$!expose-loader?jQuery!jquery'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

import vuetify from './plugins/vuetify';
import store from './store/store'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import fullpage from './plugins/LandingView/fullpage.js'

import VModal from 'vue-js-modal'
Vue.use(VModal, { dynamic: true })

Vue.config.productionTip = false;
new Vue({
  store,
  fullpage,
  vuetify,
  Swal,
  router,
  render: h => h(App)
}).$mount('#app');
