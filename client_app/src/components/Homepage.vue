<template>
      <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      Zamów!
    </v-main>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HelloWorld',

  data () {
    return {
      menu: ['zamów', 'historia']
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
