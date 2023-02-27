<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 text-center">
                <h1>
                    <strong class="blue-color">TELEGRAM USERBOT API</strong>
                </h1>
                <div class="main-text">
                    is an integration of a Telegram number into CRM, or any other system.
                </div>
                <div class="description mt-4">
                    A stable REST API for personal (numbered) Telegram to send and read messages via HTTP requests.
                </div>
                <div class="mt-4">
                    <div class="d-flex">
                        <img src="@/assets/good.svg" width="32" height="32" />
                        <p class="ms-3 possibilities">
                            <span class="blue-color">You can write first</span> by phone number
                        </p>
                    </div>
                    <div class="d-flex">
                        <img src="@/assets/good.svg" width="32" height="32" />
                        <p class="ms-3 possibilities">
                            It is possible <span class="blue-color">to read messages in groups</span>
                        </p>
                    </div>
                    <div class="d-flex">
                        <img src="@/assets/good.svg" width="32" height="32" />
                        <p class="ms-3 possibilities">
                            Ability <span class="blue-color">to communicate through the Telegram interface</span>
                        </p>
                    </div>
                </div>
                <button class="main-button mt-4">Try for free</button>
            </div>
            <div class="col-md-6 position-relative">
                <img width="470" height="569" src="@/assets/phone.png" />
                <img class="message message-first" src="@/assets/message_1.jpg">
                <img class="message message-second" src="@/assets/message_2.jpg">
                <img class="message message-thrid" src="@/assets/message_3.jpg">
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.main-text {
    color: #333333;
    font-size: 25px;
    font-weight: 700;
    border-color: transparent;
    border-style: solid;
}

.description {
    color: #333333;
    border-color: transparent;
    border-style: solid;
}

.possibilities {
    color: #333333;
    font-weight: 600;
    border-color: transparent;
    border-style: solid;
}

.main-button {
    color: #fff;
    font-size: 14px;
    line-height: 1.55;
    border-radius: 30px;
    background-color: #44a5fa;
    border-color: transparent;
    border-style: solid;
    transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
    box-shadow: 0px 34px 15px -19px rgb(121 191 252 / 20%);
    width: 235px;
    height: 55px;
}

.message {
    border-radius: 10px;
    border-color: transparent;
    border-style: solid;
}

.message-first {
    position: absolute;
    width: 415px;
    height: 91px;
    left: 95px;
    top: 145px;
}

.message-second {
    position: absolute;
    width: 342px;
    height: 113px;
    left: 25px;
    top: 240px;
}

.message-thrid {
    position: absolute;
    width: 386px;
    height: 91px;
    left: 170px;
    top: 355px;
}
</style>