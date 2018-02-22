<template>
  <div>
    <div v-show="!code || !type">
      <p>Login</p>
      <form id="login" class="ui large form">
        <div class="ui stacked segment">
          <p>Login via credentials</p>
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input
                type="text"
                name="username"
                placeholder="Username"
                v-model="credentials.username"
              >
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input
                type="password"
                name="password"
                placeholder="Password"
                v-model="credentials.password"
              >
            </div>
          </div>
          <div class="ui fluid large blue submit button" @click="login()">Login</div>
        </div>

        <div class="ui error message" v-if="error">
          <p>{{ error }}</p>
        </div>
      </form>

      <div class="ui clearing segment">
        <p>Login via @google credentials</p>
        <button class="ui google plus button" v-on:click="social('google')">
          <i class="google icon"></i>
            Google
        </button>
        <!--<button class="ui facebook button" v-on:click="social('facebook')">
          <i class="facebook icon"></i>
            Facebook
        </button>-->
      </div>
    </div>
    <div v-show="code && type">
        Verifying {{ type }} code...
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      context: 'oauth2 context',
      credentials: {
        username: '',
        password: ''
      },
      code: this.$route.query.code,
      type: this.$route.params.type,
      error: ''
    }
  },
  mounted () {
    if (this.code) {
      this.$auth.oauth2({
        url: 'https://api.ab.com',
        code: true,
        provider: this.type,
        params: {
          code: this.code
        },
        success: function (res) {
          console.log('success ' + this.context)
        },
        error: function (res) {
          console.log('error ' + this.context)
        }
      })
    }
  },
  methods: {
    login () {
      console.log(this.credentials.username)
      console.log(this.credentials.password)
    },
    social (type) {
      console.log(this.$auth)
      console.log(this.$auth.oauth2)
      this.$auth.oauth2({
        provider: type || this.type
      })
    }
  }
}
</script>
<style>
#login {
  text-align: left;
  width: 340px;
}
</style>
