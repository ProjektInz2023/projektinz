<template>
        <Login @OverlayToggle="overlaypasson()"/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
// Components
import Login from '../components/Login.vue'
export default defineComponent({
  name: 'LoginView',
  components: {
    Login
  },
  data () {
    return {}
  },
  methods: {
    overlaypasson () {
      this.$emit('OverlayChange')
    }
  }
})
</script>
