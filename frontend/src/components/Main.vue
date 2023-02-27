<template>
    <Header />
    <Info />
    <Advantages />
    <Example />
</template>

<script>
import Info from '@/components/main/Info.vue'
import Advantages from '@/components/main/Advantages.vue'
import Example from '@/components/main/Example.vue'
import Header from "@/components/Header.vue"

export default {
    components: {
        Info,
        Advantages,
        Example,
        Header
    }
}
</script>

<style scoped>

</style>