<template>
  <div class="column_wrapper">
    <CharacterMainSpecification v-model="props.modelValue" />
    <CharacterPerception v-model="props.modelValue" />
    <CharacterLanguage v-model="props.modelValue" />
  </div>
</template>

<script setup>
import CharacterPerception from "./CharacterPerception.vue";
import CharacterLanguage from "./CharacterLanguage.vue";
import CharacterMainSpecification from "./CharacterMainSpecification.vue";

const props = defineProps({
  modelValue: { default: {} },
});
</script>

<style scoped>
.column_wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  flex: 1 1 0%;
}
</style>
