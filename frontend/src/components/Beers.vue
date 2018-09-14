// Beers.vue
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
    </br>
    <div class="ui container">
      <filter-bar></filter-bar>
      <vuetable ref="vuetable"
        :api-url="this.$data.beersApiUrl"
        :http-options="httpOptions"
        :http-fetch="getBeerData"
        data-path="data"
        :fields="fields"
        :append-params="moreParams"
        @vuetable:load-error="handleLoadError"
        @vuetable:loaded="onTableLoaded"
      ></vuetable>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueEvents from 'vue-events'
import Vuetable from 'vuetable-2/src/components/Vuetable'
import FilterBar from './FilterBar'
import axios from 'axios'

import moment from 'moment'

Vue.use(VueEvents)
// Vue.component('custom-actions', CustomActions)
// Vue.component('my-detail-row', DetailRow)
Vue.component('filter-bar', FilterBar)

var likesColumn = {
  name: 'likes_total',
  title: 'Likes',
  titleClass: 'center aligned',
  dataClass: 'center aligned'
}

export default {
  components: {
    Vuetable,
    FilterBar
  },
  data () {
    return {
      beersApiUrl: this.$shared.beersApiBaseUrl + '/beers?likes=true',
      httpOptions: {
        headers: {
          test: 123,
          'x-email': this.$auth.user().email,
          // This will be removed once JWT auth is fixed for OPTIONS in Istio
          'x-api-key': this.$shared.clientId
        }
      },
      error: false,
      errorMessage: '',
      randomNumber: 0,
      likesColumn: likesColumn,
      fields: [
        'brewery',
        {
          name: 'name',
          title: 'Name',
          // callback: 'allcap',
          titleClass: 'center aligned',
          dataClass: 'center aligned'
        },
        {
          name: 'created_at',
          title: 'Created At',
          titleClass: 'center aligned',
          dataClass: 'center aligned',
          callback: 'formatDate|YYYY-MM-DD'
        },
        // {
          // name: 'address.line1',
          // title: 'Address 1'
        // },
        {
          name: 'style',
          title: 'Style',
          titleClass: 'center aligned',
          dataClass: 'center aligned'
        },
        {
          name: 'style',
          title: 'Badge',
          titleClass: 'center aligned',
          dataClass: 'center aligned',
          callback: 'styleLabel'
        },
        {
          name: 'price',
          titleClass: 'center aligned',
          dataClass: 'center aligned',
          callback: 'priceLabel'
          // visible: false
        },
        likesColumn
      ],
      moreParams: {}
    }
  },
  mounted () {
    this.$events.$on('filter-set', eventData => this.onFilterSet(eventData))
    this.$events.$on('filter-reset', e => this.onFilterReset())
  },
  methods: {
    // getBeerData
    getBeerData (apiUrl, httpOptions) {
      return axios.get(apiUrl, httpOptions)
    },
    // handle errors
    handleLoadError (res) {
      console.log('handleLoadError: ')
      console.log(res)
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
    // filter
    onFilterSet (filterText) {
      console.log('filter-set')
      if (filterText.indexOf(':')) {
        var filter = filterText.split(':', 2)
        this.moreParams = {}
        this.moreParams[filter[0]] = filter[1]
        if (this.$refs.vuetable) {
          Vue.nextTick(() => this.$refs.vuetable.refresh())
        }
      }
    },
    onFilterReset () {
      console.log('filter-reset')
      this.moreParams = {}
      if (this.$refs.vuetable) {
        Vue.nextTick(() => this.$refs.vuetable.refresh())
      }
    },
    onTableLoaded () {
      console.log('vuetable:loaded')
      this.toggleColumn()
    },
    // table
    // toggle the columns if the data is not visible
    toggleColumn () {
      if (this.$refs.vuetable.tableData && this.$refs.vuetable.tableData[0]) {
        var firstRow = this.$refs.vuetable.tableData[0]
        // TO-DO we can make this dynamic for all fields
        console.log('likes_total' in firstRow)
        if ('likes_total' in firstRow) {
          this.likesColumn.visible = true
        } else {
          this.likesColumn.visible = false
        }
        this.$refs.vuetable.normalizeFields()
      }
    },
    allcap (value) {
      return value.toUpperCase()
    },
    formatDate (value, fmt = 'D MMM YYYY') {
      return (value == null)
        ? ''
        : moment(value, 'YYYY-MM-DD').format(fmt)
    },
    priceLabel (value) {
      return '<span class="ui green label"><i class="large dollar icon"></i>' + value + '</span>'
    },
    styleLabel (value) {
      // return /IPA/.test(value) === true
        // ? '<span class="ui orange label"><i class="large bar icon"></i>IPA</span>'
        // : '<span class="ui brown label"><i class="large bar icon"></i>Lager</span>'
      switch (true) {
        case /ipa/i.test(value):
          return '<span class="ui orange label"><i class="large bar icon"></i>IPA</span>'
        case /ale/i.test(value):
          return '<span class="ui yellow label"><i class="large bar icon"></i>ALE</span>'
        case /lager/i.test(value):
          return '<span class="ui brown label"><i class="large bar icon"></i>Lager</span>'
        default:
          return '<span class="ui brown label"><i class="large bar icon"></i>Other</span>'
      }
    }
  }
}
</script>
<style>
pre {
  white-space: pre-wrap; /* css-3 */
  white-space: -moz-pre-wrap; /* Mozilla, since 1999 */
  white-space: -pre-wrap; /* Opera 4-6 */
  white-space: -o-pre-wrap; /* Opera 7 */
  word-wrap: break-word; /* Internet Explorer 5.5+ */
}
</style>
