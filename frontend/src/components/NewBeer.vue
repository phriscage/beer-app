<template>
  <div>
    <div class="ui grid">
     <div class="row">
       <div class="three wide column"></div>
       <div class="ten wide column">
         <div class="ui error message" v-if="error">
           <i v-on:click="onErrorClose()" class="close icon"></i>
           <div class="header">Something broke!</div>
           <div id="error"><pre>{{ errorMessage }}</pre></div>
         </div>
       </div>
      </div>
    </div>
    <div class="container">
    <vue-form id="new_beer" class="ui warning error success form" :state="formstate" @submit.prevent="onSubmit">
      <div class="ui clearing segment">

         <validate auto-label class="required field" :class="fieldClassName(formstate.name)">
         <label>Name:</label>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               name="name"
               required
               v-model.lazy="model.name"
            />
           </div>
          <field-messages name="name" show="$touched || $submitted" :class="fieldMessageClassName(formstate.name)">
            <div slot="required">Name is a required field</div>
          </field-messages>
        </validate>
        <p/>

        <validate auto-label class="field">
        <label>Brewery:</label>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               name="brewery"
               required
               v-model.lazy="model.brewery"
            />
           </div>
          <field-messages name="brewery" show="$touched || $submitted" :class="fieldMessageClassName(formstate.brewery)">
            <div slot="required">Brewery is a required to identify the beer</div>
          </field-messages>
        </validate>
        <p/>

        <button type="submit" class="ui fluid large blue submit button">Save</button>
        <div v-if="model.success" class="ui success message">
          <i v-on:click="onSuccessClose()" class="close icon"></i>
          <div class="header">Success!</div>
        </div>
      </div>
    </vue-form>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      beersApiUrl: this.$shared.beersApiBaseUrl + '/beers',
      formstate: {},
      error: false,
      errorMessage: '',
      model: {
        name: '',
        brewery: '',
        success: false
      },
      context: 'new_beer context'
    }
  },
  methods: {
    // handle errors
    handleLoadError (res) {
      console.log('handleLoadError: ')
      if (res.response && res.response.status) {
        this.errorMessage = 'HTTP Status: ' + res.response.status + '\n' +
             'Body: ' + JSON.stringify(res.response.data, null, 4)
      } else {
        this.errorMessage = res.toString()
      }
      this.error = true
    },
    onErrorClose: function () {
      this.error = !this.error
    },
    fieldClassName: function (field) {
      if (!field) {
        return ''
      }
      if ((field.$touched || field.$submitted) && field.$invalid) {
        return 'field error'
      }
    },
    fieldMessageClassName: function (field) {
      if (!field) {
        return ''
      }
      if ((field.$touched || field.$submitted) && field.$valid) {
        return 'ui success message'
      }
      if ((field.$touched || field.$submitted) && field.$invalid) {
        if (field.$name === 'brewery') {
          return 'ui warning message'
        } else {
          return 'ui error message'
        }
      }
    },
    onSubmit: function () {
      var _this = this
      if (_this.formstate.$invalid) {
        // alert user and exit early
        console.log('this.formstate.$invalid: ' + _this.formstate.$invalid)
        return ''
      }
      // only update if something changed from original
      if (_this.formstate.$dirty) {
        axios({
          method: 'post',
          url: _this.$shared.beersApiBaseUrl + '/beers',
          data: {
            name: _this.model.name,
            brewery: _this.model.brewery
          }
        })
        .then(function (response) {
          console.log(response)
          _this.model.success = true
          _this.formstate._reset()
        })
        .catch(function (error) {
          console.log(error)
          _this.handleLoadError(error)
        })
      }
    },
    onSuccessClose: function () {
      this.model.success = !this.model.success
    }
  }
}
</script>
<style>
.required-field > label::after {
  content: '*';
  color: red;
  margin-left: 0.25rem;
}
#new_beer {
  text-align: left;
  width: 600px;
}
.fade-enter-active, .fade-leave-active {
    transition: opacity .5s
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0
}
#error {
  text-align: left;
  width: 340px;
}
</style>
