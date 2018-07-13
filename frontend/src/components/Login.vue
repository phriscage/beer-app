<template>
  <div>
    <div class="ui error message" v-if="error">
      <i v-on:click="onErrorClose()" class="close icon"></i>
      <div class="header">Something broke!</div>
      <div id="error"><pre>{{ errorMessage }}</pre></div>
    </div>
    <div v-show="!id_token && !type">
      <!-- Login and Verification Segment -->
      <div class="ui stacked segment">
        <!-- Verify Authorization Code form -->
        <div v-show="code">
          <form id="code" class="ui large form">
            <div class="ui clearing segment">
              <p>Verify Authorization Code</p>
              <div class="ui fluid large blue submit button" @click="verifyCode()">Continue</div>
            </div>
          </form>
        </div>
        <!-- Login form -->
        <div v-show="!code">
          <form id="login" class="ui large form">
            <div class="ui clearing segment">
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
              </br>
              <div class="ui toggle checkbox custom">
                <input id="grantType" v-on:click="onGrantTypeClick()" v-model.lazy="data.grantType" true-value="authorization_code" false-value="password" type="checkbox">
                <label for="grantType">Grant Type: <b>{{ data.grantType }}</b></label>
              </div>
            </div>
          </form>
          <!-- 3rd party Identity Provider -->
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
        <!-- Additional Configurations -->
        <div class="ui clearing segment">
          <div class="ui toggle checkbox custom">
            <input id="rememberMe" v-model="data.rememberMe" type="checkbox">
            <label for="rememberMe">Remember Me</label>
          </div>
          <br>
          <div class="ui toggle checkbox custom">
            <input id="accessTokenFormat" v-on:click="onAccessTokenFormatClick()" v-model.lazy="data.accessTokenFormat" true-value="jwt" false-value="opaque" type="checkbox">
            <label for="accessTokenFormat">Access Token Format: <b>{{ data.accessTokenFormat }}</b></label>
          </div>
        </div>
      </div>
    </div>
    <!-- End Login and Verification Segment -->
    <div v-show="id_token && type">
      <p>Verifying {{ type }} id_token...</p>
    </div>
  </div>
</template>

<script>
var querystring = require('querystring')
var axios = require('axios')

export default {
  data () {
    return {
      context: 'login context',
      credentials: {
        username: '',
        password: ''
      },
      data: {
        test: false,
        rememberMe: false,
        grantType: this.$session.get('grant_type') || 'password',
        accessTokenFormat: this.$session.get('access_token_format') || 'opaque',
        fetchUser: true
      },
      code: this.$route.query.code,
      type: this.$route.params.type,
      access_token: this.getFragmentValue('access_token'),
      id_token: this.getFragmentValue('id_token'),
      state: this.getFragmentValue('state'),
      response_type: this.$route.params.type,
      error: false,
      errorMessage: ''
    }
  },
  mounted () {
    // id_token found from 3rd party IdP
    if (this.id_token) {
      // state found from 3rd party IdP
      if (this.state) {
        console.log('this.state: ' + this.state)
      }
      // store third-party id_token and access token
      var redirect = this.$auth.redirect()
      console.log(this.$auth.options)
      // TODO need a better method to update all vue-auth default URLs
      this.axios.defaults.baseURL = this.$shared.oauthApiBaseUrl
      this.$auth.login({
        data: querystring.stringify({
          grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
          assertion: this.id_token,
          client_id: this.$shared.clientId,
          token_format: this.$session.get('access_token_format')
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
        console.log(res)
        if (res.response && res.response.status) {
          this.errorMessage = 'HTTP Status: ' + res.response.status + '\n' +
               'Body: ' + JSON.stringify(res.response.data, null, 4)
        } else {
          this.errorMessage = res.toString()
        }
        this.error = true
      })
    } else {
      console.log('Id Token URL fragment DNE')
    }
  },
  methods: {
    // parse url fragment by parameter key
    getFragmentValue (key) {
      let fragment = this.$route.hash.replace(/^#/, '')
      let params = fragment.split('&')
      if (params.length > 1) {
        for (var i = 0; i < params.length; i++) {
          let pair = params[i].split('=')
          if (pair[0] === key) {
            return pair[1]
          }
        }
      }
    },
    verifyCode () {
      console.log('Validating Authorization Code ' + this.code)
      var redirect = this.$auth.redirect()
      this.$auth.login({
        data: querystring.stringify({
          grant_type: 'authorization_code',
          code: this.code,
          client_id: this.$shared.clientId,
          client_secret: this.$shared.clientSecret,
          redirect_uri: 'http://localhost:8080' + this.$route.path,
          token_format: this.$session.get('access_token_format')
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
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
        console.log(res)
        if (res.response && res.response.status) {
          this.errorMessage = 'HTTP Status: ' + res.response.status + '\n' +
               'Body: ' + JSON.stringify(res.response.data, null, 4)
        } else {
          this.errorMessage = res.toString()
        }
        this.error = true
      })
    },
    login () {
      // TO-DO
      let _this = this
      var redirect = _this.$auth.redirect()
      // Check the grantType for the login option
      console.log('grant_type ' + _this.data.grantType)
      if (_this.data.grantType === 'password') {
        console.log('Resource Owner Password Grant Type')
        _this.$auth.login({
          data: querystring.stringify({
            username: _this.credentials.username,
            password: _this.credentials.password,
            grant_type: _this.data.grantType,
            client_id: _this.$shared.clientId,
            client_secret: _this.$shared.clientSecret,
            token_format: _this.data.accessTokenFormat
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Provider': _this.type
          },
          rememberMe: _this.data.rememberMe,
          redirect: {name: redirect ? redirect.from.name : 'account'},
          fetchUser: _this.data.fetchUser
        })
        .then(() => {
          // this.$auth.token('id_token', '', 'remove')
          console.log('success ' + _this.context)
          console.log('this.$auth.token(): ' + _this.$auth.token())
        }, (res) => {
          console.log('error ' + _this.context)
          console.log(res)
          if (res.response && res.response.status) {
            _this.errorMessage = 'HTTP Status: ' + res.response.status + '\n' +
                 'Body: ' + JSON.stringify(res.response.data, null, 4)
          } else {
            _this.errorMessage = res.toString()
          }
          _this.error = true
        })
      } else {
        console.log('Authorization Code Grant Type')
        axios.post('/authorize',
          querystring.stringify({
            username: _this.credentials.username,
            password: _this.credentials.password,
            response_type: 'code',
            redirect_uri: 'http://localhost:8080' + _this.$route.path,
            client_id: _this.$shared.clientId
          })
        )
        .then(function (response) {
          console.log(response)
          if (response.data && response.data.code) {
            console.log('code: ' + response.data.code)
            // _this.$router.push({name: 'login', params: {type: 'code'}})
            _this.$router.push('/login?code=' + response.data.code)
            _this.$router.go()
          }
        })
        .catch(function (error) {
          console.log(error)
        })
      }
    },
    social (type) {
      // set googleOauth2Data client_id
      this.$auth.options.googleOauth2Data.params.client_id = this.$shared.googleClientId
      this.$auth.oauth2({
        provider: type || this.type,
        rememberMe: this.data.rememberMe,
        response_type: 'token id_token'
      })
    },
    onErrorClose: function () {
      this.error = !this.error
      console.log(this.error)
    },
    onGrantTypeClick: function () {
      var grantType = 'password'
      if (this.data.grantType === 'password') {
        grantType = 'authorization_code'
      }
      this.$session.set('grant_type', grantType)
    },
    onAccessTokenFormatClick: function () {
      var accessTokenFormat = 'opaque'
      if (this.data.accessTokenFormat === 'opaque') {
        accessTokenFormat = 'jwt'
      }
      this.$session.set('access_token_format', accessTokenFormat)
    }
  }
}
</script>
<style>
#login {
  text-align: left;
  width: 340px;
}
#error {
  text-align: left;
}
.custom {
  float: left;
  margin: 5px 5px 5px 5px;

}
</style>
