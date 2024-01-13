<template>
  <div class="manager-account-view">
    <div class="dishes">
      <BackPanel>
        <div class="edit-dish-form">
          <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
          <h1 class="section-title">Edytuj danie</h1>
          <form @submit.prevent="submitDishForm" class="edit-form">
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

          <button type="submit" @click="submitDishForm">Zapisz zmiany</button>
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
      dishId: null as string | null,
      dishPhoto: null,
      newDish: {
        name: '',
        description: '',
        price: 0,
        alergens: [{ name: '' }],
        image: '' // TODO: Change depends on firebase
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
        if (await this.confirmEdition()) {
          axios
            .put(`http://127.0.0.1:8000/api/maincourses/${this.dishId}/`, this.newDish)
            .then((response) => {
              console.log('Danie zmienione:', response.data)
              this.showSuccessNotification()
            })
            .catch((error) => {
              console.error('Błąd aktualizacji dania:', error)
              this.showErrorNotification()
            })
        }
      } else {
        this.$router.push({ name: 'Edit-Dish' })
      }
    },
    async confirmEdition () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz zaktualizować to danie?',
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
        title: 'Danie zostało pomyślnie zaktualizowane!',
        showConfirmButton: false,
        timer: 1500
      }).then(() => {
        router.push('/main-dishes')
      })
    },
    showErrorNotification () {
      Swal.fire({
        icon: 'error',
        title: 'Błąd podczas edycji dania',
        text: 'Sprawdź wszystkie pola i spróbuj ponownie',
        showConfirmButton: false,
        timer: 3000
      })
    },
    async fetchDishData () {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/maincourses/${this.dishId}`)
        const dishData = response.data

        this.newDish.name = dishData.name
        this.newDish.description = dishData.description
        this.newDish.price = dishData.price
        this.newDish.alergens[0].name = dishData.alergens[0].name
        this.newDish.image = dishData.image
      } catch (error) {
        console.error('Error fetching dish data:', error)
      }
    }
  },
  beforeMount () {
    if ($cookie.get('managerToken')) {
      this.dishId = this.$route.params.dishId as string | null
      this.fetchDishData()
    } else {
      this.$router.push({ name: '404' })
    }
  }
})
</script>

<style lang="css" scoped>
.edit-dish-form {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 10px;
  width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: #333;
  margin-top: 80px;
}

.edit-dish-form h1 {
  font-size: 1.5em;
}

.edit-dish-form label {
  display: block;
  margin-top: 10px;
}

.edit-dish-form input,
.edit-dish-form textarea {
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
.edit-dish-form textarea:focus,.edit-dish-form input:focus{
  background-color: rgba(255, 255, 255, 1);
  box-shadow: 0px 25px 20px -20px rgb(245, 131, 1);
  border-bottom: rgb(245, 131, 1) 1px solid;
}

.edit-dish-form button {
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

.edit-dish-form button:hover {
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
