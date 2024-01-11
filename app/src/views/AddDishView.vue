<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div class="add-dish-form">
          <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
          <h1 class="section-title">Dodawanie dania</h1>
          <form @submit.prevent="submitDishForm">
            <label>Nazwa dania:</label>
            <input v-model="newDish.name" required />

            <label>Opis dania:</label>
            <input v-model="newDish.description" required />

            <label>Cena:</label>
            <input type="number" v-model="newDish.price" required />

            <label>Alergeny:</label>
            <input v-model="newDish.alergens[0].name" />

            <label>Obrazek:</label>
            <input type="file" @change="handleFileChange" />
          </form>

          <button type="submit" @click="submitDishForm">Dodaj</button>
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
import { ref, uploadBytes } from 'firebase/storage'
import { storage } from '../firebase'

const $cookie = require('vue-cookies')

export default defineComponent({
  name: 'ManagerAccountView',
  data () {
    return {
      mainCourses: [],
      dishPhoto: null,
      newDish: {
        name: '',
        description: '',
        price: 0,
        alergens: [{ name: '' }],
        image: ''
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
    handleFileChange (event: { target: { files: any[] } }) {
      const file = event.target.files[0]
      this.dishPhoto = file
    },
    async submitDishForm () {
      if ($cookie.get('managerToken')) {
        if (await this.confirmAddition()) {
          try {
            if (this.dishPhoto) {
              const file = this.dishPhoto as File

              const storageRef = ref(storage, 'folder/' + file.name)
              const snapshot = await uploadBytes(storageRef, file)
              this.newDish.image = file.name
              console.log('Image uploaded:', snapshot)

              axios.post('http://127.0.0.1:8000/api/addmaincourse/', this.newDish)
                .then((response) => {
                  console.log('Danie dodane:', response.data)
                  this.showSuccessNotification()
                })
                .catch((error) => {
                  console.error('Błąd dodawania dania:', error)
                })
            } else {
              console.error('Image is null.')
            }
          } catch (error) {
            console.error('Error uploading image:', error)
          }
        }
      }
    },
    async confirmAddition () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz dodać to danie?',
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
        title: 'Danie zostało pomyślnie dodane!',
        showConfirmButton: false,
        timer: 1500
      }).then(() => {
        router.push('/main-dishes')
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
.add-dish-form textarea {
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
