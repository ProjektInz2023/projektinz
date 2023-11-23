<template>
     <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      Historia
    </v-main>
  </template>
<script lang='ts'>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'HistoryComponent',
  data () {
    return {
      items: [
        { icon: '1', title: 'Zamów', route: '/zamow' },
        { icon: '2', title: 'Historia', route: '/ustawienia' }
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
