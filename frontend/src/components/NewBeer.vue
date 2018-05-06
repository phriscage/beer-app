<template>
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
</template>

<script>

export default {
  data () {
    return {
      formstate: {},
      model: {
        name: '',
        brewery: '',
        success: false
      },
      context: 'new_beer context'
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
        if (field.$name === 'brewery') {
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
</style>
