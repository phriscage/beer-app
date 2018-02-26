import Vue from 'vue'
import Router from 'vue-router'
const routerOptions = [
  {
    path: '/',
    name: 'home',
    component: 'Home'
  },
  {
    path: '/about',
    name: 'about',
    component: 'About'
  },
  {
    path: '/account',
    name: 'account',
    component: 'Account',
    meta: {auth: true}
  },
  {
    path: '/login',
    name: 'login',
    component: 'Login',
    meta: {auth: false}
  },
  {
    path: '/login/:type',
    name: 'oauth2-type',
    component: 'Login'
  },
  {
    path: '/beers',
    name: 'beers',
    component: 'Beers'
  },
  {
    path: '/random',
    name: 'random',
    component: 'Random',
    meta: {auth: true}
  },
  {
    path: '*',
    component: 'NotFound'
  }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
