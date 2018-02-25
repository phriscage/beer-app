<template>
  <div>
    <h3>Account</h3>
    <b>Username:</b> {{ $auth.user().username }}
    <hr/>
    <ul>
      <li><a v-on:click="fetch()" href="javascript:void(0);">Test fetch user</a></li>
      <li><a v-on:click="refresh()" href="javascript:void(0);">Test refresh token</a></li>
    </ul>
    <p>Version: {{ vueVersion }}</p>
  </div>
</template>

<script>
import Vue from 'vue'
export default {
  data () {
    return {
      context: 'account context',
      vueVersion: Vue.version
    }
  },
  methods: {
    fetch () {
      this.$auth.fetch({
        success () {
          console.log('success ' + this.context)
        },
        error () {
          console.log('error ' + this.context)
        }
      })
    },
    refresh () {
      this.$auth.refresh({
        success () {
          console.log('success ' + this.context)
        },
        error () {
          console.log('error ' + this.context)
        }
      })
    }
  }
}
</script>
