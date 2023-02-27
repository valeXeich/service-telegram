<template>
    <nav class="bg-light sidebar">
        <div class="sidebar-sticky">
            <ul class="nav flex-column">
                <li class="mt-4 nav-item">
                    <router-link to="/cabinet" class="nav-link link-dark back-color">
                        <i class="bi bi-send-fill icon"></i>
                        <span class="section">APIKeys</span>
                    </router-link>
                    <router-link to="/cabinet/settings" class="nav-link link-dark back-color">
                        <i class="bi bi-gear-fill icon"></i>
                        <span class="section">Settings</span>
                    </router-link>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
export default {

}
</script>

<style  scoped>
.sidebar {
    width: 200px;
    border-right: 1px solid rgba(0, 0, 0, .12);
    height: 840px;
}

.section {
    margin-left: 30px;
    font-size: 15px;
}

.back-color:hover {
    background-color: #dddddd;
}

.icon {
    font-size: 25px;
}
</style>