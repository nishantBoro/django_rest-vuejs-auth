<template>
  <div class="downloads">
    <NavBar></NavBar>
    <div class="bod">
      <h1>Welcome to Download Hub</h1>
      <h2>Versions available:</h2>
      <h2 v-for="mod in APIData" :key="mod.id">{{mod.name}}</h2>
      <h2></h2>
    </div>
  </div>
</template>

<script>
  import NavBar from '../components/Navbar'
  import { getAPI } from '../api/axios-base'
  import { mapState } from 'vuex'
  export default {
    name: 'Downloads',
    onIdle () { // dispatch logoutUser if no activity detected
      this.$store.dispatch('logoutUser')
        .then(response => {
          this.$router.push('/login')
        })
    },
    components: {
      NavBar
    },
    computed: mapState(['APIData']), // get APIData from store.state.
    created () {
        getAPI.get('/mods/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }) // proof that your access token is still valid; if not the
        // axios getAPI response interceptor will attempt to get a new  access token from the server. check out ../api/axios-base.js getAPI instance response interceptor
          .then(response => {
            console.log('GetAPI successfully got the mods')
            this.$store.state.APIData = response.data // store the response data in store
          })
          .catch(err => { // refresh token expired or some other error status
            console.log(err)
          })
    }
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand) ;
  .downloads {
    margin: 0;
    padding: 0;
  }
  .bod {
    background-color: #606366;
    width: 100%;
    text-align: center;
    color: white;
    font-family: 'Quicksand', sans-serif;
    padding: 0;
    margin: 78px auto;
  }
  .bod h1 {
    background-color: #292b2d;
    padding: 40px 0 40px 0;
    font-size: 32px;
    margin: 0;
  }
  .bod h2 {
    margin: 0;
    padding: 10px 0 10px 0;
  }
</style>
