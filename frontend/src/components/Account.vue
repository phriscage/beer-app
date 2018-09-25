<template>
  <div class="ui container">
    <p>Account</p>
    <br>
    <p><a v-on:click="fetch()" href="javascript:void(0);">Test fetch user</a></p>
    <p><a v-on:click="refresh()" href="javascript:void(0);">Test refresh token</a></p>
    <div class="ui form">
      <div class="field">
        <label>Access Token | <a target="_blank" v-bind:href="'https://jwt.io/?value='+ token">jwt.io</a></label>
        <textarea rows="6" v-model=token></textarea>
      </div>
      <div class="field">
        <label>ID Token | <a target="_blank" v-bind:href="'https://jwt.io/?value='+ id_token">jwt.io</a></label>
        <textarea rows="6" v-model=id_token></textarea>
     </div>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
      context: 'account context',
      token: this.$auth.token(),
      id_token: this.$auth.token('id_token')
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
