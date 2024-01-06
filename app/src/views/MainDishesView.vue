<template>
  <div class="admin-account-view">
    <div class="dishes">
      <BackPanel>
        <div>
          <section class="main-courses-section">
            <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
            <div style="color: white;">
              <ul>
                <li v-for="mainCourse in mainCourses" :key="mainCourse.id">
                  <div class="main-course-box">
                    <span class="main-course-name">{{ mainCourse.name }}</span>
                    <i class="fas fa-trash delete-icon" @click="deleteDish(mainCourse.mainCourseId)"></i>
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
      console.log('dishid before deleteDish:', dishid)

      if (confirm('Czy na pewno chcesz usunąć to danie?')) {
        axios
          .delete(`http://127.0.0.1:8000/api/deletemaincourse/${dishid}`)
          .then((response) => {
            console.log(response.data)
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

.main-courses-section {
  margin-bottom: 20px;
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
  background-color: transparent;
  border: 1px solid white;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
  margin-top: 10px;
}

</style>
