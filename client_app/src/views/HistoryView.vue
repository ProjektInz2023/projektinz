<template>
  <history/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

// Components
import history from '../components/History.vue'
export default defineComponent({
  name: 'HistoryView',
  components: {
    history
  }
})
</script>
