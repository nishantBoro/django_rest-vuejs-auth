<template>
  <div class="downloads">
    <NavBar></NavBar>
    <div class="bod">
      <h1>Welcome to Download Hub</h1>
      <h2>Pick your game:</h2>
    </div>
  </div>
</template>

<script>
  import NavBar from '../components/Navbar'
  export default {
    name: 'Downloads',
    components: {
      NavBar
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
