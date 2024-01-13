<template>
    <div class="container">
      <button class="btn-exit" @click="close(mode)"><i class="fa fa-times" aria-hidden="true"></i></button>
        <span class="order-num">zamowienie nr {{id}}</span>
        <p class="hero-desc">Opis</p>
        <div class="line"></div>
        <p>
            {{ course }}
        </p>
        <div class="line down"></div>
        <span>Zamawiający:</span>
        <p class="hero-text">{{ name }}</p>
        <button class="btn" v-if="mode === 'Wydaj'" @click="action('return')" style="margin-left: 0;">Cofnij Status</button>
        <button class="btn" @click="action()">{{mode}}</button>
    </div>
  </template>
<script lang="ts">
import axios from 'axios'
import store from '@/store'
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
    course: String,
    mode: String
  },
  methods: {
    action (special = '') {
      console.log(this.mode)
      if (this.mode === 'Gotowe') {
        let url = 'http://127.0.0.1:8000/api/orders/'
        console.log(this.id)
        if (this.id) {
          console.log(this.id)
          url = url.concat('patch', '/', this.id.toString(10), '/')
          axios.patch(url, { status: this.mode }).then(function (response) {
            if (response.status === 200) {
              console.log(response.data)
              window.location.reload()
            }
          }, function (err) {
            console.log('err', err)
          })
        }
      } else {
        if (this.mode === 'Wydaj') {
          let url = 'http://127.0.0.1:8000/api/orders/'
          console.log(this.id)
          if (this.id) {
            console.log(this.id)
            url = url.concat('patch', '/', this.id.toString(10), '/')
            axios.patch(url, { status: 'Zakonczone' }).then(function (response) {
              if (response.status === 200) {
                console.log(response.data)
                window.location.reload()
              }
            }, function (err) {
              console.log('err', err)
            })
          }
        }
      } if (special === 'return') {
        let url = 'http://127.0.0.1:8000/api/orders/'
        console.log(this.id)
        if (this.id) {
          console.log(this.id)
          url = url.concat('patch', '/', this.id.toString(10), '/')
          axios.patch(url, { status: 'Aktywne' }).then(function (response) {
            if (response.status === 200) {
              console.log(response.data)
              window.location.reload()
            }
          }, function (err) {
            console.log('err', err)
          })
        }
      }
    },
    close (mode = ' ') {
      if (mode === 'key') {
        this.$emit('closed', true)
      }
      this.$emit('closed', false)
    },
    escapeKeyListener: function (evt:any) {
      if (evt.keyCode === 27) {
        this.close('key')
      }
    }
  },
  created: function () {
    document.addEventListener('keyup', this.escapeKeyListener)
  },
  unmounted: function () {
    document.removeEventListener('keyup', this.escapeKeyListener)
  }
})
</script>
<style lang="css" scoped>
p{
    margin:5px;
}
p,span{
  cursor:auto ;
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
    padding: 25px;
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
    margin-top:20%;
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
    margin-left: 25px;
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
.btn-exit{
  display: block;
  margin:0px !important;
  position: absolute;
  right:15px;
  top:15px;
  z-index: 1;
  background: transparent;
  color:rgba(255, 0, 0, 0.5);
  border: 0px;
  font-size: 250%;
}
.btn-exit:hover{
  cursor: pointer;
  color:rgba(255, 0, 0, 1);
}
</style>
