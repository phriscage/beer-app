<template>
  <div>
    <div v-show="!id_token || !type">
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
    <div v-show="id_token && type">
        Verifying {{ type }} id_token...
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
      data: {
        rememberMe: false,
        fetchUser: true
      },
      code: this.$route.query.code,
      type: this.$route.params.type,
      access_token: this.getFragmentValue('access_token'),
      id_token: this.getFragmentValue('id_token'),
      response_type: this.$route.params.type,
      error: ''
    }
  },
  mounted () {
    console.log('redirect: ' + this.$auth.redirect())
    console.log('id_token: ' + this.id_token)
    if (this.id_token) {
      /* this.$auth.oauth2({
        code: true,
        provider: this.type,
        headers: {
          'X-Provider': this.type,
          'X-Provider-id_token': this.id_token,
          'X-Provider-access_token': this.access_token
        },
        params: {
        },
        success: function (res) {
          console.log('success ' + this.context)
        },
        error: function (res) {
          console.log('error ' + this.context)
        }
      }) */

      // trying to login
      var redirect = this.$auth.redirect()
      console.log('redirect: ' + redirect)
      this.$auth.login({
        headers: {
          'X-Provider': this.type,
          'X-Provider-id_token': this.id_token,
          'X-Provider-access_token': this.access_token
        },
        rememberMe: this.data.rememberMe,
        redirect: {
          name: 'account'
        },
        fetchUser: this.data.fetchUser
      })
      .then(() => {
        console.log('success ' + this.context)
      }, (res) => {
        console.log('error ' + this.context)
        this.error = res.data
      })
    }
  },
  methods: {
    // parse access token
    getFragmentValue (key) {
      let params = this.$route.hash.split('&')
      if (params.length > 1) {
        for (var i = 0; i < params.length; i++) {
          let pair = params[i].split('=')
          console.log(pair)
          if (pair[0] === key) {
            console.log('found')
            return pair[1]
          }
        }
      }
    },
    login () {
      console.log(this.credentials.username)
      console.log(this.credentials.password)
    },
    social (type) {
      console.log(this.$auth)
      console.log(this.$auth.oauth2)
      this.$auth.oauth2({
        provider: type || this.type,
        response_type: 'token id_token'
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
