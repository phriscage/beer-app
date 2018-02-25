import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

Vue.router = router
/* Http */
// Vue.http.options.root = 'https://api-demo.websanova.com/api/v1'

Vue.use(require('@websanova/vue-auth'), {
  auth: require('@websanova/vue-auth/drivers/auth/bearer.js'),
  http: require('@websanova/vue-auth/drivers/http/axios.1.x.js'),
  router: require('@websanova/vue-auth/drivers/router/vue-router.2.x.js'),
  rolesVar: 'role',
  fetchData: {
    url: 'http://localhost:5000/api/oauth/user'
  },
  loginData: {
    url: 'http://localhost:5000/api/oauth/token'
  },
  refreshData: {
    url: 'http://localhost:5000/api/oauth/token/refresh'
  },
  googleData: {
    url: 'http://localhost:5000/api/oauth/token'
  },
  googleOauth2Data: {
    url: 'https://accounts.google.com/o/oauth2/auth',
    params: {
      client_id: '823357352754-ej9k1n120u9nn8pljr5gbghesjm0h5tk.apps.googleusercontent.com'
    }
    // params: {
      // redirect_uri: function () {
        // return this.options.getUrl() + '/login'
      // }
    // }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
}).$mount('#app')

// new Vue({
  // el: '#app',
  // template: '<App/>',
  // router,
  // components: { App }
// }).$mount('#app')
