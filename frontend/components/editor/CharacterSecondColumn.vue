<template>
  <div class="column_wrapper">
    <CharacterVitality v-model="props.vitality" />
    <CharacterAttacks v-model="props.attacks" />
    <CharacterEquipment v-model="props.equipment" />
  </div>
</template>

<script setup>
import CharacterVitality from "./CharacterVitality.vue";
import CharacterAttacks from "./CharacterAttacks.vue";
import CharacterEquipment from "./CharacterEquipment.vue";
const props = defineProps({
  vitality: { default: {} },
  attacks: { default: [] },
  equipment: { default: {} },
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
