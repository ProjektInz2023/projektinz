<template>
  <div class="user">
    <span class="hero-text">Welcome user</span>
    <div class="orders">
  <section class="active">
    <div v-for="item in ordersActive" class="small-tile" :key="item">
      <FloatingWindow :ref="item.mainCourse" :class="{'visible': big === item.mainCourse,'invisible': big !== item.mainCourse }">
        <OrderSpecifications :name="item.user" :course="item.mainCourse" @closed="bigWindow(item.mainCourse)"></OrderSpecifications>
      </FloatingWindow>
      <div class="fill-tile" @click="bigWindow(item.mainCourse)"><p v-if="item.user" class="spaced">{{ item.user }}</p>
      <span>{{ item.mainCourse }}</span></div>
    </div>
  </section>
  <section class="finalized">
    <div v-for="item in ordersReady" class="small-tile" :key="item" >
      <FloatingWindow :ref="item.mainCourse" :class="{'visible': big === item.mainCourse,'invisible': big !== item.mainCourse }">
        <OrderSpecifications :name="item.user" :course="item.mainCourse" @closed="bigWindow(item.mainCourse)"></OrderSpecifications>
      </FloatingWindow>
      <div class="fill-tile" @click="bigWindow(item.mainCourse)"><p v-if="item.user" class="spaced">{{ item.user }}</p>
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
      console.log('token is present')
    } else {
      console.log('token not present')
      router.push({ name: '404' })
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/api/orders/', {
      headers: {
        'Content-Type': 'application/json'
      },
      params: {
        format: 'json'
      }
    }).then(function (response) {
      if (response.status === 200) {
        store.dispatch('insertOrders', response.data)
        console.log('xd')
        console.log(store.state.Orders)
      }
    }, function (err) {
      console.log('err', err)
    })
  },
  methods: {
    ...mapActions(['insertOrders']),
    bigWindow (id:string) {
      if (this.big === id) {
        this.big = ''
      } else {
        this.big = id
      }
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
  display: block;
  position: relative;
  width: 50%;
  text-align: center;
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
background:rgba(255, 255, 255,0.5);
box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.1);
width:35vw;
height:80vh;
overflow-y: scroll;
overflow: auto;
border-radius: 5px;
}
.finalized{
padding: 5px;
background:rgba(255, 255, 255,0.5);
box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.1);
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
}
</style>
