<template>
  <div class="admin-account-view">
    <div class="dishes">
      <Back>
        <div style="display: flex; flex-direction: column; align-items: center;">
          <h2 @click="toggleMainCourses" class="main-courses-caption">Main Courses</h2>
          <div style="color: white;">
            <ul v-if="showContent">
              <li v-for="mainCourse in mainCourses" :key="mainCourse.id">
                <div class="main-course-box">
                  <span class="main-course-name">{{ mainCourse.name }}</span>
                  <ul>
                    <li v-for="dish in mainCourse.dishes" :key="dish.id">
                      <div class="dish-box">
                        <span class="dish-name">{{ dish.name }}</span>
                      </div>
                    </li>
                  </ul>
                </div>
              </li>
            </ul>
            <button @click="addDish" style="color: white;">Add Dish</button>
          </div>
        </div>
      </Back>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import Back from '@/components/Back.vue'

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
    toggleMainCourses () {
      this.showContent = !this.showContent
    },
    addDish () {
      // Add logic to handle adding a dish
      console.log('Dish added!')
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
p, .main-course-name, .dish-name {
  color: white !important;
  margin: 0 !important;
  padding: 5px !important;
  position: relative !important;
}

ul {
  list-style-type: none;
}

.main-courses-caption {
  color: white;
  width: 150px; /* Set a fixed width to prevent expansion */
  cursor: pointer;
}

.main-course-box, .dish-box {
  border: 1px solid white;
  margin-bottom: 5px;
  padding: 5px;
  box-sizing: border-box;
}

button {
  background-color: transparent;
  border: 1px solid white;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
