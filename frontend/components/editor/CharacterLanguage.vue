<template>
  <div class="language_wrapper">
    <p>ЯЗЫКИ И ПРОЧИЕ ВЛАДЕНИЯ</p>
    <CTextArea v-model="props.modelValue.other" class="language_input" />
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { default: {} },
});
</script>

<style scoped>
.language_wrapper {
  display: flex;
  flex-direction: column;
  background-color: var(--editor-color);
  gap: 10px;
  border: 1px solid var(--main-color);
  flex: 1;
  padding: 20px;
}
.language_input {
  flex: 1;
  resize: none;
}
</style>
