<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div class="edit-user-form">
          <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
          <h1 class="section-title">Edytuj osobę</h1>
          <form @submit.prevent="submitUserForm" class="edit-form">
            <label>Imię:</label>
            <input v-model="newPerson.name" required />

            <label>Nazwisko:</label>
            <input v-model="newPerson.surname" required />

            <label>Email:</label>
            <input v-model="newPerson.email" required />
          </form>

          <button type="submit" @click="submitUserForm">Zapisz zmiany</button>
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
      userEmail: null as string | null,
      newPerson: {
        email: '',
        name: '',
        surname: ''
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
        if (await this.confirmEdition()) {
          axios
            .put(`http://127.0.0.1:8000/api/edit_staff/${this.newPerson.email}/`, this.newPerson)
            .then((response) => {
              console.log('Osoba zmieniona:', response.data)
              this.showSuccessNotification()
            })
            .catch((error) => {
              console.error('Błąd edytowania osoby:', error)
            })
        }
      } else {
        this.$router.push({ name: 'Edit-User' })
      }
    },
    async confirmEdition () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz zaktualizować tę osobę?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Tak, zaktualizuj',
        cancelButtonText: 'Anuluj',
        confirmButtonColor: '#007bff'
      })
      return result.isConfirmed
    },
    showSuccessNotification () {
      Swal.fire({
        icon: 'success',
        title: 'Osoba została pomyślnie zaktualizowana!',
        showConfirmButton: false,
        timer: 1500
      }).then(() => {
        router.push('/users')
      })
    },
    async fetchDishData () {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/staff/${this.userEmail}/`)
        const personData = response.data
        console.log(personData)

        this.newPerson.email = personData.email
        this.newPerson.name = personData.name
        this.newPerson.surname = personData.surname
      } catch (error) {
        console.error('Error fetching person data:', error)
      }
    }
  },
  beforeMount () {
    if ($cookie.get('managerToken')) {
      this.userEmail = this.$route.params.userEmail as string | null
      this.fetchDishData()
    } else {
      this.$router.push({ name: '404' })
    }
  }
})
</script>

<style lang="css" scoped>
.edit-form{
  width: 100%;
  padding-bottom: 15px;
}
.edit-user-form {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 10px;
  width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333;
}

.edit-user-form h1 {
  font-size: 1.5em;
  margin-bottom: 20px;
}

.edit-user-form label {
  display: block;
  margin-top: 10px;
}

.edit-user-form input {
  font-size: 110%;
  outline: none;
  text-indent: 15px;
  width: 400px;
  height: 40px;
  border: none;
  background-color: rgba(255, 255, 255, 1);
  border-radius: 5px;
  box-shadow: 0px 25px 20px -20px rgba(0,0,0,1);
  margin: 10px;
  border-bottom: 1px transparent solid;
  transition: all 1s;
}

.edit-user-form button {
  padding: 10px;
  width: 30%;
  background-color: #EF6C00;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s ease;
  margin-top: 20px;
}

.edit-user-form button:hover {
  background-color: #E65100;
}

.back-arrow {
  cursor: pointer;
  font-size: 1.5em;
  float: left;
  margin-left: 15px;
  margin-right: -25px;
}

</style>
