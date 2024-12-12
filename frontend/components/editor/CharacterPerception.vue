<template>
  <div class="perception_wrapper">
    <div class="editor_perception">
      <CInput
        v-model="props.modelValue.perception"
        class="input"
        type="number"
      />
    </div>
    <div class="title">ПАССИВНАЯ МУДРОСТЬ (ВОСПРЯИТИЕ)</div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { default: {} },
});
</script>

<style scoped>
.perception_wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}
.title {
  background-color: var(--editor-color);
  padding: 10px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  flex: 1;
  height: fit-content;
}
.editor_perception {
  width: 70px;
  height: 60px;
  background-color: var(--editor-color);
  border-radius: 25px;
  border: 2px solid var(--main-color);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}
.input {
  width: 50px;
  text-align: center;
}
</style>
