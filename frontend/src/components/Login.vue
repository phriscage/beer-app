<template>
  <div>
    <div v-show="!id_token || !type">
      <p>Login</p> <form id="login" class="ui large form">
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
                placeholder="Password" v-model="credentials.password"
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
      context: 'login context',
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
    if (this.id_token) {
      // store third-party id_token and access token
      var redirect = this.$auth.redirect()
      console.log('redirect: ' + redirect)
      var querystring = require('querystring')
      this.$auth.login({
        data: querystring.stringify({
          grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
          assertion: this.id_token
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-Provider': this.type,
          'Authorization': 'Bearer ' + this.access_token
        },
        rememberMe: this.data.rememberMe,
        redirect: {name: redirect ? redirect.from.name : 'account'},
        fetchUser: this.data.fetchUser
      })
      .then(() => {
        this.$auth.token('id_token', this.id_token)
        console.log('success ' + this.context)
        console.log('this.$auth.token(): ' + this.$auth.token())
      }, (res) => {
        console.log('error ' + this.context)
        this.error = res.data
      })
    } else {
      console.log('Id Token URL fragment DNE')
    }
  },
  methods: {
    // parse url fragment by parameter key
    getFragmentValue (key) {
      let params = this.$route.hash.split('&')
      if (params.length > 1) {
        for (var i = 0; i < params.length; i++) {
          let pair = params[i].split('=')
          if (pair[0] === key) {
            console.log('found: ' + pair)
            return pair[1]
          }
        }
      }
    },
    login () {
      // TO-DO
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
