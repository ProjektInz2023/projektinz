<template>
  <homepage/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

// Components
import Homepage from '../components/Homepage.vue'

export default defineComponent({
  name: 'HomeView',

  components: {
    Homepage
  }
})
</script>
