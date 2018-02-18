// Beers.vue
<template>
  <div>
    <div class="ui container">
    </div>
    </br>
    <div class="ui container">
      <filter-bar></filter-bar>
      <vuetable ref="vuetable"
        api-url="http://localhost:5000/api/beers"
        data-path="data"
        :fields="fields"
        :append-params="moreParams"
      ></vuetable>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueEvents from 'vue-events'
import Vuetable from 'vuetable-2/src/components/Vuetable'
import FilterBar from './FilterBar'

import moment from 'moment'

Vue.use(VueEvents)
// Vue.component('custom-actions', CustomActions)
// Vue.component('my-detail-row', DetailRow)
Vue.component('filter-bar', FilterBar)

export default {
  components: {
    Vuetable,
    FilterBar
  },
  data () {
    return {
      randomNumber: 0,
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
        }
      ],
      moreParams: {}
    }
  },
  mounted () {
    this.$events.$on('filter-set', eventData => this.onFilterSet(eventData))
    this.$events.$on('filter-reset', e => this.onFilterReset())
  },
  methods: {
    // filter
    onFilterSet (filterText) {
      console.log('filter-set', filterText)
      var filter = filterText.split(':', 2)
      // this.moreParams = {}
      this.moreParams[filter[0]] = filter[1]
      Vue.nextTick(() => this.$refs.vuetable.refresh())
    },
    onFilterReset () {
      console.log('filter-reset')
      this.moreParams = {}
      Vue.nextTick(() => this.$refs.vuetable.refresh())
    },
    // table
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
