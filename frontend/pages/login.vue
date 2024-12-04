<template>
  <div class="div_login">
    <h1 class="title fc">Вход</h1>
    <div class="div_form">
      <div class="column">
        <p class="field">Логин:</p>
        <p class="field">Пароль:</p>
      </div>
      <div class="column">
        <CInput
          placeholder="Введите логин"
          v-model="login"
          @keyup.enter="validation"
        />
        <CInput
          placeholder="Введите пароль"
          v-model="password"
          type="password"
          @keyup.enter="validation"
        />
      </div>
    </div>
    <CButton class="btn_login" @click="validation">Войти</CButton>
    <NuxtLink to="/registration" class="change_window"
      >Создать аккаунт</NuxtLink
    >
  </div>
</template>

<script setup>
const { $api } = useNuxtApp();
const login = ref("");
const password = ref("");
const router = useRouter();

function validation() {
  if (!login.value) {
    createNotification("Введите логин!", "unsuccess");
    return;
  }
  if (!password.value) {
    createNotification("Введите пароль!", "error");
    return;
  }
  if (login.value.length < 5) {
    createNotification("Логин должен быть больше 4 символов!", "error");
    return;
  }
  if (password.value.length < 8) {
    createNotification("Пароль должен быть больше 7 символов!", "error");
    return;
  }
  loginFunc();
}

async function loginFunc() {
  try {
    const response = await $api.post(
      `/api/v1/user/login`,
      {
        username: login.value,
        password: password.value,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    localStorage.setItem("token", response.data.access_token);
    createNotification("Вы успешно авторизовались!", "success");
    loginHeader();
    router.push("/");
  } catch (error) {
    console.error(error);
    createNotification(`${error.response.data.detail}`, "error");
  }
}
onMounted(() => {
  if (localStorage.getItem("token")) router.push("/");
  fetch();
});

let createNotification;
let loginHeader;

function fetch() {
  createNotification = inject("createNotification");
  loginHeader = inject("loginHeader");
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
