<template>
  <div class="login-form">
    <NavBar></NavBar>
    <div class="lg">
      <form v-on:submit.prevent="loginUser">
        <label for="user">Username</label>
        <input type="text" name="username" id="user" v-model="username">
        <label for="pass">Password</label>
        <input type="password" name="password" id="pass" v-model="password">
        <button type="submit">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
  import NavBar from '../components/Navbar'
  export default {
    name: 'login',
    components: {
      NavBar
    },
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      loginUser () {
        this.$store.dispatch('loginUser', {
          username: this.username,
          password: this.password
        })
            .then(response => {
              this.$router.push({ name: 'downloads' })
            })
        }
      }
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand) ;
  .login-form {
    margin: 0;
    padding: 0;
  }
  .lg {
    background-color: #606366;
    text-align: center;
    color: white;
    font-family: 'Quicksand', sans-serif;
    padding: 0;
    margin: 78px 0;
  }
</style>
