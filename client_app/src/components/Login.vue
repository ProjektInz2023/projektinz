<template>
    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      Login
      <font-awesome-icon icon="fa-solid fa-user-secret" />
      <v-btn
      append-icon="mdi-open-in-new"
      color="deep-purple-accent-4"
      @click="$emit('OverlayToggle')"
    >
      Launch Application
    </v-btn>
    </v-main>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LogIn',

  data () {
    return {
      menu: ['zamów', 'ustawienia']
    }
  }
})
</script>
<style scoped>

</style>
