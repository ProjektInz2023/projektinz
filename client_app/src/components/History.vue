<template>
  <v-main class="d-flex flex-column" style="min-height: 300px;">
    <div class="bg-background"  id="orderContainer">
          <v-card class=" text-center history-card ma-3 pa-3 d-flex divider-sm"><v-card-text class="divider-sm-text" style="color:#fc8241;">Gotowe zamówienia: </v-card-text></v-card>
          <v-card class=" ma-3 pa-3 d-flex text-center history-card" v-if="!ordersData.filter(x => x.status === 'Gotowe').length"><v-card-text class="divider-sm-text">Brak Gotowych zamówień </v-card-text></v-card>
          <v-card v-for="(order, index) in ordersData.filter(x => x.status === 'Gotowe')" :key="index" height="100" :elevation="8"  class="ma-3 pa-3 d-flex text-center history-card" :ref="order.orderId" :class="order.status === 'Gotowe' ? 'active-order': 'not-active'">
            <v-card class=" text-center history-card ma-3 pa-3 d-flex divider-sm" v-if="!ordersData.filter(x => x.status === 'Gotowe').length"><v-card-text class="divider-sm-text">Brak </v-card-text></v-card>
            <v-row cols="12">
        <v-col cols="3">
    </v-col>
    <v-col>
      <span :class="order.status === 'Gotowe' ? 'item-name': 'item-name-sm'">
        Numer zamówienia {{ order.orderId }}
      </span>
      <div class="ver-line"></div>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2-top': 'text-overline-special-2-not-top'">
       Zamówiono: {{ order.mainCourse.name }}
      </v-card-text>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2': 'text-overline-special-2-not'">
        Status zamówienia: {{ order.status }}
      </v-card-text>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2': 'text-overline-special-2-not'">
        Data: {{ formatDate(order.date) }}
      </v-card-text>
    </v-col>
    <v-col cols="3"></v-col>
    </v-row>
    </v-card>
    <v-card class=" text-center history-card ma-3 pa-3 d-flex divider-sm"><v-card-text class="divider-sm-text"> Oczekujące zamówienia: </v-card-text></v-card>
    <v-card class=" ma-3 pa-3 d-flex text-center history-card" v-if="!ordersData.filter(z => z.status === 'Aktywne').length"><v-card-text class="divider-sm-text">Brak aktywnych zamówień </v-card-text></v-card>
    <v-card v-for="(order, index) in ordersData.filter(z => z.status === 'Aktywne')" :key="index" height="100" :elevation="8"  class="ma-3 pa-3 d-flex text-center " :ref="order.orderId" :class="order.status === 'Gotowe' ? 'active-order': 'not-active'">
      <v-row cols="12">
        <v-col cols="3">
    </v-col>
    <v-col>
      <span :class="order.status === 'Gotowe' ? 'item-name': 'item-name-sm'">
        Numer zamówienia {{ order.orderId }}
      </span>
      <div class="ver-line"></div>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2-top': 'text-overline-special-2-not-top'">
       Zamówiono: {{ order.mainCourse.name }}
      </v-card-text>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2': 'text-overline-special-2-not'">
        Status zamówienia: {{ order.status }}
      </v-card-text>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2': 'text-overline-special-2-not'">
        Data: {{ formatDate(order.date) }}
      </v-card-text>
    </v-col>
    <v-col cols="3"></v-col>
    </v-row>
    </v-card>
    <v-card class=" text-center history-card ma-3 pa-3 d-flex divider-sm"><v-card-text class="divider-sm-text"> Historia: </v-card-text></v-card>
    <v-card class=" ma-3 pa-3 d-flex text-center history-card" v-if="!ordersData.filter(y => y.status === 'Zakonczone').length"><v-card-text class="divider-sm-text">Brak Gotowych zamówień </v-card-text></v-card>
    <v-card v-for="(order, index) in ordersData.filter(y => y.status === 'Zakonczone')" :key="index" height="100" :elevation="8"  class="ma-3 pa-3 d-flex text-center history-card" :ref="order.orderId" :class="order.status === 'Gotowe' ? 'active-order': 'not-active'">
      <v-row cols="12">
        <v-col cols="3">
    </v-col>
    <v-col>
      <span :class="order.status === 'Gotowe' ? 'item-name': 'item-name-sm'">
        Numer zamówienia {{ order.orderId }}
      </span>
      <div class="ver-line"></div>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2-top': 'text-overline-special-2-not-top'">
       Zamówiono: {{ order.mainCourse.name }}
      </v-card-text>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2': 'text-overline-special-2-not'">
        Status zamówienia: {{ order.status }}
      </v-card-text>
      <v-card-text :class="order.status === 'Gotowe' ? 'text-overline-special-2': 'text-overline-special-2-not'">
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
      dataMail: '',
      prevRoute: null,
      userid: Number,
      loading: false
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
    this.delay(1000).then(() => {
      this.loading = true
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
          console.log('error getting data')
        }
      }, function (err) {
        console.log('err', err)
      })
      this.loading = false
    })
  },
  methods: {
    delay (time : number) {
      return new Promise(resolve => setTimeout(resolve, time))
    },
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
  font-size: 100%;
  margin-top: 15px;
}
.text-overline-special-2-not{
  font-weight: 400;
  line-height: 1.5rem;
  padding: 0 !important;
}
.text-overline-special-2-top{
  font-weight: 400;
  line-height: 2rem;
  padding: 0 !important;
  font-size: 100%;
  margin-top:25px;
}
.text-overline-special-2-not-top{
  font-weight: 400;
  line-height: 1.5rem;
  padding: 0 !important;
  margin-top:10px;
}
.bg-background{
  background: rgba(255,255,255,0.8) !important;
  margin: 15px;
  width:70% !important;
  border-radius: 15px;
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
.not-active{
  height: 150px !important;
}
.item-name{
  font-size: 130%;
}
.item-name-sm{
  font-size: 100%;
}
.ver-line{
  display: block;
  width: 100%;
  height: 2px;
  margin-bottom: 10px;
  background-color: rgba(0,0,0,0.5);
}
.divider-sm-text{
  font-size: 140%;
}
.divider-sm{
  background: rgba(255,255,255,0);
  box-shadow: 0px 25px 20px -20px rgba(0, 0, 0,0);
  width: 50%;
  margin: 0 auto !important;
  margin-top: 25px  !important;
}
/* Media Query */
@media (max-width: 1280px) {
  .bg-background{
  background: rgba(255,255,255,0.8) !important;
  margin: 0px;
  min-height: 150% !important;
  padding-right: 0px;
  width:100% !important;
  border-radius: 0px;
  overflow:visible;
}
}
@media (max-width: 768px) {
  .text-mobile{
    font-size: 15px !important;
  }
  .text-mobile-allergen{
    font-size: 10px !important;
  }
  .history-card{
    height: 100px !important;
  }
  .active-order{
    height: 200px !important;
  }
  .v-col-3{
    display: none;
  }
  .v-col{
    padding-left:5px;
    padding-right: 5px;
  }
  .text-overline-special-2{
  font-weight: 400;
  line-height: 1.5rem;
  padding: 0 !important;
  font-size: 100%;
  margin-top: 10px;
}
.text-overline-special-2-not{
  font-weight: 400;
  line-height: 1rem;
  padding: 0 !important;
}
.text-overline-special-2-top{
  font-weight: 400;
  line-height: 1.5rem;
  padding: 0 !important;
  font-size: 100%;
  margin-top:15px;
}
.text-overline-special-2-not-top{
  font-weight: 400;
  line-height: 1rem;
  padding: 0 !important;
  margin-top:10px;
}

}
</style>
