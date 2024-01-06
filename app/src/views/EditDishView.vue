<template>
  <div class="admin-account-view">
    <div class="dishes">
      <BackPanel>
        <i class="fas fa-arrow-left back-arrow" @click="goBack"></i>
        <div class="add-dish-form">
          <h2>Edytuj danie</h2>
          <form @submit.prevent="submitDishForm">
            <label>Nazwa dania:</label>
            <input v-model="newDish.name" required />

            <label>Opis dania:</label>
            <textarea v-model="newDish.description" required></textarea>

            <label>Cena:</label>
            <input type="number" v-model="newDish.price" required />

            <label>Alergeny:</label>
            <input v-model="newDish.alergens[0].name" />

            <label>Obrazek (URL):</label>
            <input v-model="newDish.image" />
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
  name: 'AdminAccountView',
  data () {
    return {
      dishId: null as string | null,
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
    async submitDishForm () {
      if ($cookie.get('adminToken')) {
        if (await this.confirmEdition()) {
          axios
            .put(`http://127.0.0.1:8000/api/maincourses/${this.dishId}/`, this.newDish)
            .then((response) => {
              console.log('Danie dodane:', response.data)
              this.showSuccessNotification()
            })
            .catch((error) => {
              console.error('Błąd dodawania dania:', error)
            })
        }
      } else {
        this.$router.push({ name: '404' })
      }
    },
    async confirmEdition () {
      const result = await Swal.fire({
        title: 'Czy na pewno chcesz zaktualizować to danie?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Tak, zaktualizuj',
        cancelButtonText: 'Anuluj'
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
    if ($cookie.get('adminToken')) {
      this.dishId = this.$route.params.dishId as string | null
      this.fetchDishData()
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
