import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

axios.defaults.baseURL = 'https://backend-fastapi-production.up.railway.app/'

createApp(App).use(store).use(router).mount('#app')
