<template>
  <div>
    <img src="../assets/logo.png">
    <p>About</p>
    <p>Version: {{ vueVersion }}</p>
  </div>
</template>

<script>
import Vue from 'vue'
export default {
  data () {
    return {
      vueVersion: Vue.version
    }
  }
}
</script>
