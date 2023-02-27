<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <span class="navbar-brand text-white" >TelegramUserBot</span>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link" to="/cabinet">Аккаунты</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/cabinet/settings">Настройки</router-link>
        </li>
      </ul>
      
    <img class="img-fluid rounded-circle" width="40" height="40" :src="tgData.photo_url" alt="">
    <span class="text-white ms-2 username">{{ tgData.username }}</span>
    <i class="bi bi-box-arrow-right ms-3 pt-1 exit" @click="logOut"></i>
    </div>
  </div>
</nav>
</template>

<script>
import axios from 'axios';
    export default {
        name: 'CabinetHeader',
        props: ['tgData'],
        methods: {
          logOut() {
            localStorage.removeItem('tgData');
            localStorage.removeItem('token');
            axios.defaults.headers.common['Authorization'] = '';
            this.$router.push('/');
          }
        }
    }
</script>

<style  scoped>
    .navbar {
        background-color: #1976d2;
    }

    .exit:hover {
        color: rgb(160, 52, 52);
    }
    .exit {
        cursor: pointer;
        font-size: 24px;
    }

    .nav-link {
        color: #fff;
    }

    .nav-link:hover {
        color: #e8e8e8
    }
</style>