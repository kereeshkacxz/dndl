<template>
  <div class="wrapper_equipment">
    <p>СНАРЯЖЕНИЕ</p>
    <div class="field_wrapper">
      <p>ОРУЖИЕ</p>
      <div class="field_items">
        <div class="field">
          <div
            v-for="(item, idx) in props.modelValue.weapons"
            :key="idx"
            class="item_item"
          >
            <div class="item_propertys">
              <div class="property">{{ item.name }}</div>
              <div class="property">{{ item.type }}</div>
              <div class="property">{{ item.damage }}</div>
              <div class="property">{{ item.bonus }}</div>
            </div>
            <div class="remove-button" @click="removeWeapon(idx)">X</div>
          </div>
        </div>
      </div>
      <div class="input_wrapper">
        <CInput
          placeholder="Название"
          v-model="nameWeapon"
          class="input_field"
        />
        <CInput placeholder="Тип" v-model="typeWeapon" class="input_field" />
        <CInput
          placeholder="Урон"
          v-model="damageWeapon"
          class="input_field"
          type="number"
        />
        <CInput placeholder="Бонус" v-model="bonusWeapon" class="input_field" />
        <CButton @click="addWeapon()">+</CButton>
      </div>
      <p>БРОНЯ</p>
      <div class="field_items">
        <div class="field">
          <div
            v-for="(item, idx) in props.modelValue.armor"
            :key="idx"
            class="item_item"
          >
            <div class="item_propertys">
              <div class="property">{{ item.name }}</div>
              <div class="property">{{ item.armorClass }}</div>
            </div>
            <div class="remove-button" @click="removeArmor(idx)">X</div>
          </div>
        </div>
      </div>
      <div class="input_wrapper">
        <CInput
          placeholder="Название"
          v-model="nameArmor"
          class="input_field"
        />
        <CInput placeholder="Класс" v-model="armorClass" class="input_field" />
        <CButton @click="addArmor()">+</CButton>
      </div>
      <p>ВЕЩИ</p>
      <div class="field_items">
        <div class="field">
          <div
            v-for="(item, idx) in props.modelValue.items"
            :key="idx"
            class="item_item"
          >
            <div class="item_propertys">
              <div class="property" :title="item.description">
                {{ item.name }}
              </div>
            </div>
            <div class="remove-button" @click="removeItem(idx)">X</div>
          </div>
        </div>
      </div>
      <div class="input_wrapper">
        <CInput placeholder="Название" v-model="nameItem" class="input_field" />
        <CInput
          placeholder="Описание"
          v-model="descriptionItem"
          class="input_field"
        />
        <CButton @click="addItem()">+</CButton>
      </div>
    </div>
  </div>
</template>

<script setup>
const nameWeapon = ref(null);
const typeWeapon = ref(null);
const damageWeapon = ref(null);
const bonusWeapon = ref(null);
const nameArmor = ref(null);
const armorClass = ref(null);
const nameItem = ref(null);
const descriptionItem = ref(null);

const props = defineProps({
  modelValue: { default: [] },
});
function addWeapon() {
  props.modelValue.weapons.push({
    name: nameWeapon.value,
    type: typeWeapon.value,
    damage: damageWeapon.value,
    bonus: bonusWeapon.value,
  });
  nameWeapon.value = "";
  typeWeapon.value = "";
  damageWeapon.value = "";
  bonusWeapon.value = "";
}

function removeWeapon(index) {
  props.modelValue.weapons.splice(index, 1);
}
function addArmor() {
  props.modelValue.armor.push({
    name: nameArmor.value,
    armorClass: armorClass.value,
  });
  nameArmor.value = "";
  armorClass.value = "";
}

function removeArmor(index) {
  props.modelValue.armor.splice(index, 1);
}
function addItem() {
  props.modelValue.items.push({
    name: nameItem.value,
    description: descriptionItem.value,
  });
  nameItem.value = "";
  descriptionItem.value = "";
}

function removeItem(index) {
  props.modelValue.items.splice(index, 1);
}
</script>

<style scoped>
.wrapper_equipment {
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
.field_items {
  display: flex;
  flex-direction: column;
  flex: 1;
  border: 2px solid white;
  padding: 20px;
  width: 100%;
  border-radius: 10px;
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
.item_item {
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
.item_propertys {
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
