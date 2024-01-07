<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
        <div class="add-dish-form">
          <h2>Dodaj osobę</h2>
          <form @submit.prevent="submitUserForm">
            <label>Imię:</label>
            <input v-model="newPerson.name" required />

            <label>Nazwisko:</label>
            <input v-model="newPerson.surname" required />

            <label>Email:</label>
            <input v-model="newPerson.email" required />

            <label>Hasło:</label>
            <input v-model="newPerson.password" required/>

            <label>Rola:</label>
            <select v-model="newPerson.role_name" required class="wide-select">
              <option value="Admin">Admin</option>
              <option value="Cook">Kucharz</option>
              <option value="Manager">Manager</option>
              <option value="User">Użytkownik</option>
            </select>
          </form>

          <button type="submit" @click="submitUserForm">Dodaj osobę</button>
        </div>
      </BackPanel>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import BackPanel from '@/components/BackPanel.vue'
import Swal from 'sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import router from '@/router'

const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'ManagerAccountView',
  data () {
    return {
      mainCourses: [],
      newPerson: {
        email: '',
        name: '',
        surname: '',
        password: '',
        role_name: ''
      }
    }
  },
  components: {
    BackPanel
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    async submitUserForm () {
      if ($cookie.get('managerToken')) {
        if (await this.confirmAddition()) {
          axios
            .post('http://127.0.0.1:8000/api/addstaff/', this.newPerson)
            .then((response) => {
              console.log('Osoba dodana:', response.data)
              this.showSuccessNotification()
            })
            .catch((error) => {
              console.error('Błąd dodawania dania:', error)
            })
        } else {
          this.$router.push({ name: 'Add-User' })
        }
      }
    },
    async confirmAddition () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz dodać tę osobę?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Tak, dodaj',
        cancelButtonText: 'Anuluj'
      })
      return result.isConfirmed
    },
    showSuccessNotification () {
      Swal.fire({
        icon: 'success',
        title: 'Osoba została pomyślnie dodana!',
        showConfirmButton: false,
        timer: 1500
      }).then(() => {
        router.push('/users')
      })
    }
  },
  beforeMount () {
    if ($cookie.get('managerToken')) {
      $cookie.get('managerToken')
    } else {
      this.$router.push({ name: '404' })
    }
  }
})
</script>

<style lang="css" scoped>
.add-dish-form {
  background-color: grey;
  padding: 20px;
  margin-top: 20px;
  border-radius: 10px;
  width: 280px;
  color: white;
}

.add-dish-form h2 {
  color: #333;
  margin-bottom: 10px;
}

.add-dish-form label {
  display: block;
  margin-top: 10px;
}

.add-dish-form input,
.add-dish-form textarea {
  height: 25px;
  width: 200px;
}

.wide-select {
  height: 25px;
  width: 200px;
}

.add-dish-form button {
  margin-top: 10px;
}
.add-dish-form button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 16px;
}

.add-dish-form button:hover {
  background-color: #45a049;
}

.back-arrow {
  position: absolute;
  top: 5px;
  left: 5px;
  font-size: 40px;
  cursor: pointer;
  color: white;
}

.back-arrow {
  position: absolute;
  top: 5px;
  left: 5px;
  font-size: 40px;
  cursor: pointer;
  color: white;
}
</style>
