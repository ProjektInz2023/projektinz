<template>
  <header>
    <img src="@/assets/logo.png" alt="" class="logo-img">
    <div class="nav-right">
      <h1 class="nav-hero-text">
        System Obsługi zamówień
      </h1>
    </div>
  </header>
  <div class="bg-image"></div>
  <router-view/>
</template>
<style lang="css">
html,body,form{
  padding:0px;
  margin:0px;
  scroll-behavior: smooth;
}
header{
  background: rgb(85, 85, 85);
  width:100vw;
  height: 4%;
  display: flex;
  z-index: 11;
  position: absolute;
  color: white;
}
#app {
  font-family:Montserrat ,Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-size: 120%;
  width:100vw;
  height:100vh;
  z-index:auto;
}
.bg-image{
  background-image:url("@/assets/bgimage.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  filter: blur(20px);
  -webkit-filter: blur(20px);
  z-index:1;
   width:100vw;
  height:100vh;
  position: absolute;
}
router-view{
  z-index:2;
}
.center{
  margin:0 auto;
}
.center-horiz{
transform: translate(50%, 50%);
}
.logo-img{
  width:9vw;
  height:100%;
  align-items: start;
  z-index: 11;
}
.nav-right{
  height:100px;
  align-items: start;
  margin-left: 1vw;
  width:93vw;
}
.nav-hero-text{
  font-weight: 400;
  padding: 0px;
  margin: 0px;
  font-size: 150%
}
.line{
  display: block;
  width:80%;
  margin:0 auto;
  margin-top: 0%;
  margin-bottom: 5%;
  height:2px;
  background-color: rgba(255,103,31,1);
  box-shadow: 0px 0px 70px 2px rgba(255,103,31,1);
}
@media screen and (min-width:900px) {
  .nav-hero-text{
  font-size: 200%
}
header{
  height: 5%;
}
}
@media screen and (min-width:1400px) {
  .logo-img{
  width:6vw;
  }
}
@media screen and (min-width:2400px) {
  .logo-img{
  width:7vw;
  }
  header{
  height: 7%;
}
.nav-hero-text{
  font-size: 3.5em
}
}
</style>
