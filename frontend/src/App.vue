<template>
  <router-view/>
</template>

<script>
import axios from 'axios';
export default {
  beforeCreate() {
    const token = localStorage.getItem('token');
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    }
  }
}
</script>

<style>

.blue-color {
  color: rgb(68, 165, 250);
}

</style>
