<template>
  <div>
    <h2>Lista zamówień:</h2>
    <ul>
      <li v-for="(order, index) in ordersData" :key="index">
        {{ order.orderId }} - {{ order.status }} - {{ formatDate(order.date) }}
      </li>
    </ul>
  </div>
</template>
<script lang='ts'>
import { defineComponent } from 'vue'
import axios from 'axios'
export default defineComponent({
  name: 'UstawieniaSettings',
  data () {
    return {
      items: [
        { icon: '1', title: 'Zamów', route: '/zamow' },
        { icon: '2', title: 'Historia', route: '/historia' }
      ],
      ordersData: []
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/api/orders/user@user.pl/', {
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
    }
  }
})
</script>
<style scoped>
a{
text-decoration: none;
color: black;
}
</style>
