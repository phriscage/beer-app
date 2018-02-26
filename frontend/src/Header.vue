<template>
  <div class="container-fluid header">
    <span class="home">
        <router-link :to="{name: 'home'}">Home</router-link>
    </span>
    <span class="auth" v-show="!$auth.check()">
      <router-link :to="{name: 'login'}">Login</router-link>
    </span>
    <span class="auth" v-show="$auth.check()">
      <router-link :to="{name: 'account'}">{{ $auth.user().username }}</router-link>
      |
      <a v-on:click="logout()" href="javascript:void(0);">Logout</a>
    </span>
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
.header {
  position: fixed;
  top: 0;
  height: 40px;
  line-height: 40px;
  width: 100%;
  background-color: #f5f5f5;
}
.header .home {
  float:left;
  padding-left: 10px
}
.header .auth {
  float:right;
  padding-right: 10px
}
</style>
