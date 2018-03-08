import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueForm from 'vue-form'
import VueSession from 'vue-session'

Vue.config.productionTip = false

// Enable vue-form
Vue.use(VueForm)

// Setup some global shared variables across all Vue components
const shared = {
  apiBaseUrl: process.env.API_BASE_URL,
  clientId: process.env.CLIENT_ID,
  googleClientId: process.env.GOOGLE_CLIENT_ID
}
shared.install = function () {
  var _shared = shared
  Object.defineProperty(Vue.prototype, '$shared', {
    get () {
      return _shared
    },
    set (value) {
      _shared = value
    }
  })
}
Vue.use(shared)

// Enable vue-session #across tabs and browser instances
Vue.use(VueSession, {persist: true})

// Setup axios for AJAX calls. Use default api for all axios calls
Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = shared.apiBaseUrl

// Setup router for Vue-Auth
Vue.router = router
/* Http */
// Vue.http.options.root = 'https://api-demo.websanova.com/api/v1'

Vue.use(require('@websanova/vue-auth'), {
  auth: require('@websanova/vue-auth/drivers/auth/bearer.js'),
  http: require('@websanova/vue-auth/drivers/http/axios.1.x.js'),
  router: require('@websanova/vue-auth/drivers/router/vue-router.2.x.js'),
  rolesVar: 'role',
  fetchData: {
    url: '/oauth/user'
  },
  loginData: {
    url: '/oauth/token'
  },
  refreshData: {
    url: '/oauth/token/refresh'
  },
  googleData: {
    url: '/oauth/token'
  },
  googleOauth2Data: {
    url: 'https://accounts.google.com/o/oauth2/auth',
    params: {
      client_id: shared.googleClientId
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
