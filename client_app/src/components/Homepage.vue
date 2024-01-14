<template>
    <v-main class="d-flex  flex-column " style="min-height: 300px;">
      <div class="bg-background" id="orderContainer" >
      <v-card class=" text-center history-card ma-3 pa-3 d-flex divider-sm"><v-card-text class="divider-sm-text">Dania Obiadowe </v-card-text></v-card>
      <v-dialog width="25%" v-for="item in menu" :key="item.name" display="inline-block" persistent  class="align-self-md-center"  >
  <template v-slot:activator="{ props }">
    <v-card v-bind="props" height="200" :elevation="8"  class="ma-3 pa-3 d-flex food-blocks">
      <v-row cols="12">
        <v-col cols="2">
      <v-img
      class="image-holder-sm"
      height="176"
      cover
      :src="require('@/assets/' + item.image +'.jpg')"
      :error="require('@/assets/' + 'kurczak' +'.jpg')"></v-img>
    </v-col>
    <v-col>
      <span class="item-name">
        {{ item.name }}
      </span>
      <div class="d-flex flex-row mb-6 specifications">
      <v-sheet  v-for="alergen in item.alergens" :key="alergen" class="ma-2 pa-2 text-orange-darken-3">{{ alergen.name }}</v-sheet>
    </div>
      <v-card-text class="text-overline-special-2">
      {{item.price}}.00zł
      </v-card-text>
    </v-col>
    </v-row>
    </v-card>
  </template>

  <template v-slot:default="{ isActive }" >
    <v-card class="justify-center mt-auto popupcard text-mobile"  :title="item.name"  :elevation="8">
      <v-card-text class="text-black">
        {{item.description}}
      </v-card-text>
      <v-img
      class="image-holder"
        height="500"
        width="576"
        cover
        :src="require('@/assets/' + item.image +'.jpg')"
        ></v-img>
        <v-divider style="margin-top: 15px;"></v-divider>
      <v-card-text class="text-black text-overline-special text-mobile">
        zawiera cechy:
      </v-card-text>
      <v-row>
      <div class="indented text-overline text-mobile-allergen" v-for="alergen in item.alergens" :key="alergen" style="display: inline-block;">
        {{ alergen.name }}
      </div>
    </v-row>
    <v-divider style="margin-top: 15px;"></v-divider>
    <v-divider style="margin-top: 25px;" ></v-divider>
      <v-card-text class="text-h5 text-overline-special-2 text-mobile">
        Cena {{item.price}}.00zł
      </v-card-text>
      <v-divider style="margin: 5px;" ></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          text="Zamknij"
          @click="isActive.value = false"
        ></v-btn>
        <form @submit="newOrder(item.mainCourseId)" action="http://127.0.0.1:8000/api/create-checkout-session/" method="POST">
      <v-btn type="submit">
        Zamów
      </v-btn>
    </form>
      </v-card-actions>
    </v-card>
  </template>
</v-dialog>
<!--######################################-->
</div>
<v-slide-y-reverse-transition>
<v-banner class="bottom-baner" :elevation="8"  v-if="orderplaced">
  <font-awesome-icon icon="fa-solid fa-check" class="confirm-icon"/>
  <v-banner-text class="confirmation-text">
      Zamówienie złożone!
    </v-banner-text>
</v-banner>
</v-slide-y-reverse-transition>
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
      userid: Number,
      orderplaced: false
    }
  },
  methods: {
    delay (time : number) {
      return new Promise(resolve => setTimeout(resolve, time))
    },
    // eslint-disable-next-line
    parseJwt (token:any) {
      const base64Url = token.split('.')[1]
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      }).join(''))

      return JSON.parse(jsonPayload)
    },
    newOrder (id: number) {
      $cookie.set('cartitem', id, 60 * 60 * 24)
      $cookie.set('cartuser', this.userid, 60 * 60 * 24)
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
.confirm-icon{
  width: 100px;
  height: 50px;
  padding:10px ;
  color: rgb(255, 255, 255,0.9);
}
.confirmation-text{
  font-size: 250%;
  padding: 10px;
}
.v-col-sm-4{
  flex:1 !important;
}
.indented{
  margin-left: 35px;
  color:rgba(239, 108, 0,1)
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
  font-weight: 400;
  line-height: 2rem;
  letter-spacing: 0.1666666667em !important;
  font-family: "Roboto", sans-serif !important;
}
.bg-background{
  background: rgba(255,255,255,0.8) !important;
  margin: 15px;
  padding-right: 25px;
  width:70% !important;
  border-radius: 15px;
}
.list-image{
  height: 100%;
  width: 100%;
}
.specifications{
  height:50px;
}
.category-text{
  position: relative;
  top:10px;
}
.custom-background{
  height: 100%;
  width:1064px;
  position: absolute;
  background: rgba(255,255,255,0.8);
  left: 305px;
  border-top-right-radius: 155px;
  border-top-left-radius: 155px;
}
.bottom-baner{
  position: fixed;
  height: 100px;
  width: 60%;
  margin: 0 auto;
  background-color: rgba(239, 108, 0,0.9);
  bottom: 10px;
  border-top-right-radius: 15px;
  border-top-left-radius: 15px;
  border-radius: 15px;
  line-height: 2rem;
  font-family: "Roboto", sans-serif !important;
}
.popupcard{
  overflow-y: scroll !important;
  width: 150%;
}
#orderContainer{
  margin-top:15px;
  height: 95vh;
}
.food-blocks {
  width: 100%;
}
@media (max-width: 1280px) {
  .bg-background{
  background: rgba(255,255,255,0.8) !important;
  margin: 0px;
  padding-right: 15px;
  width:100% !important;
  border-radius: 0px;
}
.image-holder-sm{
    height: 200px !important;
    width: 400px !important;
  }
  .popupcard{
    overflow-y: scroll !important;
    width: 500px;
    margin-left: -100px;
    margin-right: auto;
  }
}
@media (max-width: 768px) {
  .popupcard{
    overflow-y: scroll !important;
    width: 300px;
    height: 550px;
    margin-left: -100px;
    margin-right: auto;
  }
  .food-blocks {
    width: 300%;
    height: 300%;
  }
  .confirmation-text{
    font-size: 150%;
    width: 100%;
  }
  .image-holder{
    height: 200px !important;
    width: 300px !important;
  }
  .image-holder-sm{
    height: 200px !important;
    width: 200px !important;
  }
  .text-mobile{
    font-size: 15px !important;
  }
  .text-mobile-allergen{
    font-size: 10px !important;
  }
}
.divider-sm-text{
  font-size: 130%;
}
.divider-sm{
  background: rgba(255,255,255,0);
  box-shadow: 0px 25px 20px -20px rgba(0, 0, 0,0);
  width: 50%;
  margin: 0 auto !important;
  margin-top: 25px  !important;
}
</style>
