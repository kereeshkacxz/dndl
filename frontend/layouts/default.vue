<template>
  <Notification>
    <div class="main_div">
      <Header :loginHeader="loginHeader" :logout="logout" :login="login" />
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

async function loginHeader() {
  if (localStorage.getItem("token") === null) {
    logout();
    return;
  }
  try {
    const response = await $api.get(`/api/v1/user/me`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    localStorage.setItem("admin", response.data.type === "admin");
    login.value = response.data.username;
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

onMounted(() => {
  loginHeader();
});

provide("loginHeader", loginHeader);
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
