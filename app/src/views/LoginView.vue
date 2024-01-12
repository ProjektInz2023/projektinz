<template>
  <div class="welcome">
    <FloatingWindow>
      <LoginForm @success='LogIn($event)'></LoginForm>
    </FloatingWindow>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import FloatingWindow from '@/components/FloatingWindow.vue'
import LoginForm from '@/components/LoginForm.vue'
import router from '@/router'
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'HomeView',
  components: {
    FloatingWindow,
    LoginForm
  },
  methods: {
    LogIn (event:Event) {
      router.push({ name: 'Account' })
      console.log(event)
    }
  },
  mounted () {
    if ($cookie.get('usertoken')) {
      router.push({ name: 'Account' })
    } else {
      router.push({ name: 'Welcome' })
    }
  }
})
</script>
<style lang="css">
.welcome{
  width: 100vw;
  height: 100vh;
  display:block;
}
.redirect-link:hover>legend>h2{
text-decoration: underline;
}

</style>
