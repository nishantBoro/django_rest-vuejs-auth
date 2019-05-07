<template>
  <div class="nav-bar">
    <ul>
      <li v-if="accessToken==null"><router-link :to = "{ name:'register' }">REGISTER</router-link></li>
      <li v-if="accessToken==null"><router-link :to = "{ name:'login' }">LOGIN</router-link></li>
      <li v-if="accessToken!=null"><router-link :to = "{ name:'logout' }">LOGOUT</router-link></li>
      <li><router-link :to = "{ name:'downloads' }">DOWNLOADS</router-link></li>
      <li><router-link :to = "{ name:'home' }" exact>HOME</router-link></li>
    </ul>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    name: 'NavBar',
    computed: mapState(['accessToken'])
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand);
  .nav-bar {
    background-color: #2f3033;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    overflow: hidden;
  }
  .nav-bar ul {
    list-style: none;
    margin:0 14%;
    padding: 0;
    text-align: center;
    color: white;
  }
  .nav-bar ul li {
    display: inline-block;
    margin: 0 5px;
    padding: 25px;
    float: right;
  }
  .nav-bar:after {
    content: '';
    display: block;
    clear: both;
  }
  .nav-bar ul li a {
    text-decoration: none;
    font-family: 'Quicksand', sans-serif;
    font-size: 22px;
    font-weight: bold;
    color: white;
    padding: 10px;
    border-radius: 7px;
  }
  .nav-bar ul li a:hover {
    background-color: #a72a64;
  }
  .router-link-active {
    background-color: #a72a64
  }
</style>
