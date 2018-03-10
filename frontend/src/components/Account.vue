<template>
  <div class="ui container">
    <p>Account</p>
    </hr>
    <p><a v-on:click="fetch()" href="javascript:void(0);">Test fetch user</a></p>
    <p><a v-on:click="refresh()" href="javascript:void(0);">Test refresh token</a></p>
    <div class="ui form">
      <div class="field">
        <label>Access Token</label>
        <textarea rows="1">{{ $auth.token() }}</textarea>
      </div>
      <div class="field">
        <label>ID Token | <a target="_blank" v-bind:href="'https://jwt.io/?value='+ $auth.token('id_token')">jwt.io</a></label>
        <textarea rows="6">{{ $auth.token('id_token') }}</textarea>
     </div>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
      context: 'account context'
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
