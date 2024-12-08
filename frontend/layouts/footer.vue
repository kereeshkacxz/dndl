<template>
  <div class="div_footer">
    <div><h2 class="title">Контакты</h2></div>
    <div class="div_decoration">
      <div class="decoration decoration-left"></div>
      <div class="decoration decoration-right"></div>
    </div>
    <div class="contacts">
      <div></div>
      <h2 class="contact">Phone: +7(963)-742-28-80</h2>
      <h2 class="contact">Email: kvl7312@yandex.ru</h2>
      <div></div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.div_footer {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 10px;
  height: 160px;
}

.title {
  font-weight: bold;
  color: var(--main-color);
  user-select: none;
}

.decoration {
  background-image: url("~/public/footer-decor.png");
  background-size: contain;
  background-repeat: no-repeat;
  width: 40%;
  max-width: 400px;
  aspect-ratio: 5/1;
}
.div_decoration {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 125px;
}
.decoration-left {
  transform: scaleX(-1);
}
.contacts {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
@media (max-width: 700px) {
  .decoration {
    width: 48%;
  }
  .div_decoration {
    gap: 0px;
  }
  .title {
    font-size: 18px;
  }
  .contact {
    font-size: 16px;
  }
}
@media (max-width: 450px) {
  .contacts {
    flex-direction: column;
    text-align: center;
    gap: 10px;
  }
}
</style>
