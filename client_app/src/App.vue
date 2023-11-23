<template>
  <v-app class="text-primary ">
      <v-layout class="rounded rounded-md">
        <v-app-bar title="">
<v-img
max-height="125"
max-width="255"
  src=".\assets\logo.png"
></v-img></v-app-bar>
        <v-navigation-drawer
        rail
        expand-on-hover>
          <v-list>
              <v-list-item v-for="item in items" :key="item.title" :to="item.route" >
                <font-awesome-icon icon="fa-regular fa-bookmark " class="special-icon"/>
                <v-list-item :title="item.title"></v-list-item>
              </v-list-item>
          </v-list>
    </v-navigation-drawer>
    <router-view/>
  </v-layout>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'App',
  data () {
    return {
      items: [
        { icon: 'receipt', title: 'Zamów', route: '/order' },
        { icon: 'bookmark', title: 'Historia Zamówień', route: '/history' }
      ]
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
}
.special-icon{
  font-size: 25px;
  padding-top: 10px;
  float: left;
}
html, body {margin: 0; height: 100%; overflow: hidden}
</style>
