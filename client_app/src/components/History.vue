<template>
  <v-main class="d-flex flex-column" style="min-height: 300px;">
    <div class="bg-background"  id="orderContainer">
      <div class="custom-background"></div>
          <div class="text-h5 text-center category-text">Historia Zamówień</div>
              <v-card v-for="(order, index) in ordersData.slice().reverse()" :key="index" height="100" :elevation="8"  class="ma-3 pa-3 d-flex text-center history-card" :ref="order.orderId" :class="order.status === 'Aktywne' ? 'active-order': 'not-active'">
      <v-row cols="12">
        <v-col cols="3">
    </v-col>
    <v-col>
      <span class="item-name">
        Numer zamówienia {{ order.orderId }}
      </span>
      <v-card-text class="text-overline-special-2">
        Status zamówienia: {{ order.status }}
      </v-card-text>
      <v-card-text class="text-overline-special-2">
        Data: {{ formatDate(order.date) }}
      </v-card-text>
    </v-col>
    <v-col cols="3"></v-col>
    </v-row>
    </v-card>

    </div>
  </v-main>
</template>
<script lang='ts'>
import { defineComponent } from 'vue'
import axios from 'axios'
import router from '@/router'
import store from '@/store'
// eslint-disable-next-line
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'HistoryComponent',
  data () {
    return {
      ordersData: [],
      dataMail: ''
    }
  },
  beforeMount () {
    if ($cookie.get('data')) {
      this.dataMail = $cookie.get('data')
    } else {
      router.push({ name: 'LandingPage' })
    }
    if ($cookie.get('token')) {
      // console.log('token is present')
      const token = $cookie.get('token')
      store.dispatch('insertUser', { name: this.parseJwt(token).name, surname: this.parseJwt(token).surname })
      this.$emit('UserActionLogin')
    } else {
    //  console.log('token not present')
      router.push({ name: '404' })
    }
  },
  mounted () {
    axios.get(`http://127.0.0.1:8000/api/orders/${this.dataMail}/`, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'login'
      }
    }).then((response) => {
      if (response.status === 200) {
        console.log(response)
        this.ordersData = response.data
      } else {
        console.log('aaaaa')
      }
    }, function (err) {
      console.log('err', err)
    })
  },
  methods: {
    formatDate (date: string | number | Date) {
      const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' }
      return new Date(date).toLocaleDateString('pl-PL', options)
    },
    // eslint-disable-next-line
    parseJwt (token:any) {
      const base64Url = token.split('.')[1]
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      }).join(''))

      return JSON.parse(jsonPayload)
    }
  }
})
</script>
<style scoped>
.text-overline-special-2{
  font-weight: 400;
  line-height: 2rem;
  padding: 0 !important;
}
.bg-background{
  background: rgba(255,255,255,0) !important;
  width:70% !important;
}
.custom-background{
  height: 100%;
  width:1064px;
  position: absolute;
  background: rgba(255,255,255,0.8);
  left: 305px;
  border-top-right-radius: 155px;
  border-top-left-radius: 155px;
}
.category-text{
  position: relative;
  top:10px;
}

#orderContainer{
  padding-top:15px;
  height: 95vh;
}
.active-order{
  height: 300px !important;
}
</style>
