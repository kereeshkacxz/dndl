<template>
  <Notification>
    <div class="main_div">
      <Header
        :loginHeader="loginHeader"
        :logout="logout"
        :login="login"
        :avatar="avatar"
      />
      <div class="content">
        <slot></slot>
      </div>
      <Footer />
    </div>
  </Notification>
</template>

<script setup>
import Notification from "./notification.vue";
import Header from "./header.vue";
import Footer from "./footer.vue";

const { $api } = useNuxtApp();
const login = ref("");
const avatar = ref(null);
const config = useRuntimeConfig();
const defaultUrl = config.public.backendUrl;

async function loginHeader() {
  if (localStorage.getItem("token") === null) {
    logout();
    return;
  }
  try {
    const response = await $api.get(`/api/user/me`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    localStorage.setItem("admin", response.data.type === "admin");
    login.value = response.data.username;
    if (response.data.avatar_id)
      avatar.value = defaultUrl + "/api/get_file?id=" + response.data.avatar_id;
    console.log(avatar.value);
  } catch (error) {
    console.error(error);
    logout();
  }
}

function logout() {
  localStorage.removeItem("token");
  localStorage.setItem("admin", false);
  login.value = "";
}

function updateAvatar(newValue) {
  avatar.value = newValue;
}
onMounted(() => {
  loginHeader();
});

provide("loginHeader", loginHeader);
provide("updateAvatar", updateAvatar);
</script>

<style scoped>
.main_div {
  background: var(--bg-grad);
  width: 100%;
  min-height: 100vh;
}
.content {
  padding: calc(40px + var(--header-height)) 60px;
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: calc(100vh - 250px);
}
</style>
