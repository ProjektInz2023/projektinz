<template>
  <v-main class="d-flex align-center flex-column" style="min-height: 300px;">
    <v-container class="bg-background">
      <v-row cols="10" class="d-flex align-center justify-center">
        <v-col class="justify-center text-center" lg="6">
          <div class="text-h5 mb-4">Lista zamówień</div>
          <v-card v-for="(order, index) in ordersData" :key="index" class="mb-4">
            <v-card-title class="headline">{{ order.orderId }}</v-card-title>
            <v-card-subtitle>{{ order.status }}</v-card-subtitle>
            <v-card-text>{{ formatDate(order.date) }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
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
      items: [
        { icon: '1', title: 'Zamów', route: '/zamow' },
        { icon: '2', title: 'Historia', route: '/historia' }
      ],
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
.bg-background{
  background: rgba(255,255,255,0.9) !important;
  width: 70% !important;
  height: 95vh !important;
  overflow-y: auto;
  margin-top:15px;
}
</style>
