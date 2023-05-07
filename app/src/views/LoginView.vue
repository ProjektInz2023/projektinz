<template>
  <div class="welcome">
    <FloatingWindow>
      <LoginForm></LoginForm>
    </FloatingWindow>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import FloatingWindow from '@/components/FloatingWindow.vue'
import LoginForm from '@/components/LoginForm.vue'
export default defineComponent({
  name: 'HomeView',
  components: {
    FloatingWindow,
    LoginForm
  }
})
</script>
<style lang="css">
.welcome{
  width: 100vw;
  height: 100vh;
  display:block;
}
</style>
