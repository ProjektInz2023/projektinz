<template>
        <Login @OverlayToggle="overlaypasson()"/>
<v-slide-y-reverse-transition>
<v-banner class="bottom-baner"   v-if="checkSess">
  <font-awesome-icon icon="fa-solid fa-check" class="confirm-icon"/>
  <v-banner-text class="confirmation-text">
      Zostałeś wylogowany
  </v-banner-text>
</v-banner>
</v-slide-y-reverse-transition>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
import Login from '../components/Login.vue'
// eslint-disable-next-line
const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'LoginView',
  data () {
    return {
      checkSess: false
    }
  },
  components: {
    Login
  },
  mounted () {
    if ($cookie.get('token')) {
      router.push('/order')
    } else {
      console.log(router.options.history.state.back)
      if (!(router.options.history.state.back === '/')) {
        this.checkSess = true
        this.delay(3000).then(() => {
          this.checkSess = false
        })
      }
    }
  },
  methods: {
    overlaypasson () {
      this.$emit('OverlayChange')
    },
    delay (time : number) {
      return new Promise(resolve => setTimeout(resolve, time))
    }
  }
})
</script>

<style scoped>
.confirm-icon{
  width: 100px;
  height: 50px;
  padding:10px ;
  color: rgb(255, 255, 255,0.9);
}
.confirmation-text{
  font-size: 250%;
  padding: 10px;
}
.bottom-baner{
  position: fixed;
  height: 100px;
  width: 40%;
  margin: 0 auto !important;
  background-color: rgba(239, 108, 0,0.9);
  box-shadow: 0 0 10px 1px rgba(0,0,0,0.5);
  bottom: 10px;
  left:30%;
  right:30%;
  border-top-right-radius: 15px;
  border-top-left-radius: 15px;
  border-radius: 15px;
  line-height: 2rem;
  font-family: "Roboto", sans-serif !important;
  z-index: 999;
}
@media only screen and (max-width: 768px) {
  .bottom-baner{
  position: fixed;
  height: 110px;
  width: 100%;
  margin: 0 auto !important;
  background-color: rgba(239, 108, 0,0.9);
  box-shadow: 0 0 10px 1px rgba(0,0,0,0.5);
  bottom: -10px;
  left: 0;
  border-top-right-radius: 15px;
  border-top-left-radius: 15px;
  border-radius: 15px;
  line-height: 1.75rem;
  font-family: "Roboto", sans-serif !important;
  z-index: 999;
}
}

</style>
