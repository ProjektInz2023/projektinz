<template>
  <v-app>
    <v-main>
      <v-layout class="rounded rounded-md">
        <v-app-bar title="Application bar"></v-app-bar>
        <v-navigation-drawer>
          <v-list>
            <router-link v-for="item in items" :to="item.route" :key="item.route">
              <v-list-item  :title="item.title" :key="item.title"></v-list-item>
            </router-link>
          </v-list>
        </v-navigation-drawer>
        <router-view/>
      </v-layout>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',

  data () {
    return {
      items: [
        { icon: '1', title: 'Zamów', route: '/zamow' },
        { icon: '2', title: 'Historia', route: '/historia' }
      ]
    }
  }
})
</script>
