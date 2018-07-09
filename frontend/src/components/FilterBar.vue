// FilterBar.vue
<template>
  <div class="filter-bar ui middle padded grid">
    <div class='row'>
      <div class='five wide column'>
        <div class='ui fluid padded input'>
          <input type="text" v-model="filterText" @keyup.enter="doFilter" placeholder="name:abc or brewery:abc">
        </div>
      </div>
      <div class='one wide column'>
        <button class="ui primary button" @click="doFilter">Go</button>
      </div>
        |
      <div class='one wide column'>
         <button class="ui button" @click="resetFilter">Reset</button>
      </div>
      <div class='right floated left aligned one wide column'>
         <router-link :to="{name: 'new_beer'}" class="ui primary button">New</router-link>
      </div>
      <div class='one wide column'></div>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    data () {
      return {
        filterText: ''
      }
    },
    methods: {
      doFilter () {
        console.log('doFilter:', this.filterText)
        this.$events.fire('filter-set', this.filterText)
      },
      resetFilter () {
        this.filterText = ''
        console.log('resetFilter')
        this.$events.fire('filter-reset')
      },
      newBeer () {
        console.log('newBeer')
      }
    }
  }
</script>
