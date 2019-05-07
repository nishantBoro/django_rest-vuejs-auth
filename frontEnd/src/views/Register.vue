<template>
  <div class="register-form">
    <NavBar></NavBar>
    <form @submit.prevent="registerUser">
      <label for="Name">Name</label>
      <input type="text" name="Name" id="Name" v-model="name">
      <label for="el">Email</label>
      <input type="email" name="el" id="el" v-model="email">
      <label for="ur">Username</label>
      <input type="text" name="ur" id="ur" v-model="username">
      <label for="pwr">Password</label>
      <input type="password" name="pwr" id="pwr" v-model="password">
      <label for="pass">Password Confirmation</label>
      <input type="password" name="pass" id="pass" v-model="confirm">
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
  import NavBar from '../components/Navbar'
  export default {
    name: 'register',
    components: {
      NavBar
    },
    data () {
      return {
        name: '',
        email: '',
        username: '',
        password: '',
        confirm: ''
      }
    },
    methods: {
      registerUser () {
        this.$store.dispatch('registerUser', {
          name: this.name,
          email: this.email,
          username: this.username,
          password: this.password,
          confirm: this.confirm
        }).then(() => {
          this.$router.push({ name: 'login' })
        })
      }
    }
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand) ;
  .register-form {
    background-color: #606366;
    width: 100%;
    margin: 78px auto;
    padding: 0;
    text-align: center;
  }
</style>
