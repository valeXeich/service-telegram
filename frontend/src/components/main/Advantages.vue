<template>
  <div class="container main-text">
    <h1>
      <span class="blue-color">DIFFERENCES</span>
      BETWEEN THE
      <br>
      USERBOT AND THE BOT
    </h1>
  </div>
  <div class="container">
    <table class="table" style="box-shadow: 0px 0px 25px 0px rgb(0 0 0 / 10%); border-radius: 8px;">
      <thead>
        <tr class="tr-color">
          <th></th>
          <th class="blue-color text-center talbe-field">TELEGRAM USERBOT</th>
          <th class="blue-color text-center talbe-field">TELEGRAM BOT</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="blue-color table-text">You can write first by phone number</td>
          <td class="text-center check-mark">
            <i class="fas fa-check-circle mt-4"></i>
          </td>
          <td class="text-center check-xmark">
            <i class="fas fa-times-circle mt-4"></i>
          </td>
        </tr>
        <tr>
          <td class="blue-color table-text">It is possible to read messages in groups</td>
          <td class="text-center check-mark">
            <i class="fas fa-check-circle mt-4"></i>
          </td>
          <td class="text-center check-xmark">
            <i class="fas fa-times-circle mt-4"></i>
          </td>
        </tr>
        <tr>
          <td class="blue-color table-text">Ability to communicate through the Telegram interface</td>
          <td class="text-center check-mark">
            <i class="fas fa-check-circle mt-4"></i>
          </td>
          <td class="text-center check-xmark">
            <i class="fas fa-times-circle mt-4"></i>
          </td>
        </tr>
        <tr class="end-border">
          <td class="blue-color table-text">All the features of a regular Telegram use</td>
          <td class="text-center check-mark">
            <i class="fas fa-check-circle mt-4"></i>
          </td>
          <td class="text-center check-xmark">
            <i class="fas fa-times-circle mt-4"></i>
          </td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.main-text {
  margin-top: 70px;
  margin-bottom: 70px;
  border-color: transparent;
  border-style: solid;
}

.talbe-field {
  font-size: 18px;
}

.table-text {
  padding: 22px 20px;
  width: 260px;
}

.end-border {
  border-bottom: #fff;
}

.check-mark {
  font-size: 24px;
  color: #25b309;
  width: 449px
}

.check-xmark {
  font-size: 24px;
  color: rgb(242, 70, 17);
  width: 449px
}

.table-rounded {
  border-radius: 10px;
}

.tr-color {
  background-color: #f2f8fd;
  border-bottom: #fff;
}
</style>