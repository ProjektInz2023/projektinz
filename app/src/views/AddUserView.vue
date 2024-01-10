<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div class="add-dish-form">
          <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
          <h1 class="section-title">Dodaj osobę</h1>
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
          <button type="submit" @click="submitUserForm">Dodaj</button>
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
              console.error('Błąd dodawania osoby:', error)
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
        cancelButtonText: 'Anuluj',
        confirmButtonColor: '#007bff'
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
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 10px;
  width: 600px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333;
}

.add-dish-form h1 {
  font-size: 1.5em;
  margin-bottom: 20px;
}

.add-dish-form label {
  display: block;
  margin-top: 10px;
}

.add-dish-form input,
.add-dish-form select {
  height: 35px;
  width: 300px;
}

.add-dish-form button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s ease;
  margin-top: 20px;
}

.add-dish-form button:hover {
  background-color: #0056b3;
}

.back-arrow {
  cursor: pointer;
  font-size: 1.5em;
  margin-right: 10px;
  margin-left: -550px;
}
</style>
