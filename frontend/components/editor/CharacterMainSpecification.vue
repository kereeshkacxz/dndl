<template>
  <div class="wrapper_specification">
    <div class="left_specification">
      <div class="spec">
        <p>СИЛА</p>
        <CInput
          class="hit_input"
          type="number"
          v-model="props.modelValue.main.strength"
        />
      </div>
      <div class="spec">
        <p>ЛОВКОСТЬ</p>
        <CInput
          class="hit_input"
          type="number"
          v-model="props.modelValue.main.agility"
        />
      </div>
      <div class="spec">
        <p>ТЕЛОСЛОЖЕНИЕ</p>
        <CInput
          class="hit_input"
          type="number"
          v-model="props.modelValue.main.physique"
        />
      </div>
      <div class="spec">
        <p>ИНТЕЛЛЕКТ</p>
        <CInput
          class="hit_input"
          type="number"
          v-model="props.modelValue.main.intelligence"
        />
      </div>
      <div class="spec">
        <p>МУДРОСТЬ</p>
        <CInput
          class="hit_input"
          type="number"
          v-model="props.modelValue.main.wisdom"
        />
      </div>
      <div class="spec">
        <p>ХАРИЗМА</p>
        <CInput
          class="hit_input"
          type="number"
          v-model="props.modelValue.main.charisma"
        />
      </div>
    </div>
    <div class="right_specification">
      <div class="inspiration">
        <NuxtImg
          src="inspiration.png"
          class="inspiration_image"
          @click="toggleInspiration"
          v-show="props.modelValue.inspiration"
          preload
        />
        <div
          v-show="!props.modelValue.inspiration"
          @click="toggleInspiration"
          class="inspiration_not_image"
        ></div>
        <p class="inspiration_title">ВДОХНОВЕНИЕ</p>
      </div>
      <div class="inspiration">
        <div class="inspiration_not_image">
          <CInput
            v-model="props.modelValue.bonus"
            class="bonus_input"
            type="number"
          />
        </div>
        <p class="inspiration_title">БОНУС ВЛАДЕНИЯ</p>
      </div>
      <div class="saving_throws">
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.savingThrows.strength"
          />
          <p>Сила</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.savingThrows.agility"
          />
          <p>Ловкость</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.savingThrows.physique"
          />
          <p>Телосложение</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.savingThrows.intelligence"
          />
          <p>Интеллект</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.savingThrows.wisdom"
          />
          <p>Мудрость</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.savingThrows.charisma"
          />
          <p>Харизма</p>
        </div>
      </div>
      <div class="skills">
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.acrobatics"
          />
          <p>Акробатика</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.analysis"
          />
          <p>Анализ</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.athletics"
          />
          <p>Атлетика</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.perception"
          />
          <p>Восприятие</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.survival"
          />
          <p>Выживание</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.performance"
          />
          <p>Выступление</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.intimidation"
          />
          <p>Запугивание</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.history"
          />
          <p>История</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.sleightOfHand"
          />
          <p>Ловкость рук</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.magic"
          />
          <p>Магия</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.medicine"
          />
          <p>Медицина</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.deception"
          />
          <p>Обман</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.nature"
          />
          <p>Природа</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.insight"
          />
          <p>Проницательность</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.religion"
          />
          <p>Религия</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.stealth"
          />
          <p>Скрытность</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.persuasion"
          />
          <p>Убеждение</p>
        </div>
        <div class="throw">
          <CInput
            class="throw_input"
            type="number"
            v-model="props.modelValue.skills.animalHandling"
          />
          <p>Уход за животными</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { default: {} },
});
function toggleInspiration() {
  props.modelValue.inspiration = !props.modelValue.inspiration;
}
</script>

<style scoped>
.skills {
  display: flex;
  padding: 10px;
  flex-direction: column;
  background-color: var(--editor-color);
  height: fit-content;
  border-radius: 10px;
  border: 2px solid white;
  gap: 10px;
  min-width: 259px;
  width: 100%;
}
.throw_input {
  width: 50px;
}
.throw {
  display: flex;
  gap: 10px;
}
.saving_throws {
  display: flex;
  padding: 10px;
  flex-direction: column;
  background-color: var(--editor-color);
  width: 100%;
  height: fit-content;
  border-radius: 10px;
  border: 2px solid white;
  gap: 10px;
}
.wrapper_specification {
  display: flex;
  gap: 20px;
}
.left_specification {
  display: flex;
  flex-direction: column;
  padding: 60px 20px;
  background-color: var(--editor-color);
  border-radius: 60px;
  gap: 30px;
  width: 220px;
  border: 1px solid var(--main-color);
}
.spec {
  border-radius: 10px;
  border: 2px solid white;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
.hit_input {
  width: 100px;
  font-size: 30px;
  padding: 20px;
  text-align: center;
}
.inspiration {
  display: flex;
  align-items: center;
  justify-content: center;
}
.right_specification {
  display: flex;
  flex-direction: column;
  flex: 1;
  gap: 20px;
  border: 1px solid var(--main-color);
  padding: 20px;
}
.inspiration_image {
  aspect-ratio: 1/1;
  background-color: var(--editor-color);
  border: 2px solid white;
  border-radius: 10px;
  padding: 5px;
  height: 62px;
  cursor: pointer;
  user-select: none;
}
.inspiration_title {
  background-color: var(--editor-color);
  padding: 10px;
  border: 2px solid white;
  flex: 1;
  border-radius: 10px;
  height: fit-content;
}
.inspiration_not_image {
  aspect-ratio: 1/1;
  background-color: var(--editor-color);
  border: 2px solid white;
  border-radius: 10px;
  padding: 5px;
  height: 62px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.bonus_input {
  border-radius: 10px;
  height: 50px;
  width: 50px;
  text-align: center;
  font-size: 25px;
}
@media screen and (max-width: 660px) {
  .wrapper_specification {
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .right_specification {
    width: 100%;
  }
}
</style>
