<template>
  <div>
    <div class="ui error message" v-if="error">
      <i v-on:click="onErrorClose()" class="close icon"></i>
      <div class="header">Something broke!</div>
      <div id="error"><pre>{{ errorMessage }}</pre></div>
    </div>
    <div class="ui one column stackable center aligned page grid">
    <div v-show="!id_token && !type">
      <!-- Login and Verification Segment -->
      <div id="authentication" class="ui stacked segment">
        <!-- Verify Authorization Code form -->
        <div v-show="code">
          <form id="code" class="ui large form">
            <div class="ui left aligned clearing segment">
              <b>{{ client_name }}</b>
              <div class="ui center aligned basic segment">
                <p>This app would like to access:</p>
                <div class="ui left aligned container">
                  <li v-for="(description, scope) in scopeParsed" :key="description">
                        <b>{{ scope }}</b>: {{ description }}
                  </li>
                </div>
              </div>
              <div class="ui fluid large green submit button" @click="verifyCode()">Accept</div>
              <br>
              <div class="ui fluid large yellow submit button" @click="cancelCode()">Cancel</div>
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
              <br>
              <div class="ui toggle checkbox custom">
                <input id="grantType" v-on:click="onGrantTypeClick()" v-model.lazy="data.grantType" true-value="authorization_code" false-value="password" type="checkbox">
                <label for="grantType">Grant Type: <b>{{ data.grantType }}</b></label>
              </div>
            </div>
          </form>
          <!-- 3rd party Identity Provider -->
          <div class="ui center aligned clearing segment">
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
            <input id="promptType" v-on:click="onPromptTypeClick()" v-model.lazy="data.promptType" true-value="consent" false-value=none type="checkbox">
            <label for="promptType">Prompt Type: <b>{{ data.promptType }}</b></label>
          </div>
          <br>
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

  </div>
</template>

<script>
var querystring = require('querystring')
var axios = require('axios')

// OpenID Connect Basic Profile
let scopeValues = {
  // 'openid': 'Informs the Authorization Server that the Client is making an OpenID Connect request. If the openid scope value is not present, the behavior is entirely unspecified.',
  'profile': 'This scope value requests access to the End-User\'s default profile Claims, which are: name, family_name, given_name, middle_name, nickname, preferred_username, profile, picture, website, gender, birthdate, zoneinfo, locale, and updated_at.',
  'email': 'This scope value requests access to the email and email_verified Claims.',
  'address': 'This scope value requests access to the address Claim.',
  'phone': 'This scope value requests access to the phone_number and phone_number_verified Claims.',
  'offline_access': 'This scope value requests that an OAuth 2.0 Refresh Token be issued that can be used to obtain an Access Token that grants access to the End-User\'s UserInfo Endpoint even when the End-User is not present (not logged in).'
}

// generate a readable scope div
function formatScopeRequested (scopeRequested) {
  let scopes = {}
  if (scopeRequested === undefined) {
    return scopes
  }
  let items = scopeRequested.split(' ')
  if (items.length > 6) {
    let message = 'Additional custom scopes is not supported.'
    console.log(message)
    return { 'custom': message }
  }
  if (items.length > 1) {
    for (var i = 0; i < items.length; i++) {
      if (scopeValues[items[i]]) {
        scopes[items[i]] = scopeValues[items[i]]
      }
    }
  }
  return scopes
}

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
        promptType: this.$session.get('prompt_type_format') || 'none',
        accessTokenFormat: this.$session.get('access_token_format') || 'opaque',
        fetchUser: true
      },
      code: this.$route.query.code,
      type: this.$route.params.type,
      client_name: this.$route.query.client_name,
      access_token: this.getFragmentValue('access_token'),
      id_token: this.getFragmentValue('id_token'),
      state: this.getFragmentValue('state'),
      response_type: this.$route.params.type,
      error: false,
      errorMessage: '',
      scopeParsed: formatScopeRequested(this.$route.query.scope)
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
    // verify the authorization code
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
    cancelCode () {
      let _this = this
      console.log('Canceling Authorization Code')
      _this.$router.push({'name': 'login'})
      _this.$router.go()
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
            scope: 'openid profile email',
            client_id: _this.$shared.clientId,
            prompt: _this.data.promptType
          })
        )
          .then(function (response) {
            console.log(response)
            if (response.data && response.data.code) {
              var query = {
                code: response.data.code,
                client_id: response.data.client_id,
                client_name: response.data.client_name,
                scope: response.data.scope,
                state: response.data.state
              }
              _this.client_name = response.data.client_name
              _this.$router.push({name: 'login', query: query})
              // _this.$router.push({name: 'login', query: {code: response.data.code}})
              // _this.$router.push('/login?code=' + response.data.code)
              _this.$router.go()
            }
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    social (type) {
      var params = {
        client_id: this.$shared.googleClientId
      }
      // can't set prompt to None if no cookie session exists
      if (this.data.promptType !== 'none') {
        params['prompt'] = this.data.promptType
      }
      this.$auth.oauth2({
        provider: type || this.type,
        rememberMe: this.data.rememberMe,
        response_type: 'token id_token',
        params: params
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
    onPromptTypeClick: function () {
      var promptType = 'consent'
      if (this.data.promptType === 'consent') {
        promptType = 'none'
      }
      this.$session.set('prompt_type_format', promptType)
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
#authentication {
  text-align: left;
  width: 340px;
}
.custom {
  float: left;
  margin: 5px 5px 5px 5px;

}
</style>
