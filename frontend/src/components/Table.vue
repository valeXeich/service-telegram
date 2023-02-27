<template>
    <div class="text-center mt-3">
        <button class="btn btn-success" @click="addAccount">Создать инстанс</button>
    </div>
    <div class="container mt-3">
        <div class="row">
            <div class="col-12">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Имя аккаунта</th>
                            <th scope="col">Прокси</th>
                        </tr>
                    </thead>
                    <tbody>
                        <template v-for="account in accounts" :key="account.id">
                            <tr class="pointer" @click="redirectDetail(account.id)">
                                <th scope="row">{{ account.id }}</th>
                                <td>{{ account.name ? account.name : '-' }}</td>
                                <td>{{ account.proxy }}</td>
                            </tr>
                        </template>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Table',
    data() {
        return {
            accounts: []
        }
    },
    methods: {
        redirectDetail(accountId) {
            this.$router.push(`/cabinet/detail/${accountId}`)
        },
        async getAccounts() {
            const response = await axios.get('get-instances');
            this.accounts = response.data
        },
        async addAccount() {
            const response = await axios.post('create-instance');
            this.accounts.push(response.data)
        }
    },
    mounted() {
        this.getAccounts()
    }
}
</script>

<style scoped>

.pointer {
    cursor: pointer;
}
</style>