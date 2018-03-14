<template>
  <div id="app">
    <appHeader></appHeader>
    <div v-if="$auth.ready() && loaded">
      <router-view/>
    </div>
    <div v-if="!$auth.ready() || !loaded">
      <div style="text-align:center; padding-top:50px;">
          Loading site...
      </div>
    </div>
    <appFooter></appFooter> </div>
</template>

<script>
import Header from './Header.vue'
import Footer from './Footer.vue'

export default {
  name: 'app',
  components: {
    appHeader: Header,
    appFooter: Footer
  },
  data () {
    return {
      context: 'app context',
      loaded: false
    }
  },
  mounted () {
    var _this = this
    setTimeout(function () {
      _this.loaded = true
    }, 500)
  },
  created () {
    this.setSessionData()
    this.axios.defaults.baseURL = this.$shared.oauthApiBaseUrl
    this.$auth.ready(function () {
      console.log('ready ' + this.context)
    })
  },
  methods: {
    // set the session info
    setSessionData () {
      // start a new session
      this.$session.start()
      if (!this.$session.get('shared')) {
        console.log('setting session from this.$shared')
        this.$session.set('shared', this.$shared)
      } else {
        console.log('setting this.$shared from session')
        this.$shared = this.$session.get('shared')
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
