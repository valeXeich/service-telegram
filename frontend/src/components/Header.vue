<template>
  <header class="header">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="@/assets/telegram.png" alt="Logo" width="58" height="58" class="d-inline-block align-top">
      </a>
      <div class="navbar-collapse justify-content-center" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#">Price</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Support</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://backend-fastapi-production.up.railway.app/docs">Documentation</a>
          </li>
        </ul>
      </div>
      <div class="d-flex justify-content-end">
        <router-link v-if="!token" to="/login">
          <button class="btn btn-primary me-2">Personal Cabinet</button>
        </router-link>
        <router-link v-else to="/cabinet">
          <button class="btn btn-primary">Personal Cabinet</button>
        </router-link>
      </div>
    </div>
  </nav>
</header>

</template>
<script>
export default {
  name: 'Header',
  data() {
    return {
      token: localStorage.getItem('token')
    }
  }
}
</script>

<style scoped>
.login-btn {
  color: #ffffff;
  font-size: 14px;
  line-height: 1.55;
  font-weight: 400;
  border-width: 1px;
  border-radius: 30px;
  background-color: #44a5fa;
  background-position: center center;
  border-color: transparent;
  border-style: solid;
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
  padding: 10px;
}

.nav-link {
  color: #333333;
  font-size: 18px;
  font-weight: 400;
  font-family: 'Roboto', Arial, sans-serif;
}


.nav-link:hover {
  color: #44a5fa;
}

.header {
  box-shadow: 0px 3px 13px rgb(51 51 51 / 10%);
}
</style>