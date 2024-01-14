<template>
  <v-app class="text-primary">
    <page-loader></page-loader>
    <v-layout class="rounded rounded-md">
      <v-app-bar title="">
        <v-img
          class="home-btn"
          @click="home()"
          max-height="125"
          max-width="255"
          src=".\assets\logo.png"
        ></v-img>
      </v-app-bar>
      <v-navigation-drawer mobile-break-point=750 v-if="login">
        <v-list-item class="text-center" style="margin-top: 5px;">
          Witaj <span style="text-transform: capitalize;">{{user}} </span>
        </v-list-item>
        <v-divider></v-divider>
        <v-list class="custom-list">
          <v-list-item style="min-height: 35px;" v-for="item in items" :key="item.title" :to="item.route">
            <font-awesome-icon :icon="item.icon" class="special-icon"/>
            <div class="vertical-line"></div>
            <v-list-item style="display:inline-block;padding-top: 10px;">{{ item.title }}</v-list-item>
          </v-list-item>
        </v-list>
        <template v-slot:append>
          <div class="pa-4">
            <v-btn block class="bg-orange-darken-3" @click="LogOut()" style="margin-bottom:50px">
              Wyloguj się
            </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
      <router-view @loginPage="login = false" @otherPage="login = true" @UserActionLogin="LogIn()"/>
    </v-layout>
    <v-bottom-navigation class="mobile-view">

  <v-btn  v-for="item in items" :key="item.title" :to="item.route">
    <span>{{ item.title }}</span>
  </v-btn>

  <v-btn block class="bg-orange-darken-3 nav-logout" @click="LogOut()" >
              Wyloguj się
            </v-btn>
</v-bottom-navigation>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
import store from '@/store'
import PageLoader from './components/PageLoader.vue'
// eslint-disable-next-line
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'App',
  data () {
    return {
      items: [
        { icon: 'fa-regular fa-star', title: 'Zamów Posiłek', route: '/order' },
        { icon: 'fa-regular fa-bookmark', title: 'Historia Zamówień', route: '/history' }
      ],
      user: {},
      login: true as boolean
    }
  },
  components: {
    PageLoader
  },
  methods: {
    home () {
      router.push('/')
    },
    LogOut () {
      if ($cookie.get('token')) {
        $cookie.remove('token')
        if ($cookie.get('data')) {
          $cookie.remove('data')
        }
        // eslint-disable-next-line
        // @ts-ignore
        router.push('/')
        this.login = false
      }
    },
    LogIn () {
      console.log('in')
      this.user = $cookie.get('userdata')
    }
  },
  mounted () {
    if ($cookie.get('userdata')) {
      this.user = $cookie.get('userdata')
    } else {
      this.login = false
    }
    if (router.options.history.state.current === '/' || router.options.history.state.current === '') {
      this.login = false
    }
  }
})
</script>
<style>
 a{
  text-decoration: none;
 }
 .logo-img{
  width:5%;
  height:100%;
  align-items: start;
}
.v-overlay__scrim {
  opacity:0.99;
}
.v-main {
  background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.2)),
 url('./assets/bgimage.jpg') no-repeat center fixed;
 background-blend-mode: saturation;
  background-size: cover;
  overflow: scroll;
}
.special-icon{
  width:30px;
  height: 30px;
  padding-top: 10px;
  display: inline-block;
}
.center-horiz{
transform: translate(50%, 50%);
}
.vertical-line{
  display: inline-block;
  height: 30px;
  width: 3px;
  background-color: rgba(0,0,0,0.8);
  position: relative;
  top:3px;
  left:10px;
  margin-right:5px;
}
#Username{
  box-shadow: 0px 2px 2px 1px black;
}
html, body {margin: 0; height: 100%; overflow: hidden;
  font-family: "Roboto", sans-serif }
.home-btn:hover{
cursor: pointer;
}
.mobile-view{
  display: none;
}
@media (max-width: 1280px) {
  .mobile-view{
  display: flex;
}
}
 @media (max-width: 768px) {
   /* Apply custom styles for the navigation bar in mobile view */
   .custom-list {
     width: 100%; /* Collapse the navigation bar to full width */
     height: auto; /* Remove fixed height to adjust to screen size */
     padding: 20px 10px; /* Add padding to enhance readability */
   }

   /* Hide the divider line on mobile */
   .vertical-line {
     display: none;
   }

   /* Increase username font size for better visibility */
   #Username {
     font-size: 18px;
   }

   /* Remove fixed height for login page and vertical line on mobile */
   .v-navigation-drawer {
     height: auto;
   }

   .vertical-line {
     display: none;
   }
   .nav-logout{
    min-width: 50px !important;
   }
   .mobile-view{
  display: flex;
}
 }

</style>
