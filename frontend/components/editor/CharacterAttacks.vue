<template>
  <div class="wrapper_attacks">
    <p>АТАКИ И ЗАКЛИНАНИЯ</p>
    <div class="field_wrapper">
      <div class="field_attacks">
        <div class="field">
          <div
            v-for="(attack, idx) in props.modelValue"
            :key="idx"
            class="attack_item"
          >
            <div class="attack_propertys">
              <div class="property">{{ attack.name }}</div>
              <div class="property">{{ attack.bonus }}</div>
              <div class="property">{{ attack.damage }}</div>
            </div>
            <div class="remove-button" @click="removeAttack(idx)">X</div>
          </div>
        </div>
      </div>
      <div class="input_wrapper">
        <CInput placeholder="Название" v-model="name" class="input_field" />
        <CInput
          placeholder="Бонус атаки"
          v-model="bonus"
          class="input_field"
          type="number"
        />
        <CInput placeholder="Урон/Вид" v-model="damage" class="input_field" />
        <CButton @click="addAttack()">+</CButton>
      </div>
    </div>
  </div>
</template>

<script setup>
const name = ref(null);
const bonus = ref(null);
const damage = ref(null);

const props = defineProps({
  modelValue: { default: [] },
});
function addAttack() {
  props.modelValue.push({
    bonus: bonus.value,
    name: name.value,
    damage: damage.value,
  });
  damage.value = "";
  name.value = "";
  bonus.value = "";
}

function removeAttack(index) {
  props.modelValue.splice(index, 1);
}
</script>

<style scoped>
.wrapper_attacks {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--main-color);
  gap: 10px;
  padding: 20px;
  background-color: var(--editor-color);
  width: 100%;
  align-items: center;
  flex: 1;
}
.field_attacks {
  display: flex;
  flex-direction: column;
  flex: 1;
  border: 2px solid white;
  padding: 20px;
  width: 100%;
  border-radius: 10px;
  min-height: 300px;
}
.field_wrapper {
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: 5px;
  width: 100%;
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
.attack_item {
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
.attack_propertys {
  display: flex;
  flex: 1;
}
.property {
  flex: 1;
}
.field {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
