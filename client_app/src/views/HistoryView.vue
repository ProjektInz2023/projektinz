<template>
  <history/>
  <v-slide-y-reverse-transition>
<v-banner class="bottom-baner"   v-if="orderplaced">
  <font-awesome-icon icon="fa-solid fa-check" class="confirm-icon"/>
  <v-banner-text class="confirmation-text">
      Zamówienie złożone!
  </v-banner-text>
</v-banner>
</v-slide-y-reverse-transition>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

// Components
import history from '../components/History.vue'
import router from '@/router'
import axios from 'axios'
// eslint-disable-next-line
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'HistoryView',
  data () {
    return {
      orderplaced: false
    }
  },
  components: {
    history
  },
  mounted () {
    if ($cookie.get('cartitem')) {
      if ($cookie.get('cartuser')) {
        console.log(router.options.history.state.back)
        if (router.options.history.state.back === '/success') {
          this.newOrder()
          this.orderplaced = true
          this.delay(3000).then(() => {
            this.orderplaced = false
          })
        }
      }
    }
  },
  methods: {
    delay (time : number) {
      return new Promise(resolve => setTimeout(resolve, time))
    },
    newOrder () {
      if ($cookie.get('cartitem')) {
        if ($cookie.get('cartuser')) {
          axios.post('http://127.0.0.1:8000/api/addorder/', {
            headers: {
              'Content-Type': 'application/json',
              Authorization: $cookie.get('token')
            },
            mainCourse: $cookie.get('cartitem'),
            user: $cookie.get('cartuser')
          }).then(function (response) {
            console.log(response)
            console.log(response)
            $cookie.remove('cartitem')
            $cookie.remove('cartuser')
          }, function (err) {
            console.log('err', err)
          })
        }
      }
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
  width: 100%;
  margin: 0 auto;
  background-color: rgba(239, 108, 0,0.9);
  bottom: 10px;
  border-top-right-radius: 15px;
  border-top-left-radius: 15px;
  border-radius: 15px;
  line-height: 2rem;
  font-family: "Roboto", sans-serif !important;
  z-index: 999;
}
</style>
