<template>
    <div class="page-loader" v-if="!isloaded">
      <div class="cubes"></div>
      <div class="cubes"></div>
      <div class="cubes"></div>
      <div class="cubes"></div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  data () {
    return {
      isloaded: false
    }
  },
  mounted () {
    this.delay(2000).then(() => {
      this.isloaded = true
    })
  },
  methods: {
    delay (time : number) {
      return new Promise(resolve => setTimeout(resolve, time))
    }
  }
})
</script>
<style>
.page-loader{
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top:0;
    left:0;
    width:100vw;
    height:100vh;
    background-color: white;
    z-index: 999;
}
.cubes{
    width: 40px;
    height:40px;
    margin-right: 10px;
    background-color: rgba(100, 100, 100, 1);
}
.cubes:nth-child(1){
    animation: first 2s infinite;
    animation-delay: 0.5s;
}
.cubes:nth-child(2){
    animation: first 2s infinite;
    animation-delay: 1s;
}
.cubes:nth-child(3){
    animation: first 2s infinite;
    animation-delay: 1.5s;
}
.cubes:nth-child(4){
    animation: first 2s infinite;
    animation-delay: 2s;
}
@keyframes first {
    40% {
      background-color: #EF6C00
    }
    100% {
        background-color: rgba(255, 255, 255, 1);
    }
}
</style>
