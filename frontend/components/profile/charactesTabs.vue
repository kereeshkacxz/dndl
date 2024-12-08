<template>
  <div class="tabs_wrapper">
    <div class="tabs_menu">
      <div class="tab" :class="{ active: curTab === 0 }" @click="changeTab(0)">
        Мои персонажи
      </div>
      <div class="tab" :class="{ active: curTab === 1 }" @click="changeTab(1)">
        Доступные персонажи
      </div>
      <div
        class="tab"
        :class="{ active: curTab === 2 }"
        v-if="isAdmin"
        @click="changeTab(2)"
      >
        Все персонажи
      </div>
      <CSelectableList
        class="selectable"
        :items="tabs"
        :curIdx="curTab"
        @changeIndex="(i) => (curTab = i)"
      />
    </div>
    <div class="characters_wrapper"></div>
  </div>
</template>

<script setup>
const isAdmin = ref(localStorage.getItem("admin") === "true");
const curTab = ref(0);

function changeTab(newValue) {
  curTab.value = newValue;
}

const tabs = isAdmin.value
  ? ["Мои персонажи", "Доступные персонажи", "Все персонажи"]
  : ["Мои персонажи", "Доступные персонажи"];
</script>

<style scoped>
.tabs_wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  height: 700px;
  background-color: rgb(32, 32, 32);
  border-radius: 10px;
  border: 1px solid var(--main-color);
  flex-direction: column;
}
.tabs_menu {
  padding: 10px;
  display: flex;
  gap: 20px;
  width: 100%;
  border-bottom: 1px solid var(--main-color);
  height: 80px;
}
.tab {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--second-color);
  height: 60px;
  border-radius: 5px;
  user-select: none;
  cursor: pointer;
  padding: 10px;
  border: 1px solid transparent;
  transition: all 0.3s;
}
.tab.active {
  border: 1px solid var(--main-color);
}
.characters_wrapper {
  flex: 1;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;
  background-color: var(--second-color);
}
.selectable {
  display: none;
}
@media (max-width: 500px) {
  .selectable {
    display: block;
  }
  .tab {
    display: none;
  }
  .characters_wrapper {
    border-radius: 10px;
  }
  .tabs_menu {
    height: 60px;
  }
}
</style>
