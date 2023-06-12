<template>
    <div class="container">
        <span class="order-num">zamowienie nr 0000</span>

        <p class="hero-desc">Opis</p>
        <div class="line"></div>
        <p>
            {{ course }} wraz sosem i frytkami
        </p>
        <div class="line down"></div>
        <span>Zamawiający:</span>
        <p class="hero-text">{{ name }}</p>
        <button class="btn" @click="close">Finalize</button>
    </div>
  </template>
<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'OrderSpecification',
  data: function () {
    return {
      elo: 'elo'
    }
  },
  props: {
    id: Number,
    name: String,
    course: String
  },
  methods: {
    close () {
      this.$emit('closed')
    }
  }
})
</script>
<style lang="css" scoped>
p{
    margin:5px;
}
.order-num{
    display: block;
    position: relative;
    margin-bottom: 5%;
}
.hero-text{
position: relative;
}
.hero-desc{
    font-size: 150%;
}
.container{
    width: 100%;
    text-align: center;
}
.line{
    background-color: rgba(255, 255, 255, 0.9);
    box-shadow: 0px 0px 0px 0px rgba(255, 255, 255, 1);
    border: 1px solid rgba(0,0,0,0.6);
    margin-top: 5%;
}
.down{
    margin: 0 auto;
    margin-top:5%;
    margin-bottom: 5%;
}
.btn{
    margin-top:25%;
    border-radius:0px;
    font-size:110%;
    color:rgba(255,255,255,1);
    width:200px;
    height:55px;
    background:rgba(255,103,31,1);
    border: 0px;
    overflow: hidden;
    position: relative;
    box-shadow: 0px 0px 5px 1px rgba(255,255,255,0.2);
}
.btn::before {
    content: '';
    display: block;
    position: absolute;
    background: rgba(255, 255, 255, 0.5);
    width: 60px;
    height: 100%;
    top: 0;
    filter: blur(30px);
    transform: translateX(-100px) skewX(-15deg);
  }
  .btn::after {
    content: '';
    display: block;
    position: absolute;
    background: rgba(255, 255, 255, 0.2);
    width: 30px;
    height: 100%;
    top: 0;
    filter: blur(5px);
    transform: translateX(-100px) skewX(-15deg);
  }
.btn:hover{
    transition: all 0.3s ease-in;
    /*transition: background-color 1s cubic-bezier(.77,0,.52,.87);*/
    cursor: pointer;
    color:black;
}
.btn:hover::before,.btn:hover::after{
  transform: translateX(300px) skewX(-15deg);
  transition: 0.7s;
}
</style>
