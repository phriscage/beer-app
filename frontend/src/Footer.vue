<template>
  <div class="container-fluid footer">
        <router-link to="/">Home</router-link>
        |
        <router-link to="/random">Random</router-link>
        |
        <router-link to="/about">About</router-link>
        |
        <small>&copy; Copyright 2018, Chris Page</small>
  </div>
</template>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  height: 60px;
  line-height: 60px;
  width: 100%;
  background-color: #f5f5f5;
}
</style>
