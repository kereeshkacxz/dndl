<template>
  <div class="gender-toggle" @click="toggleGender">
    <div class="toggle">
      <div
        class="toggle-circle"
        :class="{
          male: props.modelValue === 'male' || !props.modelValue,
          female: props.modelValue === 'female',
        }"
      >
        {{ props.modelValue === "male" || !props.modelValue ? "М" : "Ж" }}
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { default: "male" },
});
const emit = defineEmits(["update:modelValue"]);
const toggleGender = () => {
  emit(
    "update:modelValue",
    props.modelValue === "male" || !props.modelValue ? "female" : "male"
  );
};
</script>

<style scoped>
.gender-toggle {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.toggle {
  width: 100px;
  height: 50px;
  background-color: black;
  border-radius: 10px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}

.toggle-circle {
  width: 40px;
  height: 40px;
  background-color: var(--success-color);
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  border-radius: 5px;
  position: absolute;
  top: 5px;
  user-select: none;
  transition: all 0.3s;
}

.toggle-circle.male {
  transform: translateX(-20px);
}

.toggle-circle.female {
  transform: translateX(20px);
}

.toggle-text {
  position: absolute;
  color: white;
  font-weight: bold;
}
</style>
