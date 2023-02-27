<template>
    <CabinetHeader :tgData="data"/>
    <div class="container mt-3">
        <div class="row">
            <div class="col-12 block p-3">
                <h4 class="text-center">Настройка аккаунта</h4>
                <input v-model="appID" class="form-control" placeholder="App ID">
                <input v-model="appHash" class="form-control mt-2" placeholder="App Hash">
                <div class="text-center mt-3">
                    <button class="btn btn-primary" @click="updateBotData">Сохранить</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CabinetHeader from '@/components/CabinetHeader.vue';
import axios from 'axios';
    export default {
        name: 'CabinetSettings',
        components: {
            CabinetHeader
        },
        data() {
            return {
                data: JSON.parse(localStorage.getItem('tg_data')),
                appID: '',
                appHash: ''
            }
        },
        methods: {
            async updateBotData() {
                const formData = {
                    bot_id: this.appID,
                    bot_hash: this.appHash
                }
                await axios.post('change-bot-data', formData)
            },
            async getBotData() {
                const response = await axios.get('get-bot-data');
                this.appID = response.data.bot_id;
                this.appHash = response.data.bot_hash;
            }
        },
        mounted() {
            this.getBotData()
        }
    }
</script>

<style scoped>
.block {
    box-shadow: 0 1px 5px #0003, 0 2px 2px #00000024, 0 3px 1px -2px #0000001f;
    border-radius: 4px;
}

</style>