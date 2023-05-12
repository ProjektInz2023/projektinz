<template>
  <div class="about">
    <h1>Welcome {{ userid }}</h1>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
// eslint-disable-next-line
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'AccountView',
  data () {
    return {
      userid: Number
    }
  },
  mounted () {
    if ($cookie.get('token')) {
      console.log('token is present')
    } else {
      console.log('token not present')
      router.push({ name: '404' })
    }
  }
})
</script>
