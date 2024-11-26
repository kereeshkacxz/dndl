<template>
  <Notification>
    <div class="fwh main_div">
      <Header />
      <div class="content">
        <slot></slot>
      </div>
    </div>
  </Notification>
</template>

<script setup>
import Notification from "./notification.vue";
import Header from "./header.vue";
const checkContestExists = async (contestId) => {
  try {
    const responseName = await $api.get(`/api/Contest/${contestId}`);
  } catch (error) {
    contestNotExists.value = true;
  }
};

const route = useRoute();
const contestNotExists = ref(false);

onMounted(() => {
  const contestId = parseInt(route.params.id);
  if (route.name.includes("contests-id"))
    contestNotExists.value = checkContestExists(contestId);
});
</script>

<style scoped>
.main_div {
  background: var(--bg-grad);
  width: 100%;
  min-height: 100vh;
}
.content {
  padding: calc(var(--padding-content-height) + var(--header-height))
    var(--padding-content-width);
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  z-index: 3;
}

@media (max-width: 1200px) {
  .content {
    padding: calc(var(--padding-content-height) + var(--header-height))
      var(--padding-content-width-small);
  }
}
.not_exist {
  color: var(--main-color);
}
</style>
