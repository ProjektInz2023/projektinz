// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app'
import { getStorage } from 'firebase/storage'

// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: 'AIzaSyDgDs8MxVvPrr3uO5Z3AOnxwhG5msaRadI',
  authDomain: 'kantyna-3f92b.firebaseapp.com',
  projectId: 'kantyna-3f92b',
  storageBucket: 'kantyna-3f92b.appspot.com',
  messagingSenderId: '468501709396',
  appId: '1:468501709396:web:3e51bcc1382794fdcca3c1'
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)
const storage = getStorage(app)

export { storage }
