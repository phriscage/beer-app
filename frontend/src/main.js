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
// hack to get session variables and load as shared defaults
var vueSession = JSON.parse(window.localStorage.getItem(VueSession.key)) || {}
var sharedSession = vueSession.shared || {}
const shared = {
  beersApiBaseUrl: sharedSession.beersApiBaseUrl || process.env.BEERS_API_BASE_URL,
  oauthApiBaseUrl: sharedSession.oauthApiBaseUrl || process.env.OAUTH_API_BASE_URL,
  clientId: sharedSession.clientId || process.env.CLIENT_ID,
  clientSecret: sharedSession.clientSecret || process.env.CLIENT_SECRET,
  googleClientId: sharedSession.googleClientId || process.env.GOOGLE_CLIENT_ID
}
shared.install = function () {
  var _this = this
  Object.defineProperty(Vue.prototype, '$shared', {
    get (key) {
      if (key) {
        return _this[key]
      }
      return _this
    },
    set (value) {
      _this = value
    }
  })
}
Vue.use(shared)

// Enable vue-session #across tabs and browser instances
Vue.use(VueSession, {persist: true})

// Setup axios for AJAX calls. Use default api for all axios calls
/* axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (!error.status) {
      router.push({path: '404'})
      console.log(error)
    }
    return Promise.reject(error)
  }
) */

/* axios.interceptors.request.use(
  config => {
    console.log('interceptors')
    console.log(config.baseUrl)
    if (!config.baseUrl) {
      config.baseUrl = 'http://abc'
    }
    console.log(config.baseUrl)
    console.log(config.url)
    return config
  },
  error => {
    console.log(error)
    return Promise.reject(error)
  }
) */
Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = shared.oauthApiBaseUrl
// Vue.axios.defaults.headers.common = {
// 'X-Requested-With': 'XMLHttpRequest'
// }

// Setup router for Vue-Auth
Vue.router = router
/* Http */
// Vue.http.options.root = 'https://api-demo.websanova.com/api/v1'

// Vue-Auth will append the *Data urls without http?s:// to the Axios baseURL.
// Need a better method to set these dynamically...
var vueOptions = {
  auth: require('@websanova/vue-auth/drivers/auth/bearer.js'),
  http: require('@websanova/vue-auth/drivers/http/axios.1.x.js'),
  router: require('@websanova/vue-auth/drivers/router/vue-router.2.x.js'),
  rolesVar: 'role',
  fetchData: {
    url: '/user'
  },
  loginData: {
    url: '/token'
  },
  refreshData: {
    url: '/token/refresh'
    // enabled: false
  },
  googleData: {
    url: '/token'
  },
  googleOauth2Data: {
    url: 'https://accounts.google.com/o/oauth2/auth',
    params: {
      client_id: shared.googleClientId
    },
    response_type: 'token id_token'
    // params: {
    // redirect_uri: function () {
    // return this.options.getUrl() + '/login'
    // }
    // }
  },
  apigeeOauth2Data: {
    url: shared.oauthApiBaseUrl + '/authorize',
    params: {
      client_id: shared.clientId
    },
    response_type: 'code',
    scope: 'openid email profile'
  }
  // refreshPerform: () => {
  // console.log('refreshPerform')
  // },
}
Vue.use(require('@websanova/vue-auth'), vueOptions)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  created () {
    console.log('created')
    this.$session.start()
    if (!this.$session.get('shared')) {
      console.log('setting session from this.$shared')
      this.$session.set('shared', this.$shared)
    } else {
      console.log('setting this.$shared from session')
      this.$shared = this.$session.get('shared')
    }
    this.axios.defaults.baseURL = this.$shared.oauthApiBaseUrl
  },
  render: h => h(App)
}).$mount('#app')

// new Vue({
// el: '#app',
// template: '<App/>',
// router,
// components: { App }
// }).$mount('#app')
