<template>
  <header>
    <img src="@/assets/logo.png" alt="" class="logo-img">
    <div class="nav-right">
      <h1 class="nav-hero-text">
        System Obsługi zamówień
      </h1>
    </div>
    <div class="userSpace" v-if="logged">
      <span id="name" ref="name">{{user.name}}</span>
      <i class="fa fa-sign-out out" aria-hidden="true"  @click="LogOut"></i>
    </div>
  </header>
  <div class="bg-image"></div>
  <router-view @UserActionLogin='LogIn' />
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
import LoginForm from './components/LoginForm.vue'
import store from '@/store'
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'App',
  data () {
    return {
      logged: false as boolean,
      user: {}
    }
  },
  methods: {
    LogOut () {
      if ($cookie.get('token')) {
        $cookie.remove('token')
        this.logged = false
        // eslint-disable-next-line
        // @ts-ignore
        router.push({ name: 'Welcome' })
      }
    },
    LogIn () {
      this.logged = true
      console.log('in')
      this.user = { name: 'xd' }
      this.user = store.state.User
    }
  },
  beforeMount () {
    if ($cookie.get('token')) {
      this.logged = true
    } else {
      this.logged = false
    }
  }
})
</script>
<style lang="css">
html,body,form{
  padding:0px;
  margin:0px;
  overflow: hidden;
}
header{
  background: rgb(85, 85, 85);
  width:100vw;
  height: 55px;
  display: flex;
  z-index: 11;
  position: absolute;
  color: white;
}
#app {
  font-family:Montserrat ,Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
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
  filter: blur(8px);
  -webkit-filter: blur(8px);
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
  width:5%;
  height:100%;
  align-items: start;
}
.nav-right{
  height:100px;
  align-items: start;
  margin-left: 1%;
  width: 80%;
}
.nav-hero-text{
  font-weight: 400;
  padding: 0px;
  margin: 0px;
  font-size: 220%;
  text-align: left;
}
.userSpace{
  align-items: end;
  font-weight: 200;
  padding: 0px;
  margin: 0px;
  font-size: 120%;
  width:15%;
  height: 100%;
  text-align: center;
  padding-top:15px;
  padding-bottom:10px;
  height: 35px;
}
.out{
  margin-left: 5%;
}
.out:hover{
  cursor: pointer;
  color: red;
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
</style>
