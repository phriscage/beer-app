<template>
  <div class="ui fixed menu beer-header">
    <router-link :to="{name: 'home'}" class="item logo">
      <img class="logo" src="https://apigee.com/api-management/ui/images/apigee-logo.svg">
    </router-link>
    <router-link :to="{name: 'beers'}" class="item"><i class="beer icon"></i> Beers</router-link>
    <div class="ui simple dropdown item">More<i class="dropdown icon"></i>
      <div class="menu">
        <router-link :to="{name: 'random'}" class="item">Random</router-link>
        <!--<a class="item" href="#">Link Item</a>
        <div class="divider"></div>
        <div class="header">Header Item</div>
        <div class="item">
          <i class="dropdown icon"></i>
           Sub Menu
           <div class="menu">
             <a class="item" href="#">Link Item</a>
             <a class="item" href="#">Link Item</a>
           </div>
         </div>
        <a class="item" href="#">Link Item</a>-->
      </div>
    </div>
    <div class="right menu">
      <!--<a class="item"><i class="archive icon"></i></a>-->
      <router-link v-show="!$auth.check()" :to="{name: 'login'}" class="item">Login <i class="user icon"></i></router-link>
      <div v-show="$auth.check()" class="ui simple dropdown item">{{ $auth.user().username }}<i class="dropdown icon"></i>
        <div class="menu">
          <router-link :to="{name: 'account'}" class="item">Account <i class="address book icon"></i></router-link>
          <a class="item" v-on:click="logout()" href="javascript:void(0);">Logout <i class="power off icon"></i></a>
        </div>
      </div>
      <router-link :to="{name: 'settings'}" class="item"><i class="bars icon"></i></router-link>
      <router-link :to="{name: 'about'}" class="item"><i class="info icon"></i></router-link>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      context: 'header context'
    }
  },
  methods: {
    logout () {
      this.$auth.logout({
        success () {
          console.log('success ' + this.context)
          this.$session.clear()
          this.$session.set('shared', this.$shared)
        },
        error () {
          console.log('error ' + this.context)
        }
      })
    }
  }
}
</script>
<style scoped>
.beer-header {
  height: 40px;
  line-height: 40px;
  background-color: #f5f5f5;
}
</style>
