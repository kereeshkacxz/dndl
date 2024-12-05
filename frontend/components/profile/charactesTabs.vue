<template>
  <!-- <div class="tabs_wrapper">
    <div class="tabs_menu">
      <div class="tab" :class="{active: }">Мои персонажи</div>
      <div class="tab">Доступные персонажи</div>
      <div class="tab" v-if="isAdmin">Все персонажи</div>
    </div>
    <div class="characters_wrapper"></div>
  </div> -->
</template>

<script setup>
const isAdmin = ref(localStorage.getItem("admin") === "true");
</script>

<style scoped>
.tabs_wrapper {
  display: flex;
  justify-content: center;
}
.tabs_menu {
  display: flex;
  gap: 20px;
}
.tab {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--second-color);
  height: 60px;
  border-radius: 5px;
}
</style>
