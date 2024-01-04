<template>
  <div class="admin-login">
    <FloatingWindow>
      <AdminLoginForm @success="adminLogIn"></AdminLoginForm>
    </FloatingWindow>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import FloatingWindow from '@/components/FloatingWindow.vue'
import AdminLoginForm from '@/components/AdminLoginForm.vue'
import router from '@/router'
const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'AdminLoginView',
  components: {
    FloatingWindow,
    AdminLoginForm
  },
  methods: {
    adminLogIn (event: Event) {
      router.push({ name: 'AdminAccount' })
      console.log(event)
    }
  },
  mounted () {
    if ($cookie.get('adminToken')) {
      router.push({ name: 'Admin-Login' })
    } else {
      router.push({ name: 'Admin-Login' })
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
