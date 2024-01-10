<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div>
          <section class="users-section">
            <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
            <h1 class="section-title">Dania główne</h1>

            <div class="user-list-container">
              <ul class="user-list">
                <li v-for="mainCourse in mainCourses" :key="mainCourse.id">
                  <div class="user-container">
                    <div class="user-box">
                      <div class="user-name">{{ mainCourse.name }}</div>
                    </div>

                    <div class="action-icons">
                      <div class="fas fa-edit edit-icon" style="cursor: pointer;" @click="editDish(mainCourse.mainCourseId)"></div>
                      <div class="fas fa-trash delete-icon" style="cursor: pointer;" @click="deleteDish(mainCourse.mainCourseId)"></div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>

            <button class="add-dish-button" @click="addDish">Dodaj danie</button>
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
  name: 'ManagerAccountView',
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
      router.push('/manager-account')
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
        cancelButtonText: 'Anuluj',
        confirmButtonColor: '#d9534f'
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
    if ($cookie.get('managerToken')) {
      $cookie.get('managerToken')
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

<style scoped>

.user-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border: 1px solid #ccc;
  margin: 10px 0;
  border-radius: 5px;
  background-color: #fff;
}

.user-box {
}

.user-name {
  font-size: 1.2em;
  margin-bottom: 5px;
}

.action-icons {
  display: flex;
  gap: 10px;
}

.edit-icon,
.delete-icon {
  cursor: pointer;
  font-size: 1.2em;
  color: #333;
}

.manager-account-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.users-section {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  align-items: center;
}

.back-arrow {
  cursor: pointer;
  font-size: 1.5em;
  margin-right: 10px;
  margin-left: -550px;
}

.section-title {
  margin: 0;
  font-size: 1.5em;
}

.user-list-container {
  height: 400px;
  width: 600px;
  overflow-y: scroll;
  margin-top: 10px;
}

.user-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.user-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border: 1px solid #ccc;
  margin: 10px 0;
  border-radius: 5px;
  background-color: #fff;
}

.user-box {
  flex: 1;
  flex-direction: column;
  align-items: center;
  margin-left: 70px;
}

.user-name {
  font-size: 1.2em;
}

.action-icons {
  display: flex;
  gap: 10px;
}

.edit-icon,
.delete-icon {
  cursor: pointer;
  font-size: 1.2em;
  color: #333;
}

.add-dish-button {
  padding: 10px;
  margin-top: 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s ease;
}

.add-dish-button:hover {
  background-color: #0056b3;
}
</style>
