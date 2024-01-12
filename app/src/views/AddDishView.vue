<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div class="add-dish-form">
          <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
          <h1 class="section-title">Dodawanie dania</h1>
          <form @submit.prevent="submitDishForm">
            <label>Nazwa dania:</label>
            <input v-model="newDish.name" required placeholder="Nazwa" />

            <label>Opis dania:</label>
            <input v-model="newDish.description" required  placeholder="Opis"/>

            <label>Cena:</label>
            <input type="number" v-model="newDish.price" required/>

            <label>Alergeny:</label>
            <input v-model="newDish.alergens[0].name" placeholder="alergen, alergen" />

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
        price: 10.0,
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
                  this.showErrorNotification()
                })
            } else {
              console.error('Image is null.')
              this.showErrorNotification()
            }
          } catch (error) {
            console.error('Error uploading image:', error)
            this.showErrorNotification() // TODO: Check how it works with working firebase
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
    },
    showErrorNotification () {
      Swal.fire({
        icon: 'error',
        title: 'Błąd podczas dodawania dania',
        text: 'Sprawdź wszystkie pola i spróbuj ponownie',
        showConfirmButton: false,
        timer: 3000
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
  width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333;
  margin-top: 80px;
}

.add-dish-form h1 {
  font-size: 1.5em;
}

.add-dish-form label {
  display: block;
  margin-top: 10px;
}

.add-dish-form input,
.add-dish-form textarea {
  font-size: 110%;
  outline: none;
  text-indent: 15px;
  width: 500px;
  height: 40px;
  border: none;
  background-color: rgba(255, 255, 255, 1);
  border-radius: 5px;
  box-shadow: 0px 25px 20px -20px rgba(0,0,0,1);
  margin: 10px;
  border-bottom: 1px transparent solid;
  transition: all 1s;
}
.add-dish-form textarea:focus,.add-dish-form input:focus{
  background-color: rgba(255, 255, 255, 1);
  box-shadow: 0px 25px 20px -20px rgb(245, 131, 1);
  border-bottom: rgb(245, 131, 1) 1px solid;
}
.add-dish-form button {
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

.add-dish-form button:hover {
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
