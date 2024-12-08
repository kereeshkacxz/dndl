<template>
  <div class="div_header">
    <NuxtLink class="link logo_text fc" :to="`/`">DND LIST</NuxtLink>
    <transition name="slide">
      <div class="navbar" :class="{ active: isMenuOpen }">
        <NuxtLink
          v-for="(key, i) in Object.keys(pages)"
          :key="i"
          :to="`/${key}`"
          :class="{
            active_page: useRoute().name === key,
            navbar_btn: useRoute().name !== key,
          }"
          >{{ pages[key] }}</NuxtLink
        >
      </div>
    </transition>
    <div class="wrapper_login">
      <div
        v-if="props.login !== ''"
        class="dropdown"
        :class="{ active: isMenuOpen }"
      >
        <NuxtImg
          :src="props.avatar ? props.avatar : 'test.jpg'"
          class="avatar"
        />

        <div class="dropdown_menu">
          <NuxtLink to="/profile" class="dropdown_item"> Профиль</NuxtLink>
          <NuxtLink class="dropdown_item" @click="logout">Выйти</NuxtLink>
        </div>
      </div>
      <div class="div_login_register" v-else>
        <NuxtLink class="link reglog" :to="`/login`">Вход</NuxtLink>
        <p class="link">/</p>
        <NuxtLink class="link reglog" :to="`/registration`"
          >Регистрация</NuxtLink
        >
      </div>
      <div class="burger" :class="{ active: isMenuOpen }" @click="toggleMenu">
        <span></span>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig();
const pages = config.public.pages;
const props = defineProps({
  logout: Function,
  login: String,
  avatar: String,
});
const isMenuOpen = ref(false);
const toggleMenu = () => {
  if (window.innerWidth < 1100) {
    isMenuOpen.value = !isMenuOpen.value;
    if (isMenuOpen.value) disableScroll();
    else enableScroll();
  } else {
    isMenuOpen.value = false;
  }
};

const disableScroll = () => {
  document.body.style.overflow = "hidden";
};

const enableScroll = () => {
  document.body.style.overflow = "";
};
</script>

<style scoped>
.div_header {
  z-index: 4;
  position: fixed;
  height: var(--header-height);
  width: 100%;
  padding: 10px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--second-color);
}

.navbar {
  display: flex;
  gap: 40px;
}

.div_login_register {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
}

.logo_text {
  font-size: 46px;
  text-decoration: none;
}

.link {
  user-select: none;
  transition: all 0.3s;
}

.link:hover {
  color: var(--main-color);
}

.navbar_btn {
  user-select: none;
  text-decoration: none;
  padding: 5px 10px;
  border: 2px solid transparent;
  transition: all 0.3s;
}

.navbar_btn:hover {
  border-color: white;
}

.active_page {
  user-select: none;
  text-decoration: none;
  padding: 5px 10px;
  transition: all 0.3s;
  border: 2px solid var(--main-color);
  color: var(--main-color);
}

.burger {
  margin-left: 20px;
  display: none;
  width: 32px;
  height: 32px;
  cursor: pointer;
  z-index: 1000;
  position: relative;
  justify-content: center;
  align-items: center;
}

.burger span {
  width: 100%;
  height: 4px;
  background-color: white;
  border-radius: 12px;
  display: block;
  margin: auto;
  transition: background-color 0.2s ease-in-out;
}

.burger span::before,
.burger span::after {
  content: "";
  width: 100%;
  background-color: white;
  display: block;
  transition: all 0.2s ease-in-out;
  border-radius: 12px;
  height: 4px;
}

.burger span::before {
  transform: translateY(-10px);
}

.burger span::after {
  transform: translateY(10px);
  margin-top: -4px;
}

.burger.active span {
  background-color: transparent;
}

.burger.active span::before {
  transform: rotateZ(45deg) translateY(0);
}

.burger.active span::after {
  transform: rotateZ(-45deg) translateY(0);
}
@media (max-width: 1100px) {
  .burger {
    display: flex;
  }
  .navbar {
    display: flex;
    flex-direction: column;
    position: fixed;
    gap: 20px;
    top: calc(-100vh);
    left: 0;
    width: 100%;
    height: 100vh;
    border-bottom: 1px solid var(--main-color);
    z-index: 5;
    transition: all 0.5s ease;
    align-items: center;
    justify-content: center;
  }
}
.navbar.active {
  background-color: var(--second-color);
  top: 0px;
}

@media (max-width: 500px) {
  .div_header {
    padding: 10px 10px;
  }
  .logo_text {
    font-size: 36px;
  }
  .reglog {
    font-size: 14px;
  }
}

.dropdown {
  transition: all 0.5s;
  z-index: 4;
  margin-right: 5px;
  display: flex;
  justify-content: center;
  width: fit-content;
  align-items: center;
}

.dropdown_menu {
  display: none;
  position: absolute;
  background-color: var(--second-color);
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  right: 5px;
  top: 56px;
  width: 150px;
  text-align: center;
}

.dropdown_item {
  color: var(--text-color);
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  transition: all 0.2s;
  cursor: pointer;
}
.dropdown_item:hover {
  color: var(--main-color);
}
.dropdown:hover .dropdown_menu {
  display: flex;
  flex-direction: column;
}

.avatar {
  cursor: pointer;
  line-height: 0;
  display: inline-block;
  border: 2px solid rgba(200, 200, 200, 0.4);
  border-radius: 50%;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
  transition: linear 0.25s;
  height: 52px;
  width: 52px;
  object-fit: cover;
}

.wrapper_login {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
