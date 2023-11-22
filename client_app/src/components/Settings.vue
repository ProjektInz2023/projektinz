<template>
    <v-layout class="rounded rounded-md">
      <v-app-bar title="Application bar"></v-app-bar>
      <v-navigation-drawer>
        <v-list>
          <router-link v-for="item in items" :to="item.route" :key="item.route">
          <v-list-item  :title="item.title" :key="item.title"></v-list-item>
        </router-link>
        </v-list>
      </v-navigation-drawer>
      <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
       Ustawienia
      </v-main>
    </v-layout>
  </template>
<script lang='ts'>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'UstawieniaSettings',
  data () {
    return {
      items: [
        { icon: '1', title: 'Zamów', route: '/zamow' },
        { icon: '2', title: 'Ustawienia', route: '/ustawienia' }
      ]
    }
  }
})
</script>
<style scoped>
a{
text-decoration: none;
color: black;
}
</style>
