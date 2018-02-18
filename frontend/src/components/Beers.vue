
<template>
  <div>
    <div class="ui container">
      <p>Beers page</p>
      <p>Random number from backend: {{ randomNumber }}</p>
      <button @click="getRandom">New random number</button>
    </div>
    </br>
    <div class="ui container">
      <vuetable ref="vuetable"
        api-url="http://localhost:5000/api/beers"
        data-path="data"
        :fields="fields"
      ></vuetable>
    </div>
  </div>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import moment from 'moment'
import axios from 'axios'

export default {
  components: {
    Vuetable
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
      ]
    }
  },
  methods: {
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
    },
    // random
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      this.randomNumber = this.getRandomInt(1, 100)
      // this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/random`
      axios.get(path)
      .then(response => {
        this.randomNumber = response.data.data.randomNumber
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
