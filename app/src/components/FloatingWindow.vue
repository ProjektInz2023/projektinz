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
<style lang="css">
.blurb{
    margin:0 auto;
    padding: 1%;
    display: flex;
    width:1100px;
    box-sizing: border-box;
    box-shadow: 0px 0px 15px 10px rgba(0,0,0,0.1);
    background:rgb(55, 55, 55);
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    height:50%;
    z-index:10;
    border-radius: 5px;
}

</style>
