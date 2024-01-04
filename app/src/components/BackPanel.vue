<template>
  <div class="large-blurb">
    <div class="content">
      <slot></slot>
      <div class="really-big" v-if="reallybig"></div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LargeBlurb',
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
.large-blurb{
  margin: auto;
  padding: 1%;
  display: flex;
  width:60%;
  height:75%;
  box-sizing: border-box;
  box-shadow: 0px 0px 15px 10px rgba(0,0,0,0.1);
  background: rgb(105, 105, 105);
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index:10;
  border-radius: 5px;
  justify-content: center;
  align-items: center;
}

.really-big{
  position: absolute;
  width: 300vw;
  height: 300vh;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.1);
  z-index: -1;
}
</style>
