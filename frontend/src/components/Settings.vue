<template>
  <div class="container">
    <vue-form id="settings" class="ui warning error success form" :state="formstate" @submit.prevent="onSubmit">
      <div class="ui clearing segment">

         <validate auto-label class="required field" :class="fieldClassName(formstate.clientId)">
         <label>Client ID:</label>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               name="clientId"
               required
               v-model.lazy="model.clientId"
            />
           </div>
          <field-messages name="clientId" show="$touched || $submitted" :class="fieldMessageClassName(formstate.clientId)">
            <div slot="required">Client ID is a required field</div>
          </field-messages>
        </validate>
        <p/>

        <validate auto-label class="field">
        <label>Google Client ID:</label>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               name="googleClientId"
               required
               v-model.lazy="model.googleClientId"
            />
           </div>
          <field-messages name="googleClientId" show="$touched || $submitted" :class="fieldMessageClassName(formstate.googleClientId)">
            <div slot="required">Google Client ID is a required for Google Login</div>
          </field-messages>
        </validate>
        <p/>

        <validate auto-label class="required field" :class="fieldClassName(formstate.apiBaseUrl)">
        <label>API Base URL:</label>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               name="apiBaseUrl"
               required
               v-model.lazy="model.apiBaseUrl"
            />
           </div>
          <field-messages name="apiBaseUrl" show="$touched || $submitted" :class="fieldMessageClassName(formstate.apiBaseUrl)">
            <div slot="required">API Base URL is a required field</div>
            <div slot="apiBaseUrl">API Base URL is not valid</div>
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
      <pre>{{ formstate }}</pre>
  </div>
</template>

<script>

export default {
  data () {
    return {
      formstate: {},
      model: {
        apiBaseUrl: this.$shared.apiBaseUrl,
        clientId: this.$shared.clientId,
        googleClientId: this.$shared.googleClientId,
        success: false
      },
      context: 'settings context'
    }
  },
  methods: {
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
        if (field.$name === 'googleClientId') {
          return 'ui warning message'
        } else {
          return 'ui error message'
        }
      }
    },
    onSubmit: function () {
      if (this.formstate.$invalid) {
        // alert user and exit early
        console.log('this.formstate.$invalid: ' + this.formstate.$invalid)
        return ''
      }
      // only update if something changed from original
      if (this.formstate.$dirty) {
        this.$shared.clientId = this.model.clientId
        this.$shared.googleClientId = this.model.googleClientId
        this.$shared.apiBaseUrl = this.model.apiBaseUrl
        this.$session.set('shared', this.$shared)
        this.model.success = true
        this.formstate._reset()
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
#settings {
  text-align: left;
  width: 600px;
}
.fade-enter-active, .fade-leave-active {
    transition: opacity .5s
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0
}
</style>
