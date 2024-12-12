<template>
  <div class="header_chcaracter">
    <div class="name_and_image">
      <ImageUploader />
    </div>
    <div class="main_propertys">
      <div class="string_property">
        <div class="two">
          <div class="input_with_name">
            <CInput v-model="modelValue.classCharacter" />
            <p class="name_property">КЛАСС</p>
          </div>
          <div class="input_with_name">
            <CInput v-model="modelValue.age" />
            <p class="name_property">ВОЗРАСТ</p>
          </div>
        </div>
        <div class="input_with_name one">
          <CInput v-model="modelValue.namePlayer" />
          <p class="name_property">ИМЯ ИГРОКА</p>
        </div>
      </div>
      <div class="string_property">
        <div class="two">
          <div class="input_with_name">
            <CInput v-model="modelValue.race" />
            <p class="name_property">РАСА</p>
          </div>
          <div class="input_with_name">
            <CInput v-model="modelValue.faith" />
            <p class="name_property">ВЕРА</p>
          </div>
        </div>
        <div class="input_with_name one">
          <CInput v-model="modelValue.expirience" />
          <p class="name_property">ОПЫТ</p>
        </div>
      </div>
      <div class="string_property">
        <div class="two">
          <div class="input_with_name">
            <CInput v-model="modelValue.nameCharacter" />
            <p class="name_property">ИМЯ ПЕРСОНАЖА</p>
          </div>
        </div>
        <div class="input_with_name one">
          <CInput v-model="modelValue.level" type="number" />
          <p class="name_property">УРОВЕНЬ</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import ImageUploader from "./ImageUploader.vue";

const props = defineProps({
  modelValue: { default: {}, type: Object },
  imageFile: { required: true },
});

const emit = defineEmits(["update:modelValue"]);
</script>

<style scoped>
.name_and_image {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.header_chcaracter {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
}
.input_with_name {
  display: flex;
  flex-direction: column-reverse;
  text-align: left;
  gap: 2px;
  width: 100%;
}
.name_property {
  padding-left: 15px;
  font-size: 14px;
  width: 100%;
  user-select: none;
}
.string_property {
  display: flex;
  gap: 10px;
}

.main_propertys {
  height: 220px;
  border: 1px solid var(--main-color);
  padding: 5px 20px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1 1 0%;
}
.two {
  display: flex;
  gap: 10px;
  flex: 2;
}
.one {
  flex: 1;
}
@media (max-width: 900px) {
  .string_property {
    flex-wrap: wrap;
  }
  .main_propertys {
    height: fit-content;
  }
}
@media (max-width: 700px) {
  .two {
    flex-wrap: wrap;
    width: 100%;
  }
}
@media (max-width: 500px) {
  .header_chcaracter {
    flex-direction: column;
  }
}
</style>
