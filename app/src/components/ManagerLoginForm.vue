<template>
  <div class="form-container center-horiz">
    <form @submit.prevent="sprawdz()" autocomplete="off">
      <div class="form-group">
        <fieldset>
          <legend>
            <h2 class="hero-text">Manager</h2>
          </legend>
          <div class="line"></div>
          <input
            id="email"
            autocomplete="off"
            placeholder="manager@blum.com"
            name="login"
            type="text"
            v-model="email"
            maxlength="20"
            v-bind:class="{ hasError: error_highlight }"
          />
        </fieldset>
      </div>
      <div class="form-group">
        <fieldset>
          <input
            id="password"
            type="password"
            autocomplete="off"
            placeholder="password"
            name="pass"
            v-model="password"
            maxlength="20"
            v-bind:class="{ hasError: error_highlight }"
          />
        </fieldset>
      </div>
      <button type="submit" class="btn">{{ send }}</button>
    </form>
    <a @click="redirectToCookLogin"  class="redirect-link">
      <legend>
        <h2 class="hero-text smaller"> Kucharz</h2>
      </legend>
    </a>
    <p v-if="loginError" class="error-message">Błędne dane logowania. Spróbuj ponownie.</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'
import router from '@/router'
const $cookie = require('vue-cookies')
axios.defaults.withCredentials = true

export default defineComponent({
  name: 'ManagerLoginForm',
  data: function () {
    return {
      send: 'Log in',
      email: '',
      password: '',
      errors: [] as string[],
      error_highlight: false,
      loginError: false
    }
  },
  methods: {
    sprawdz () {
      this.errors = []
      if (!this.email) {
        this.errors.push('Email required.')
      } else if (!this.validEmail(this.email)) {
        this.errors.push('Valid email required. ex."manager@mail.com"')
      }
      if (!(this.errors.length > 0)) {
        this.error_highlight = false
        this.Wyslij()
      } else {
        this.error_highlight = true
      }
    },
    validEmail: function (email: string) {
      const re = /^(([^<>()\]\\.,;:\s@"]+(\.[^<>()\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      // return re.test(email)
      return true
    },
    Wyslij: function () {
      if ((!this.email) || (this.email.length === 0 && !this.password) || (this.password.length === 0)) {
        this.error_highlight = true
      } else {
        this.login()
        this.email = ''
        this.password = ''
      }
    },
    async login () {
      axios.post('http://127.0.0.1:8000/api/loginadmin/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'login'
        },
        password: this.password as string,
        email: this.email as string
      }).then((response) => {
        if (response.status === 200 && response.data.access) {
          console.log(response)
          this.loginError = false
          $cookie.set('managerToken', response.data.access, 60 * 60 * 24)
          router.push('/manager-account')
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
    },
    redirectToCookLogin () {
      router.push('/')
    }
  }
})
</script>

<style lang="css" scoped>
.form-container {
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
a{
  text-decoration: none;
}
a:active{
  text-decoration: none;
}
.hero-text{
  font-weight: 400;
}
.smaller{
  margin-top:30px;
  font-size: 100% !important;
}
.form-container{
  padding: 0%;
  width:50%;
  height:20%;
}
.smaller{
  font-size:160%;
}
input:focus{
  outline-width:0;
}
input::placeholder{
  font-size: smaller;
}
input{
  border:0px;
  border-radius:5px;
  text-indent:20px;
  width:100%;
  height:50px;
  font-size: 120%;
  background-color: rgba(244,244,244,1);
  z-index: 1;
  transition: all 0.3s ease-in;
  margin:0 auto;
  padding:5px;
  padding-left: 2%;
  padding-right: 2%;
  color:rgba(0,0,0,0.4);
  position: relative;
}
input:hover{
  background-color: rgba(250,250,250,1);
  color:rgba(0,0,0,0.8);
  cursor: text;
}

input:focus{
  background-color: rgba(255,255,255,1);
  color:rgba(0,0,0,1);
  box-shadow: rgba(255,103,31,1) 0px 0px 5px 1px;
}
legend>h2{
  margin:0.5rem;
  font-size: 170%;
}
legend{
  text-transform:capitalize;
  letter-spacing: 2px;
  color:rgba(255,165,0,1);
}
/*
##########################################################
Form swap link
##########################################################
*/
.register{
  text-decoration: none;
  color: black;
  display:block;
  font-size:100%;
  text-transform:uppercase;
}
.disable{
  text-align: center;
  width:100%;
  text-decoration: none;
  padding:0px;
  font-size: 120%;
  letter-spacing: 1px;
  color:rgba(100,100,100,1) !important;
}
.reg-link{
  text-decoration: underline !important;
  cursor: pointer;
  color:rgba(255,162,0,1) !important;
}
.reg-link:hover{
  color:rgba(255,162,0,0.8) !important;
}
/*
##########################################################
button
##########################################################
*/
.btn{
  margin-top:25px;
  border-radius:45px;
  font-size:110%;
  color:rgba(255,255,255,1);
  width:180px;
  height:45px;
  background:rgba(255,103,31,1);
  border: 0px;
}
.btn:hover{
  transition: all 0.3s ease-in;
  background:rgba(255,255,255,0.9);
  color: rgba(255,103,31,1);
  cursor: pointer;
  color:black;
}
.special-btn{
  margin-top:25px;
  border-radius:50px;
  font-size:110%;
  color:rgba(100,100,100,1);
  width:200px;
  height:45px;
  background:rgba(255,255,255,1);
  margin-left:6%;
}
.special-send{
  margin-top:25px;
  border-radius:50px;
  font-size:110%;
  color:rgba(100,100,100,1);
  width:200px;
  height:45px;
  background:rgba(255,255,255,1);
  margin-left:0%;
}
.hasError{
  box-shadow: 0px 0px 4px 2px rgba(223, 21, 88,1);
}
/*
############################################
Media queries
############################################
*/
/*##############################################*/
fieldset{
  position: relative;
  border:0px;
}
a{
  cursor:pointer;
}
ul{
  padding: 0;
}

.error-message {
  color: white;
  font-size: 14px;
  margin-top: 20px;
  padding: 8px;
  border-radius: 5px;
  background-color: #ff0707;
}
</style>
