<template>
  <div class="user">
    <span class="hero-text">Welcome user</span>
    <div class="orders">
  <section class="active">
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
  </section>
  <section class="finalized">
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
    <div class="small-tile">
      <p>Title</p>
      <span>Descr</span>
    </div>
  </section>
</div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
import axios from 'axios'
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'AccountView',
  data () {
    return {
      userid: Number
    }
  },
  mounted () {
    if ($cookie.get('token')) {
      console.log('token is present')
    } else {
      console.log('token not present')
      // router.push({ name: '404' })
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
  box-shadow: 0px 0px 15px 10px rgba(0,0,0,0.1);
  background:rgb(85, 85, 85);
  width:80%;
  height:10%;
  text-align: center;
  padding: 5px;
  cursor: pointer;
}
.small-tile:hover{
  box-shadow: 0px 0px 15px 10px rgba(0,0,0,0.2);
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
width:30vw;
height:80vh;
overflow-y: scroll;
}
.finalized{
padding: 5px;
background:rgba(255, 255, 255,0.5);
box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.1);
width:30vw;
height:80vh;
overflow-y: scroll;
}
</style>
