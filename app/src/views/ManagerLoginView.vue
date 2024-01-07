<template>
  <div class="manager-login">
    <FloatingWindow>
      <AdminLoginForm @success="managerLogIn"></AdminLoginForm>
    </FloatingWindow>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import FloatingWindow from '@/components/FloatingWindow.vue'
import AdminLoginForm from '@/components/ManagerLoginForm.vue'
import router from '@/router'
const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'ManagerLoginView',
  components: {
    FloatingWindow,
    AdminLoginForm
  },
  methods: {
    managerLogIn (event: Event) {
      router.push({ name: 'ManagerAccount' })
      console.log(event)
    }
  },
  mounted () {
    if ($cookie.get('managerToken')) {
      router.push({ name: 'Manager-Account' })
    } else {
      router.push({ name: 'Manager-Login' })
    }
  }
})
</script>

<style lang="css">
.admin-login {
  width: 100vw;
  height: 100vh;
  display: block;
}
</style>
