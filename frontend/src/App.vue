<template>
  <div id="app">
    <router-view/>
    <appFooter></appFooter>
  </div>
</template>

<script>
import Footer from './Footer.vue'

export default {
  name: 'app',
  components: {
    appFooter: Footer
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
