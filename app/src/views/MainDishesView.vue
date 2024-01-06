<template>
  <div class="admin-account-view">
    <div class="dishes">
      <BackPanel>
        <div>
          <section class="main-courses-section">
            <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
            <h1 class="section-title">Dania główne</h1>
            <div style="color: white;">
              <ul class="dish-list">
                <li v-for="mainCourse in mainCourses" :key="mainCourse.id">
                  <div class="course-container">
                    <div class="main-course-box">
                      <span class="main-course-name">{{ mainCourse.name }}</span>
                    </div>
                    <div class="additional-box">
                      <a class="fas fa-trash delete-icon" @click="deleteDish(mainCourse.mainCourseId)"></a>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <button @click="addDish">Dodaj danie</button>
          </section>
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

const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'AdminAccountView',
  data () {
    return {
      mainCourses: []
    }
  },
  components: {
    BackPanel
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    addDish () {
      router.push('/add-dish')
    },
    deleteDish (dishid: any) {
      if (confirm('Czy na pewno chcesz usunąć to danie?')) {
        axios
          .delete(`http://127.0.0.1:8000/api/deletemaincourse/${dishid}`)
          .then((response) => {
            console.log(response.data)
            location.reload()
          })
          .catch((error) => {
            console.error('Error deleting dish:', error)
          })
      }
    }

  },
  beforeMount () {
    if ($cookie.get('adminToken')) {
      const token = $cookie.get('adminToken')
      axios
        .get('http://127.0.0.1:8000/api/maincourses/', {})
        .then((response) => {
          console.log(response)
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

.course-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-courses-section {
  background-color: grey;
  padding: 20px;
  margin-top: 20px;
  border-radius: 10px;
  width: 360px;
}

p, .main-course-name {
  color: white !important;
  margin: 0 !important;
  padding: 5px !important;
}

ul {
  list-style-type: none;
}

.main-course-box {
  border: 1px solid white;
  margin-bottom: 8px;
  padding: 5px;
  box-sizing: border-box;
  margin-right: 10px;
}

button {
  background-color: transparent;
  border: 1px solid white;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
}

.main-courses-section {
  margin-bottom: 30px;
}

.back-arrow {
  position: absolute;
  top: 5px;
  left: 5px;
  font-size: 40px;
  cursor: pointer;
  color: white;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #45a049;
}

.delete-icon {
  margin-left: 10px;
}

.dish-list {
  max-height: 300px;
  overflow-y: auto;
}

.section-title {
  font-size: 30px;
  margin-bottom: 10px;
  color: #333
}

.additional-box {
  margin-right: 10px;
  margin-bottom: 5px;
}

</style>
