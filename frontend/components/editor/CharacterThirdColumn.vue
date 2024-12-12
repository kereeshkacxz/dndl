<template>
  <div class="column_wrapper">
    <div class="name_with_field" v-for="(item, index) in fields" :key="index">
      <p class="name">{{ item.title }}</p>
      <div class="field_wrapper">
        <div class="container">
          <div class="field">
            <div
              v-for="(entry, idx) in item.entries"
              :key="idx"
              class="field_item"
            >
              {{ entry }}
              <div class="remove-button" @click="removeEntry(index, idx)">
                X
              </div>
            </div>
          </div>
        </div>

        <div class="input_wrapper">
          <CInput
            placeholder="Добавить элемент"
            v-model="item.newEntry"
            class="input_field"
          />
          <CButton @click="addEntry(index)">+</CButton>
        </div>
      </div>
    </div>
    <div class="name_with_field" style="flex: 1">
      <p class="name">УМЕНИЯ И СПОСОБНОСТИ</p>
      <div class="skill_wrapper">
        <div class="skill_field">
          <div class="field">
            <div
              v-for="(skill, idx) in props.skills"
              :key="idx"
              class="skill_item"
            >
              <span
                >{{ skill.name }} /
                <span style="color: var(--main-color)">{{
                  skill.modifer
                }}</span></span
              >
              <div class="remove-button" @click="removeSkill(idx)">X</div>
            </div>
          </div>
        </div>
        <div class="input_wrapper">
          <CInput placeholder="Имя" v-model="name" class="input_field" />
          <CInput
            placeholder="Модификатор"
            v-model="modifer"
            class="input_field"
          />
          <CButton @click="addSkill()">+</CButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { default: {}, type: Object },
  skills: { default: [] },
});
const modifer = ref("");
const name = ref("");

const fields = ref([
  {
    title: "ЧЕРТЫ ХАРАКТЕРА",
    entries: props.modelValue.characterTraits,
    newEntry: "",
  },
  { title: "ИДЕАЛЫ", entries: props.modelValue.ideals, newEntry: "" },
  {
    title: "ПРИВЯЗАННОСТИ",
    entries: props.modelValue.attachments,
    newEntry: "",
  },
  { title: "СЛАБОСТИ", entries: props.modelValue.weaknesses, newEntry: "" },
]);

function addEntry(index) {
  if (fields.value[index].newEntry.trim() !== "") {
    fields.value[index].entries.push(fields.value[index].newEntry.trim());
    fields.value[index].newEntry = "";
  }
}

function removeEntry(fieldIndex, entryIndex) {
  fields.value[fieldIndex].entries.splice(entryIndex, 1);
}

function addSkill() {
  props.skills.push({ modifer: modifer.value, name: name.value });
  modifer.value = "";
  name.value = "";
}

function removeSkill(index) {
  props.skills.splice(index, 1);
}
</script>

<style scoped>
.column_wrapper {
  display: flex;
  flex: 1;
  padding: 20px;
  gap: 10px;
  flex-direction: column;
  border: 1px solid var(--main-color);
  width: 100%;
}
.name_with_field {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.name {
  user-select: none;
}
.field_wrapper {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.container {
  background-color: var(--editor-color);
  height: 200px;
  border: 2px solid white;
  border-radius: 8px;
}
.field {
  display: flex;
  flex-wrap: wrap;
  padding: 10px;
  width: 100%;
  gap: 10px;
}
.field_item {
  padding: 2px;
  background-color: var(--second-color);
  width: fit-content;
  padding: 10px;
  border-radius: 5px;
  height: fit-content;
  display: flex;
  justify-content: center;
  align-items: center;
}
.input_wrapper {
  display: flex;
  gap: 5px;
  width: 100%;
}
.input_field {
  width: 100%;
  flex: 1;
  padding: 2px;
}
.input_field:focus {
  outline: 1px solid var(--main-color);
}
.remove-button {
  color: var(--unsuccess-color);
  background: none;
  font-weight: 900;
  border: none;
  cursor: pointer;
  margin-left: 8px;
  font-size: 20px;
  transition: all 0.3s;
}

.remove-button:hover {
  opacity: 0.5;
  transform: scale(1.1);
}
.skill_wrapper {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}
.skill_field {
  background-color: var(--editor-color);
  min-height: 600px;
  border: 2px solid white;
  border-radius: 8px;
  flex: 1;
}
.skill_item {
  width: 100%;
  padding: 2px;
  background-color: var(--second-color);
  padding: 10px;
  border-radius: 5px;
  height: fit-content;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
