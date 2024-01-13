// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app'
import { getStorage } from 'firebase/storage'

// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: 'AIzaSyD4NxIrenB4mwNb-sysMIilUMW56G6uCbQ',
  authDomain: 'projekt-inz-fa7e1.firebaseapp.com',
  projectId: 'projekt-inz-fa7e1',
  storageBucket: 'projekt-inz-fa7e1.appspot.com',
  messagingSenderId: '850237707233',
  appId: '1:850237707233:web:247229bf31e6572edc78a0',
  measurementId: 'G-19DB0JR7V5'
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)
const storage = getStorage(app)

export { storage }
