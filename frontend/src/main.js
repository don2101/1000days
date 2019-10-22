import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store/store'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import fullpage from './plugins/LandingView/fullpage.js'


Vue.config.productionTip = false;
new Vue({
  store,
  fullpage,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app');
