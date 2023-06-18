<template>
  <div class="user">
    <div class="orders">
  <section class="active">
    <span class="hero-text">Aktywne</span>
    <div v-for="item in ordersActive" class="small-tile" :key="item">
      <FloatingWindow :ref="item.mainCourse" :class="{'visible': big === item.mainCourse,'invisible': big !== item.mainCourse }">
        <OrderSpecifications :id="item.orderId" :name="item.user" :course="item.mainCourse" :mode="'Gotowe'" @closed="bigWindow(item.mainCourse)"></OrderSpecifications>
      </FloatingWindow>
      <div class="fill-tile" @click="bigWindow(item.mainCourse)"><p v-if="item.user" class="spaced">Zamowienie nr {{ item.orderId }}</p>
      <span>{{ item.mainCourse }}</span></div>
    </div>
  </section>
  <section class="finalized">
    <span class="hero-text">Gotowe</span>
    <div v-for="item in ordersReady" class="small-tile" :key="item" >
      <FloatingWindow :ref="item.mainCourse" :class="{'visible': big === item.mainCourse,'invisible': big !== item.mainCourse }">
        <OrderSpecifications :id="item.orderId" :name="item.user" :course="item.mainCourse" :mode="'Wydaj'" @closed="bigWindow(item.mainCourse)"></OrderSpecifications>
      </FloatingWindow>
      <div class="fill-tile" @click="bigWindow(item.mainCourse)"><p v-if="item.user" class="spaced">Zamowienie nr {{ item.orderId }}</p>
      <span>{{ item.mainCourse }}</span></div>
    </div>
  </section>
</div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'
import FloatingWindow from '@/components/FloatingWindow.vue'
import OrderSpecifications from '@/components/OrderSpecification.vue'
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'AccountView',
  data () {
    return {
      userid: Number,
      big: ' '
    }
  },
  components: {
    FloatingWindow,
    OrderSpecifications
  },
  beforeMount () {
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
    function update () {
      axios.get('http://127.0.0.1:8000/api/orders/', {
        headers: {
          'Content-Type': 'application/json'
        }
        /* params: {
          format: 'json'
        } */
      }).then(function (response) {
        if (response.status === 200) {
          console.log(response.data)
          store.dispatch('insertOrders', response.data)
          console.log(store.state.Orders)
        }
      }, function (err) {
        console.log('err', err)
      })
    }
    update()
    const timer: ReturnType<typeof setTimeout> = setInterval(() => update(), 30000)
  },
  methods: {
    ...mapActions(['insertOrders']),
    bigWindow (id:string, key:boolean) {
      if (key) {
        this.big = ''
      } else {
        if (this.big === id) {
          this.big = ''
        } else {
          this.big = id
        }
      }
    },
    close () {
      this.big = ''
    },
    parseJwt (token:any) {
      var base64Url = token.split('.')[1]
      var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      }).join(''))

      return JSON.parse(jsonPayload)
    }
  },
  computed: {
    ordersReady () {
      function ready (order:any) {
        if (order.status === 'Gotowe') return true
      }
      console.log(store.state.Orders.filter(ready))
      return store.state.Orders.filter(ready)
    },
    ordersActive () {
      function ready (order:any) {
        if (order.status === 'Aktywne') return true
      }
      console.log(store.state.Orders.filter(ready))
      return store.state.Orders.filter(ready)
    },
    activeUser () {
      return store.state.User
    }
  }
})
</script>
<style lang="css" scoped>
p{
  margin:0;
  padding: 5px;
  position: relative;
}
.spaced{
  padding: 10px;
}
.user{
  position: relative;
  top:15%;
  z-index: 10;
}
.hero-text{
  margin: 0 auto;
  margin-bottom: 25px;
  display: block;
  position: relative;
  width: 70%;
  height: 20px;
  padding: 5px;
  padding-bottom: 10px;
  text-align: center;
  color:rgba(0, 0, 0, 1);
  font-size: 100%;
  background-color: rgba(0, 0, 0, 0.1);
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}
.small-tile{
  display: block;
  margin: 15px auto;
  box-sizing: border-box;
  box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.1);
  background:rgb(85, 85, 85);
  width:80%;
  height:10%;
  text-align: center;
  cursor: pointer;
}
.fill-tile{
  width: 100%;
  height: 100%;
}
.fill-tile:hover{
  box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.1);
  background:rgb(105, 105, 105);
}
.orders{
  display: flex;
  justify-content: space-between;
  color:white;
  width:80%;
  margin:0 auto;
}
.active{
padding: 5px;
padding-top: 0px;
background:rgba(255, 255, 255,0.5);
box-shadow: 5px 5px 10px 5px rgba(0,0,0,0.2);
width:35vw;
height:80vh;
overflow-y: scroll;
overflow: auto;
border-radius: 5px;
}
.finalized{
padding: 5px;
padding-top: 0px;
background:rgba(255, 255, 255,0.5);
box-shadow: 5px 5px 10px 5px rgba(0,0,0,0.2);
width:35vw;
height:80vh;
overflow-y: scroll;
overflow: auto;
border-radius: 5px;
}
.invisible{
  display: none;
}
/*##################################### Floating window style override ################################################*/
.blurb{
  width:50%;
  height: 70%;
  cursor: default;
  box-shadow: 0px 0px 0px 0px rgba(0,0,0,0.1);
}
</style>
