<template>
  <div class="manager-account-view">
    <div class="dishes">
      <Back>
        <a @click="directToMainDishes" class="link-container">
          <legend class="clickable-button">
            <h1 class="hero-text smaller">Dania główne</h1>
          </legend>
        </a>
        <a @click="directToUsers" class="link-container">
          <legend class="clickable-button">
            <h1 class="hero-text smaller">Użytkownicy</h1>
          </legend>
        </a>
      </Back>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import Back from '@/components/BackPanel.vue'
import router from '@/router'
import store from '@/store'

const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'ManagerAccountView',
  data () {
    return {
      showContent: false,
      mainCourses: []
    }
  },
  methods: {
    directToMainDishes () {
      router.push('/main-dishes')
    },
    directToUsers () {
      router.push('/users')
    },
    parseJwt (token:any) {
      const base64Url = token.split('.')[1]
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      }).join(''))

      return JSON.parse(jsonPayload)
    }
  },
  components: {
    Back
  },
  beforeMount () {
    if ($cookie.get('managerToken')) {
      const token = $cookie.get('managerToken')
      store.dispatch('insertUser', { name: this.parseJwt(token).name, surname: this.parseJwt(token).surname })
      this.$emit('UserActionLogin')
    } else {
      this.$router.push({ name: '404' })
    }
  }
})
</script>

<style lang="css" scoped>
h1 {
  color: whitesmoke;
  margin-bottom: 70px;
  margin-top: 70px;
}

.admin-account-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.dishes {
  text-align: center;
}

.link-container {
  text-decoration: none;
}

.clickable-button {
  border: 2px solid white;
  border-radius: 5px;
  cursor: pointer;
  margin: 20px;
  width: 300px;
}

.clickable-button:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
