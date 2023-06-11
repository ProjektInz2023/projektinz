<template>
<div class="blurb">
  <slot>hello</slot>
</div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HelloWorld',
  props: {
    msg: String
  }
})
</script>
<style>
.blurb{
    margin:0 auto;
    padding: 1%;
    display: flex;
    width:30%;
    box-sizing: border-box;
    box-shadow: 0px 0px 15px 10px rgba(0,0,0,0.5);
    background:rgb(85, 85, 85);
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    height:50%;
    z-index:10;
}

</style>
