<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div class="choose-view">
          <h2 class="welcome-text">Witaj!</h2>
          <a @click="directToMainDishes" class="link-container">
            <legend class="clickable-button">
              <h1 class="section-title smaller">Dania główne</h1>
            </legend>
          </a>
          <a @click="directToUsers" class="link-container">
            <legend class="clickable-button">
              <h1 class="section-title smaller">Użytkownicy</h1>
            </legend>
          </a>
        </div>
      </BackPanel>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import BackPanel from '@/components/BackPanel.vue'
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
    BackPanel
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
.manager-account-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  background-color: #f5f5f5;
}

.choose-view {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 10px;
  width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333;
  text-align: center;
  margin: 0 auto;
}

.welcome-text {
  font-size: 2em;
  margin-bottom: 20px;
  color: #333;
  font-weight: normal;
}

.dishes {
  text-align: center;
}

.link-container {
  text-decoration: none;
}

.clickable-button {
  background-color: #fff;
  padding: 20px;
  border: 2px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333;
}

.clickable-button:hover {
  background-color: #e0e0e0;
}

.section-title {
  font-size: 1.5em;
  margin-bottom: 10px;
  color: #333;
  font-weight: 500;
}

</style>
