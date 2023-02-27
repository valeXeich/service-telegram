<template>
    <CabinetHeader :tgData="data"/>
    <div class="container mt-3">
        <div class="row">
            <div class="col-md-6 col-lg-4 block p-3">
                <h4 class="text-center">Настройка инстанса</h4>
                <input v-model="accountData.account_name" class="form-control" placeholder="Имя аккаунта">
                <div class="form-check form-switch mt-2">
                    <input v-if="!checked" class="form-check-input" type="checkbox" role="switch" @click="changeCheck">
                    <input v-else class="form-check-input" type="checkbox" role="switch" checked @click="changeCheck">
                    <label class="form-check-label" for="flexSwitchCheckDefault">Использовать прокси</label>
                </div>
                <div v-if="checked" class="mt-3">
                    <p>Поддерживаются только Socks5 прокси</p>
                    <div class="container">
                        <div class="row">
                            <div class="col-md-6">
                                <input id="input-ip" v-model="accountData.proxy_ip" class="form-control" placeholder="IP" required>
                            </div>
                            <div class="col-md-6">
                                <input id="input-port" v-model="accountData.proxy_port" class="form-control" placeholder="PORT" required>
                            </div>
                        </div>
                        <div class="row mt-2">
                            <div class="col-md-6">
                                <input v-model="accountData.proxy_username" class="form-control" placeholder="Имя пользователя">
                            </div>
                            <div class="col-md-6">
                                <input v-model="accountData.proxy_password" class="form-control" placeholder="Пароль">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="text-center">
                    <button class="btn btn-primary mt-2" @click="updateAccount">Сохранить</button>
                </div>
            </div>
            <div class="col-1"></div>
            <div class="col-md-4 col-lg-4 block p-3" style="height: 50%;">
                <h4 class="text-center">Ключ</h4>
                <div class="d-flex">
                    <input id="copy-input" type="text" class="form-control" :value="accountData.secret_key" readonly>
                    <button type="submit" class="btn btn-outline-secondary ms-1" @click="copyToClipboard">Copy</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CabinetHeader from '@/components/CabinetHeader.vue';
import axios from 'axios';
    export default {
        name: 'AccountDetail',
        components: {
            CabinetHeader
        },
        data() {
            return {
                data: JSON.parse(localStorage.getItem('tg_data')),
                checked: true,
                accountData: [],
            }
        },
        methods: {
            changeCheck() {
                this.checked = !this.checked
            },
            copyToClipboard() {
                const copyText = document.getElementById("copy-input");
                copyText.select();
                document.execCommand("copy");
            },
            async getAccount() {
                const id = this.$route.params.id;
                const response = await axios.get(`get-instance?id=${id}`)
                this.checked = response.data.proxy
                this.accountData = response.data;
            },
            async updateAccount() {
                const id = this.$route.params.id;
                if (this.checked) {
                    const ipInput = document.getElementById('input-ip');
                    const portInput = document.getElementById('input-port');
                    if (!this.accountData.proxy_ip || !this.accountData.proxy_port) {
                        ipInput.style.border = '1px solid red';
                        portInput.style.border = '1px solid red';
                    } else {
                        ipInput.style.border = '1px solid #ced4da';
                        portInput.style.border = '1px solid #ced4da';
                    }
                } 
                const formData = {
                    account_name: this.accountData.account_name,
                    proxy: this.checked,
                    proxy_ip: this.accountData.proxy_ip,
                    proxy_port: this.accountData.proxy_port,
                    proxy_username: this.accountData.proxy_username,
                    proxy_password: this.accountData.proxy_password
                }
                await axios.patch(`update-instance?account_id=${id}`, formData);
            }
        },
        mounted() {
            this.getAccount()
        }
    }
</script>

<style scoped>
.block {
    box-shadow: 0 1px 5px #0003, 0 2px 2px #00000024, 0 3px 1px -2px #0000001f;
    border-radius: 4px;
}

</style>