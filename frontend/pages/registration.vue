<template>
  <div class="div_login">
    <h1 class="title fc">Регистрация</h1>
    <div class="div_form">
      <div class="column">
        <p class="field">Логин:</p>
        <p class="field">Пароль:</p>
        <p class="field">Повтор пароля:</p>
      </div>
      <div class="column">
        <CInput
          placeholder="Введите логин"
          v-model="login"
          @keyup.enter="registerFunc"
        />
        <CInput
          placeholder="Введите пароль"
          v-model="secondPassword"
          type="password"
          @keyup.enter="registerFunc"
        />
        <CInput
          placeholder="Введите пароль еще раз"
          v-model="password"
          type="password"
          @keyup.enter="registerFunc"
        />
      </div>
    </div>
    <CButton class="btn_login" @click="registerFunc"
      >Зарегистрироваться</CButton
    >
    <NuxtLink to="/login" class="change_window"
      >Уже есть аккаунт? Войти.</NuxtLink
    >
  </div>
</template>

<script setup>
const { $api } = useNuxtApp();
const login = ref("");
const password = ref("");
const secondPassword = ref("");

async function registerFunc() {
  try {
    // const response = await $api.post(
    //   `/api/Auth/byLogin?login=${login.value}&pass=${password.value}`,
    //   {
    //     headers: {
    //       "Content-Type": "application/json",
    //     },
    //     params: {
    //       login: login.value,
    //       password: password.value,
    //     },
    //   }
    // );
    // localStorage.setItem("token", response.data);
    createNotification("Вы успешно зарегистрировались!", "success");
  } catch (error) {
    createNotification("Произошла какая-то ошибка :(", "error");
    console.error(error);
  }
}
onMounted(() => {
  fetch();
});
let createNotification;

function fetch() {
  createNotification = inject("createNotification");
}
</script>

<style scoped>
.div_login {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 30px;
}
.title {
  user-select: none;
  font-size: 48px;
}
.div_form {
  display: flex;
  gap: 20px;
}
.column {
  gap: 10px;
  display: flex;
  flex-direction: column;
}
.field {
  user-select: none;
  font-size: 16px;
  padding: 6px;
  color: var(--main-color);
}
.btn_login {
  width: 200px;
}
.change_window {
  user-select: none;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  opacity: 70%;
}

.change_window:hover {
  opacity: 90%;
  color: var(--main-color);
}
</style>
