<template>
    <CabinetHeader :tgData="data"/>
    <Table/>
</template>

<script>
import CabinetHeader from '@/components/CabinetHeader.vue';
import Table from '@/components/Table.vue';
    export default {
        components: {
            CabinetHeader,
            Table
        },
        data() {
            return {
                data: JSON.parse(localStorage.getItem('tg_data'))
            }
        }
    }
</script>

<style  scoped>

</style>