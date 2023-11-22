<template>
  <settings/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

// Components
import settings from '../components/Settings.vue'

export default defineComponent({
  name: 'SettingsView',

  components: {
    settings
  }
})
</script>
