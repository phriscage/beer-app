<template>
  <div id="app">
    <appHeader></appHeader>
    <div v-if="authSuccess()">
      <router-view/>
    </div>
    <div v-if="authFail()">
      <div class="ui active inverted dimmer">
        <div class="ui text loader">Loading site...</div>
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
    this.$auth.ready(function () {
      console.log('ready ' + this.context)
    })
  },
  methods: {
    authSuccess () {
      return (this.$auth.ready() && this.loaded)
    },
    authFail () {
      return (!this.$auth.ready() || !this.loaded)
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
