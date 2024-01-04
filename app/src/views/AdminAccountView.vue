<template>
  <div class="admin-account-view">
    <div class="dishes">
      <Back>
        <a @click="directToMainDishes" class="link-container">
          <legend class="clickable-button">
            <h1 class="hero-text smaller">Dania główne</h1>
          </legend>
        </a>
        <legend class="clickable-button">
          <h1 class="hero-text smaller">Użytkownicy</h1>
        </legend>
      </Back>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import Back from '@/components/BackPanel.vue'
import router from '@/router'

const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'AdminAccountView',
  data () {
    return {
      showContent: false,
      mainCourses: []
    }
  },
  methods: {
    directToMainDishes () {
      router.push('/main-dishes')
    }
  },
  components: {
    Back
  },
  beforeMount () {
    if ($cookie.get('adminToken')) {
      const token = $cookie.get('adminToken')
      axios
        .get('http://127.0.0.1:8000/api/maincourses/', {})
        .then((response) => {
          this.mainCourses = response.data
        })
        .catch((error) => {
          console.error('Error fetching main courses:', error)
        })
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
