<template>
    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
        <v-container class="fluid fill-height">
            <v-layout class="justify-center align-center" >
              <v-row cols="12" >
                <v-col sm="4"></v-col>
                  <v-col class="justify-center"  sm="4">
                   <v-card class="elevation-12" style="min-height: 400px;">
                     <v-toolbar dark color="orange-darken-3" style="margin-bottom: 5%;" >
                        <v-toolbar-title class="text-center text-h5">Zaloguj się</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text class="justify-center ">
                     <form ref="form" @submit.prevent="login()">
                            <v-text-field
                              v-model="username"
                              name="username"
                              label="Username"
                              type="text"
                              placeholder="username"
                              required
                           ></v-text-field>
                            <v-text-field
                              v-model="password"
                              name="password"
                              label="Password"
                              type="password"
                              placeholder="password"
                              required
                           ></v-text-field>
                           <div class="red--text justify-center" style="margin-bottom: 5%;"> {{errorMessage}}</div>
                           <v-row cols="12" >
                            <v-col sm="4"></v-col>
                            <v-col sm="4">
                           <v-btn type="submit" class=".mt-auto" color="orange-darken-3" width="100%" min-height="45" value="log in">{{isRegister ? stateObj.register.name : stateObj.login.name}}</v-btn>
                          </v-col>
                           <v-col sm="4"></v-col>
                          </v-row>
                      </form>
                     </v-card-text>
                  </v-card>
               </v-col>
               <v-col sm="4"></v-col>
              </v-row>
            </v-layout>
         </v-container>
    </v-main>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'
import axios from 'axios'
import router from '@/router'
// eslint-disable-next-line
const $cookie = require('vue-cookies')
axios.defaults.withCredentials = true
export default defineComponent({
  name: 'LogIn',
  data () {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      isRegister: false,
      errorMessage: '',
      stateObj: {
        register: {
          name: 'Register',
          message: 'Aleady have an Acoount? login.'
        },
        login: {
          name: 'Login',
          message: 'Register'
        }
      }
    }
  },
  mounted () {
    this.$emit('loginPage')
  },
  methods: {
    async login () {
      console.log(this.username, this.password)
      $cookie.set('data', this.username, 60 * 60 * 24)
      axios.post('http://127.0.0.1:8000/api/login/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'login'
        },
        password: this.password as string,
        email: this.username as string
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
  }
})
</script>
<style scoped>
.bg-background{
  background: rgba(255,255,255,0.9) !important;
  width: 60% !important;
  max-height: 90vh !important;
  overflow-y: auto;
  margin-top:15px;
}
#orderContainer{
  margin-top:15px;
  height: 100vh;
}
.v-col-sm-4{
  flex:1 !important;
}
.text-center{
  margin-inline-start:0px !important;
}
</style>
