import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import fullpage from './plugins/LandingView/fullpage.js'


Vue.config.productionTip = false;
new Vue({
  fullpage,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app');
