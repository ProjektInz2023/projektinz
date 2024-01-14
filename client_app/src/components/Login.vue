<template>
  <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
    <v-container class="fluid fill-height">
      <v-layout class="justify-center align-center" >
        <v-row cols="12" >
          <v-col sm="4"></v-col>
          <v-col class="justify-center"  sm="4">
            <v-card class="elevation-12 login-blurb" style="min-height: 400px;">
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
                    <v-col sm="6" class="login-form">
                      <v-btn id="submit-btn" type="submit" class=".mt-auto" color="orange-darken-3" width="100%" min-height="45" value="log in">{{isRegister ? stateObj.register.name : stateObj.login.name}}</v-btn>
                    </v-col>
                    <v-col sm="4"></v-col>
                  </v-row>
                </form>
                <p v-if="loginError" class="error-message">Błędne dane logowania. Spróbuj ponownie.</p>
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
import store from '@/store'
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
      },
      loginError: false
    }
  },
  mounted () {
    this.$emit('loginPage')
  },
  methods: {
    async login () {
      console.log(this.username, this.password)
      $cookie.set('data', this.username, 60 * 60 * 24)
      axios.post('https://34.118.43.161:8080/api/login/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'login'
        },
        password: this.password as string,
        email: this.username as string
      }).then((response) => {
        console.log(response)
        if (response.status === 200 && response.data.access) {
          console.log(response)
          this.loginError = false
          store.dispatch('insertUser', { name: response.data.name, surname: response.data.surname })
          $cookie.set('userdata', response.data.name, 60 * 60 * 24)
          $cookie.set('token', response.data.access, 60 * 60 * 24)
          router.push('/order')
        } else {
          this.loginError = true
          setTimeout(() => {
            this.loginError = false
          }, 5000)
        }
      }, (err) => {
        console.log('err', err)
        this.loginError = true
        setTimeout(() => {
          this.loginError = false
        }, 5000)
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
.error-message {
  color: white;
  font-size: 14px;
  margin-top: 20px;
  padding: 8px;
  border-radius: 5px;
  background-color: #ff0707;
  text-align: center;
}

@media only screen and (max-width: 768px) {
  .login-form {
    width: 300px;
  }

  .text-center {
    margin-inline-start: 0px !important;
  }

  .error-message {
    font-size: 12px;
    margin-top: 10px;
  }
  .login-blurb{
    min-height: 300px !important;
    width: 350px;
  }
}

@media (max-width: 1280px) {
  .mobile{
    display: none !important;
  }
}
</style>
