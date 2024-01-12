<template>
<div class="blurb">
  <slot>hello</slot>
  <div class="really-big" v-if="reallybig"></div>
</div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HelloWorld',
  props: {
    msg: String,
    reallybig: {
      type: Boolean,
      default: true
    }
  }
})
</script>
<style lang="css">
.blurb{
    margin:0 auto;
    padding: 1%;
    display: flex;
    width:40%;
    height:50%;
    box-sizing: border-box;
    box-shadow: 0px 0px 15px 10px rgba(0,0,0,0.1);
    background:rgb(105, 105, 105);
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index:10;
    border-radius: 15px;
}
.really-big{
  position: absolute;
  width: 300vw;
  height: 300vh;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.5);
  z-index: -1;
}
</style>
