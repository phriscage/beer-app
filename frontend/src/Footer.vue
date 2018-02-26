<template>
  <div class="container-fluid footer">
        <router-link :to="{name: 'home'}">Home</router-link>
        |
        <router-link :to="{name: 'random'}">Random</router-link>
        |
        <router-link :to="{name: 'beers'}">Beers</router-link>
        |
        <small>&copy; Copyright 2018, Chris Page</small>
        |
        <router-link :to="{name: 'about'}">About</router-link>
  </div>
</template>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  height: 40px;
  line-height: 40px;
  width: 100%;
  background-color: #f5f5f5;
}
</style>
