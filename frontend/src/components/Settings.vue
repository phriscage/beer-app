<template>
  <div class="container">
    <vue-form id="settings" class="ui large form warning" :state="formstate" @submit.prevent="onSubmit">
      <div class="ui clearing segment">

         <validate tag="label" class="required field">
         <span>Client ID:</span>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               required
               name="clientId"
               v-model="model.cliendId"
            />
           </div>
          <field-messages name="clientId" class="ui warning message">
            <div slot="required">Client ID is a required field</div>
            <div slot="clientId">Client ID is not valid</div>
          </field-messages>
        </validate>
        <p/>
        <validate tag="label" class="required field">
        <span>Google Client ID:</span>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               required
               name="googleClientId"
               v-model="model.googleClientId"
            />
           </div>
          <field-messages name="googleClientId" class="ui warning message">
            <div slot="required">Google Client ID is a required field</div>
            <div slot="googleClientId">Google Client ID is not valid</div>
          </field-messages>
        </validate>
        <p/>
        <validate tag="label" class="required field">
        <span>API Base URL:</span>
         <div class="ui left icon input">
           <i class="lock icon"></i>
            <input
               type="text"
               required
               name="apiBaseUrl"
               v-model="model.apiBaseUrl"
            />
           </div>
          <field-messages name="apiBaseUrl" class="ui warning message">
            <div slot="required">API Base URL is a required field</div>
            <div slot="apiBaseUrl">API Base URL is not valid</div>
          </field-messages>
        </validate>
        <p/>
        <button type="submit" class="ui fluid large blue submit button">Save</button>
      </div>
      </vue-form>
      <!--<pre>{{ formstate }}</pre>-->
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
        googleClientId: this.$shared.googleClientId
      },
      context: 'settings context'
    }
  },
  methods: {
    fieldClassName: function (field) {
      if (!field) {
        return ''
      }
      if ((field.$touched || field.$submitted) && field.$valid) {
        return 'ui message'
      }
      if ((field.$touched || field.$submitted) && field.$invalid) {
        return 'ui warning message'
      }
    },
    onSubmit: function () {
      if (this.formstate.$invalid) {
        // alert user and exit early
        console.log(this.formstate.$invalid)
      }
      console.log(this.model.clientId)
      if (this.model.clientId !== this.$shared.clientID) {
        console.log('changing ' + this.$shared.clientID)
        this.$shared.clientID = this.model.clientId
      }
    }
  }
}
</script>
<style>
#settings {
  text-align: left;
  width: 600px;
}
</style>
