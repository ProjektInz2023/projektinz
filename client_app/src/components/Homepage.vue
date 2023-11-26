<template>
    <v-main class="d-flex align-center  flex-column " style="min-height: 300px;">
      <v-container class="bg-background" id="orderContainer" >
        <v-row cols="12" >
        <v-col sm="4"></v-col>
        <v-col class="justify-center"  sm="6">
      <div class="text-h5 text-center">Dania Obiadowe</div>
      <v-dialog width="25%" v-for="item in menu" :key="item.name" display="inline-block" persistent  class="align-self-md-center">
  <template v-slot:activator="{ props }">
    <v-card v-bind="props" :text="item.name" height="200" :elevation="8"  class="ma-3 pa-3 text-center d-flex">
      <v-img
      width="100" height="200"
      cover
      :src="require('@/assets/' + item.image +'.jpg')"></v-img>
    </v-card>
  </template>

  <template v-slot:default="{ isActive }" >
    <v-card class="justify-center mt-auto"  :title="item.name"  :elevation="8">
      <v-card-text class="text-black">
        {{item.description}}
      </v-card-text>
      <v-img
        height="500"
        width="1000"
        :src="require('@/assets/' + item.image +'.jpg')"
        ></v-img>
        <v-divider style="margin-top: 15px;"></v-divider>
      <v-card-text class="text-black text-overline-special">
        zawiera cechy:
      </v-card-text>
      <v-row>
      <div class="indented text-overline" v-for="alergen in item.alergens" :key="alergen" style="display: inline-block;">
        {{ alergen }}
      </div>
    </v-row>
    <v-divider style="margin-top: 15px;"></v-divider>
    <v-divider style="margin-top: 25px;" ></v-divider>
      <v-card-text class="text-h5 text-overline-special-2">
        Cena {{item.price}}zł
      </v-card-text>
      <v-divider style="margin: 5px;" ></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
          text="Zamknij"
          @click="isActive.value = false"
        ></v-btn>
        <v-btn
          text="Zamów"
          @click="newOrder(item.mainCourseId)"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </template>
</v-dialog>
<!--######################################-->
</v-col>
<v-col sm="4"></v-col>
</v-row>
</v-container>
    </v-main>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'
import axios from 'axios'
import router from '@/router'
import store from '@/store'
// eslint-disable-next-line
const $cookie = require('vue-cookies')
export default defineComponent({
  name: 'HomePage',

  data () {
    return {
      items: [
        { icon: 'kurczak', title: 'Kurczak z ryżem', description: 'kurczak ryż' },
        { icon: 'fish', title: 'Ryba z frytkami', description: 'Ryba, frytki' },
        { icon: 'placek', title: 'Placek po Węgiersku', description: 'Placek, Węgier' }
      ],
      menu: [],
      userid: Number
    }
  },
  methods: {
    // eslint-disable-next-line
    parseJwt (token:any) {
      const base64Url = token.split('.')[1]
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      }).join(''))

      return JSON.parse(jsonPayload)
    },
    async newOrder (id: number) {
      axios.post('http://127.0.0.1:8000/api/addorder/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: $cookie.get('token')
        },
        mainCourse: id,
        user: this.userid
      }).then(function (response) {
        console.log(response)
        if (response.status === 200 && response.data.access) {
          console.log(response)
          $cookie.set('token', response.data.access, 60 * 60 * 24)
          router.push('/order')
        }
      }, function (err) {
        console.log('err', err)
      })
    }
  },
  beforeMount () {
    if ($cookie.get('data')) {
      console.log('data ok')
    } else {
      router.push({ name: 'LandingPage' })
    }
    if ($cookie.get('token')) {
      // console.log('token is present')
      const token = $cookie.get('token')
      this.userid = this.parseJwt(token).user_id
      console.log(this.userid)
      store.dispatch('insertUser', { name: this.parseJwt(token).name, surname: this.parseJwt(token).surname })
      this.$emit('UserActionLogin')
    } else {
    //  console.log('token not present')
      router.push({ name: 'LandingPage' })
    }
  },
  mounted () {
    this.$emit('otherPage')
    axios.get('http://127.0.0.1:8000/api/maincourses', {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((response) => {
      if (response.status === 200) {
        console.log(response.data)
        this.menu = response.data
        console.log(this.menu)
      } else {
        console.log('couldnt fetch menu')
      }
    }, function (err) {
      console.log('err', err)
    })
  }
})
</script>
<style scoped>
.v-col-sm-4{
  flex:1 !important;
}
.indented{
  margin-left: 35px;
  color:#EF6C00;
}
.text-overline-special{
  font-size: 0.85rem !important;
  font-weight: 500;
  line-height: 2rem;
  letter-spacing: 0.1666666667em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: uppercase !important;
}
.text-overline-special-2{
  font-size: 1.3rem !important;
  font-weight: 500;
  line-height: 2rem;
  letter-spacing: 0.1666666667em !important;
  font-family: "Roboto", sans-serif !important;
  text-transform: uppercase !important;
}
.bg-background{
  background: rgba(255,255,255,0.9) !important;
  width:70% !important;
  overflow-y: scroll;
}
#orderContainer{
  margin-top:15px;
  height: 95vh;
}
</style>
