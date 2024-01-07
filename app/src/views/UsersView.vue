<template>
  <div class="manager-account-view">
    <div class="users">
      <BackPanel>
        <div>
          <section class="users-section">
            <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
            <h1 class="section-title">Użytkownicy</h1>
            <div style="color: white;">
              <ul class="user-list">
                <li v-for="user in users" :key="user.id">
                  <div class="user-container">
                    <div class="user-box">
                      <span class="user-name">{{ user.name }}</span>
                      <span class="user-email">{{ user.email }}</span>
                    </div>
                    <div class="action-icons">
                      <div class="fas fa-edit edit-icon" style="cursor: pointer;" @click="editUser(user.email)"></div>
                      <div class="fas fa-trash delete-icon" style="cursor: pointer;" @click="deleteUser(user.email)"></div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <button @click="addUser">Dodaj osobę</button>
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
      users: []
    }
  },
  components: {
    BackPanel
  },
  methods: {
    goBack () {
      router.push('/manager-account')
    },
    editUser (userEmail: never) {
      router.push(`/edit-user/${userEmail}`)
    },
    addUser () {
      router.push('/add-user')
    },
    async deleteUser (userEmail: never) {
      if (await this.confirmDelete()) {
        try {
          const response = await axios.delete(`http://127.0.0.1:8000/api/delete_staff/${userEmail}`)
          console.log(response.data)
          this.showSuccessNotification()
          this.delayedReload(1500)
        } catch (error) {
          console.error('Error deleting user:', error)
        }
      }
    },
    async confirmDelete () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz usunąć tę osobę?',
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
        title: 'Osoba została pomyślnie usunięta!',
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
        .get('http://127.0.0.1:8000/api/staff/', {})
        .then((response) => {
          console.log(response)
          this.users = response.data
        })
        .catch((error) => {
          console.error('Error fetching users:', error)
        })
    } else {
      this.$router.push({ name: '404' })
    }
  }
})
</script>

<style lang="css" scoped>

.user-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.users-section {
  background-color: grey;
  padding: 20px;
  margin-top: 20px;
  border-radius: 10px;
  width: 360px;
}

p, .user-name {
  color: white !important;
  margin: 0 !important;
  padding: 5px !important;
}

ul {
  list-style-type: none;
}

.user-box {
  border: 1px solid white;
  margin-bottom: 8px;
  padding: 5px;
  box-sizing: border-box;
  margin-right: 10px;
  width: min-content;
  min-width: 160px;
}

.user-box {
  display: flex;
  flex-direction: column;
}

.user-email {
  font-size: 12px;
  color: lightgray;
}

button {
  background-color: transparent;
  border: 1px solid white;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
}

.users-section {
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

.user-list {
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
