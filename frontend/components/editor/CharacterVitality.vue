<template>
  <div class="vitality_wrapper">
    <div class="images">
      <div class="shield">
        <CInput
          class="input_shield"
          type="number"
          v-model="modelValue.shield"
        />
        <NuxtImg src="shield.png" class="shield_image" />
      </div>
      <div class="parametr">
        <CInput
          class="input_parametr"
          type="number"
          v-model="modelValue.initiative"
        />
        ИНИЦИАТИВА
      </div>
      <div class="parametr">
        <CInput
          class="input_parametr"
          type="number"
          v-model="modelValue.speed"
        />
        СКОРОСТЬ
      </div>
    </div>
    <div class="hit_wrapper">
      <CInput class="hit_input" type="number" v-model="modelValue.hits" />
      <p>ТЕКУЩИЕ ХИТЫ</p>
    </div>
    <div class="hit_wrapper">
      <CInput class="hit_input" type="number" v-model="modelValue.tmp_hits" />
      <p>ВРЕМЕННЫЕ ХИТЫ</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { default: {}, type: Object },
});
</script>

<style scoped>
.vitality_wrapper {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--main-color);
  gap: 10px;
  padding: 20px;
  background-color: var(--editor-color);
  width: 100%;
  align-items: center;
}
.images {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}
.parametr {
  border: 2px solid white;
  border-radius: 10px;
  aspect-ratio: 1/1;
  height: 100px;
  font-size: 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 15px;
}
.shield_image {
  aspect-ratio: 1/1;
  height: 100px;
}
.shield {
  width: 100px;
  position: relative;
}
.input_parametr {
  width: 100%;
  text-align: center;
}
.input_shield {
  position: absolute;
  top: 25px;
  left: 25px;
  width: 50px;
  text-align: center;
}
.hit_wrapper {
  display: flex;
  flex-direction: column;
  gap: 10px;
  border-radius: 10px;
  border: 2px solid white;
  padding: 20px;
  width: 100%;
}
.hit_input {
  width: 100%;
  font-size: 30px;
  padding: 20px;
  text-align: center;
}
@media screen and (max-width: 430px) {
  .parametr {
    width: 80px;
  }
  .shield_image {
    width: 80px;
    height: 80px;
  }
  .shield {
    width: 80px;
  }
  .input_shield {
    width: 40px;
    left: 20px;
  }
  .images {
    gap: 5px;
  }
}
</style>
