<template>
    <PageLoader/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PageLoader from '../components/PageLoader.vue'
import router from '@/router'
export default defineComponent({
  name: 'HomeView',
  components: {
    PageLoader
  },
  beforeMount () {
    router.push('/history')
  }
})
</script>
