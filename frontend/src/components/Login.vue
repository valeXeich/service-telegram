<template>
    <div class="container">
        <div class="row">
            <div class="col-3"></div>
            <div class="col-5 main">
                <h4 class="text-center mt-2">Authorization</h4>
                <div class="mt-4 text-center">
                    <telegram-login-temp mode="callback" telegram-login="DistributionTelegramAuthBot" @callback="saveData" />
                </div>
            </div>
            <div class="col-4"></div>
        </div>
    </div>
</template>

<script>
import { telegramLoginTemp } from 'vue3-telegram-login'
import axios from 'axios'

export default {
    name: 'Login',
    components: {
        telegramLoginTemp,
    },
    methods: {
        async saveData(user) {
            const formData = {
                tg_id: user.id,
                username: user.username
            };
            const response = await axios.post('login', formData);
            const data = JSON.stringify(user);
            const token = response.data.token
            localStorage.setItem('tg_data', data);
            localStorage.setItem('token', token);
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            this.$router.push('/cabinet');
        }
    }
}
</script>

<style scoped>

.main {
    margin-top: 25%;
    box-shadow: 0 1px 5px #0003, 0 2px 2px #00000024, 0 3px 1px -2px #0000001f;
    border-radius: 4px;
}
</style>