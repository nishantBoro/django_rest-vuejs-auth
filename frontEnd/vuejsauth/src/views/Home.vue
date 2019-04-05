<template>
  <div class="home">
    <NavBar></NavBar>
    <div class="bod">
      <h1>Welcome to Hardcore Mods</h1>
      <h2>Wo are we?</h2>
      <h3>We specialise in building free game mods for ETS2 and ATS to make your gaming experience fun!</h3>
      <h2>What mods have we built so far?</h2>
      <h3>Wanna help us in any way?. We would love to have extra additions to our team. Send us a message and we will get back to you soon</h3>
    </div>
  </div>
</template>

<script>
  import NavBar from '../components/Navbar'
  export default {
    name: 'Home',
    components: {
      NavBar
    }
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand) ;
  .home {
    margin: 0;
    padding: 0;
  }
  .bod {
    background-color: #606366;
    text-align: center;
    color: white;
    font-family: 'Quicksand', sans-serif;
    padding: 0;
    margin: 78px 0;
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
  .bod h3 {
    margin: 20px;
  }

</style>
