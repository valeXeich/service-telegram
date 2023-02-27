<template>
    <div class="container main-text">
        <h1>
            QUICK AND CLEAR <span class="blue-color">SELF-ACTIVATION</span> OF
            <br>
            THE ACCOUNT
        </h1>
    </div>
    <div class="container mb-5">
        <div class="row">
            <div class="col-md-5 mt-5">
                <div class="d-flex">
                    <div class="circle">1</div>
                    <h3 class="pointer-cursor blue-color section ms-2" @click="setTitle('Send message')">
                        Send message
                    </h3>
                </div>
                <div class="d-flex mt-2">
                    <div class="circle">2</div>
                    <h3 class="pointer-cursor blue-color section ms-2" @click="setTitle('Send photo')">
                        Send photo
                    </h3>
                </div>
                <div class="d-flex mt-2">
                    <div class="circle">3</div>
                    <h3 class="pointer-cursor blue-color section ms-2" @click="setTitle('Find a user by phone number')">
                        Find a user by phone number
                    </h3>
                </div>
            </div>
            <div class="col-md-5">
                <div class="window">
                    <h4 class="text-uppercase blue-color">{{ title }}</h4>
                    <div v-if="description" class="description mb-5">
                        <span>
                            If the dialog was initiated by the client, you can reply with a normal message.
                            This dialog is also paid, if you responded to the client.
                            You can communicate with him for free for 24 hours from the moment of the answer.
                        </span>
                    </div>
                    <div class="d-flex">
                        <p class="pointer-cursor text-muted" @click="python = false">Curl (Bash)</p>
                        <p class="pointer-cursor ms-4" @click="python = true">Python</p>
                    </div>
                    <div class="code-window">
                        <div v-if="python">
                            <span class="comment">// URL для запроса GET /messages</span>
                            <br>
                        </div>
                        <span class="text-white">curl \</span>
                        <br>
                        <span class="text-white">-d</span> '{"phone": "79995253422","template": "template_name",
                        "namespace" : "namespace_of_template", "language": { "code": "en", "policy": "deterministic"}}'
                        <span class="text-white">/</span>
                        <br>
                        <span class="comment"># Phone and template parameters</span>
                        <br>
                        <span class="text-white">-H</span> "Content-Type: application/json"
                        <span class="text-white"> \ </span>
                        <span class="comment"># Headers</span>
                        <br>
                        <span class="text-white">-X POST \</span>
                        <span class="comment"># Type = POST"</span>
                        <br>
                        https://api.chat-api.com/sendTemplate?token=83763g87x"
                        <span class="comment"># URL for request POST /message</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            python: false,
            description: false,
            title: 'send message'
        };
    },
    methods: {
        setTitle(text) {
            if (text == 'Find a user by phone number') {
                this.description = true
            } else {
                this.description = false
            }
            this.title = text;
        }
    }
}
</script>

<style scoped>
.main-text {
    margin-top: 70px;
    margin-bottom: 70px;
    border-color: transparent;
    border-style: solid;
}

.section {
    font-size: 18px;
    font-weight: 400;
    border-color: transparent;
    border-style: solid;
}

.section:hover {
    color: gray;
}

.circle {
    width: 25px;
    height: 25px;
    color: #fff;
    background-color: rgb(68, 165, 250);
    border-radius: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.window {
    padding: 35px;
    box-shadow: 0px 1px 23px 5px rgb(163 163 163 / 20%);
}

.code-window {
    background-color: #333333;
    border-radius: 5px;
    border-color: transparent;
    border-style: solid;
    padding: 15px;
    color: rgb(240, 113, 113);
}

.comment {
    color: rgb(4, 212, 56);
}

.pointer-cursor {
    cursor: pointer;
}
</style>