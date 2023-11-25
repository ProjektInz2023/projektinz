<template>
  <div>
    <div style="height:10vh"></div>
      <v-card-title class="text-h6 text-md-h5 text-lg-h4">404 - Page Not Found</v-card-title>
      <v-card-text>
        This page no longer exists or was moved to another location.
      </v-card-text>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: '404-notfound',
  mounted () {
    this.$emit('loginPage')
  }

})
</script>
<style scoped>
h1{
  position: relative;
  top:100px;
  margin:0 auto;
}
</style>
