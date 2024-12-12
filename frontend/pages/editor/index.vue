<template>
  <div class="editor_wrapper">
    <CButton class="create_btn" @click="openModal">
      Сохранить персонажа</CButton
    >
    <CharacterHeader
      v-model="mainPropertys"
      :imageFile="imageFile"
      @fileUpdate="fileUpdate"
    />
    <div class="character_body">
      <CharacterFirstColumn v-model="specifications" />
      <CharacterSecondColumn
        :vitality="vitality"
        :attacks="attacks"
        :equipment="equipment"
      />
      <CharacterThirdColumn v-model="personalityPropertys" :skills="skills" />
    </div>
  </div>
  <WrapperModal v-if="isOpenModal" @closeModal="closeModal">
    <CButton class="create_btn" @click="createCharacter">
      Сохранить на сайте</CButton
    >
    <CButton class="create_btn" @click="downloadCharacter">
      Сохранить как PDF</CButton
    >
  </WrapperModal>
</template>

<script setup>
import CharacterHeader from "~/components/editor/CharacterHeader.vue";
import CharacterThirdColumn from "~/components/editor/CharacterThirdColumn.vue";
import CharacterFirstColumn from "~/components/editor/CharacterFirstColumn.vue";
import CharacterSecondColumn from "~/components/editor/CharacterSecondColumn.vue";

const isOpenModal = ref(false);

function openModal() {
  isOpenModal.value = true;
}

function closeModal() {
  isOpenModal.value = false;
}
function createCharacter() {
  createNotification("Персонаж успешно сохранен в личном кабинете!", "success");
  closeModal();
  console.log(characterData.value);
}
function downloadCharacter() {
  createNotification("Персонаж успешно сохранен на устройстве!", "success");
  closeModal();
}
const mainPropertys = ref({
  namePlayer: "",
  nameCharacter: "",
  classCharacter: "",
  race: "",
  faith: "",
  age: "",
  level: "",
  expirience: "",
});
const imageFile = ref({});
const personalityPropertys = ref({
  weaknesses: [],
  ideals: [],
  characterTraits: [],
  attachments: [],
});
const skills = ref([]);
const vitality = ref([]);
const attacks = ref([]);
const equipment = ref({
  weapons: [],
  armor: [],
  items: [],
});
const specifications = ref({
  perception: 10,
  other: "",
  main: {
    strength: 0,
    agility: 0,
    physique: 0,
    intelligence: 0,
    wisdom: 0,
    charisma: 0,
  },
  inspiration: false,
  bonus: 0,
  savingThrows: {
    strength: 0,
    agility: 0,
    physique: 0,
    intelligence: 0,
    wisdom: 0,
    charisma: 0,
  },
  skills: {
    acrobatics: 0,
    analysis: 0,
    athletics: 0,
    perception: 0,
    survival: 0,
    performance: 0,
    intimidation: 0,
    history: 0,
    sleightOfHand: 0,
    magic: 0,
    medicine: 0,
    deception: 0,
    nature: 0,
    insight: 0,
    religion: 0,
    stealth: 0,
    persuasion: 0,
    animalHandling: 0,
  },
});
function fileUpdate(newValue) {
  imageFile.value = newValue;
}
const characterData = computed(() => {
  return {
    mainPropertys: mainPropertys.value,
    skills: skills.value,
    equipment: equipment.value,
    attacks: attacks.value,
    vitality: vitality.value,
    specifications: specifications.value,
    personalityPropertys: personalityPropertys.value,
  };
});

provide("fileUpdate", fileUpdate);
let createNotification;

function fetch() {
  createNotification = inject("createNotification");
}
onMounted(fetch);
</script>

<style scoped>
.editor_wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
}
.character_body {
  display: flex;
  gap: 20px;
  width: 100%;
}
@media screen and (max-width: 1400px) {
  .editor_wrapper {
    flex-direction: column;
  }

  .character_body {
    width: 100%;
    display: grid;
    grid-template: 2fr 1fr;
    gap: 20px;
  }
}
.create_btn {
  width: 250px;
  font-size: 18px;
  padding: 20px;
  background-color: var(--editor-color);
}
</style>
