<template>
  <v-main class="d-flex align-center flex-column" style="min-height: 300px;">
    <v-container class="bg-background">
      <v-row cols="10" class="d-flex align-center justify-center">
        <v-col class="justify-center" lg="6">
          <div class="text-h5 text-center">Lista zamówień</div>
            <v-list v-for="(order, index) in ordersData" :key="index">
              <v-divider v-show="index !== 0"></v-divider>
                <v-list-item-title class="text-center">{{ order.orderId }}</v-list-item-title>
                <v-list-item-subtitle class="text-center">{{ order.status }}</v-list-item-subtitle>
                <v-list-item-subtitle class="text-center">{{ formatDate(order.date) }}</v-list-item-subtitle>
            </v-list>
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
  background: rgba(255,255,255,0.6) !important;
  width: 60% !important;
  max-height: 90vh !important;
  overflow-y: auto;
  margin-top:15px;
}
</style>
