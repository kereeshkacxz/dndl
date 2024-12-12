<template>
  <textarea
    class="ctextarea"
    :type="type"
    :value="modelValue"
    :placeholder="placeholder"
    @input="handleInput"
    @focus="handleFocus"
    @blur="handleBlur"
  />
</template>

<script setup>
const props = defineProps({
  placeholder: { default: "", type: String },
  modelValue: { default: "", type: [String, Number] },
  type: { default: "text", type: String },
  unit: { type: String, default: "" },
});

const emit = defineEmits([
  "update:modelValue",
  "focus",
  "input",
  "blur",
  "change",
]);

function handleInput(e) {
  let value = e.target.value;
  emit("update:modelValue", value);
  emit("input", e);
}

function handleFocus(e) {
  emit("focus", e);
}

function handleBlur(e) {
  emit("blur", e);
}
</script>

<style scoped>
.ctextarea {
  outline: none;
  border: none;
  background-color: var(--editor-color);
  border: 2px solid var(--second-color);
  padding: 4px 6px;
  font-size: 16px;
  border-radius: 5px;
  transition: border 0.2s ease, transform 0.2s ease;
  opacity: 80%;
}

.ctextarea:hover,
.ctextarea:focus {
  opacity: 100%;
}

.ctextarea:focus {
  border: 2px solid var(--main-color);
}
</style>
