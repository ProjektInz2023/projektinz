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
                    <div class="action-icons">
                      <div class="fas fa-edit edit-icon" style="cursor: pointer;" @click="editDish(mainCourse.mainCourseId)"></div>
                      <div class="fas fa-trash delete-icon" style="cursor: pointer;" @click="deleteDish(mainCourse.mainCourseId)"></div>
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
import Swal from 'sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'

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
      router.push('/admin-account')
    },
    editDish (dishId: never) {
      router.push(`/edit-dish/${dishId}`)
    },
    addDish () {
      router.push('/add-dish')
    },
    async deleteDish (dishid: never) {
      if (await this.confirmDelete()) {
        try {
          const response = await axios.delete(`http://127.0.0.1:8000/api/deletemaincourse/${dishid}`)
          console.log(response.data)
          this.showSuccessNotification()
          this.delayedReload(1500)
        } catch (error) {
          console.error('Error deleting dish:', error)
        }
      }
    },
    async confirmDelete () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz usunąć to danie?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Tak, usuń',
        cancelButtonText: 'Anuluj'
      })
      return result.isConfirmed
    },
    showSuccessNotification () {
      Swal.fire({
        icon: 'success',
        title: 'Danie zostało pomyślnie usunięte!',
        showConfirmButton: false,
        timer: 1500
      })
    },
    delayedReload (time: number) {
      setTimeout(() => {
        location.reload()
      }, time)
    }
  },
  beforeMount () {
    if ($cookie.get('adminToken')) {
      $cookie.get('adminToken')
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

.action-icons {
  margin-right: 8px;
  margin-bottom: 5px;
}

</style>
