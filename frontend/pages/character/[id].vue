<template>
  <div class="editor_wrapper">
    <CButton class="create_btn" @click="openModal">
      Сохранить персонажа</CButton
    >
    <CharacterHeader
      v-model="characters[idCharacter].mainPropertys"
      :imageFile="imageFile"
      @fileUpdate="fileUpdate"
    />
    <div class="character_body">
      <CharacterFirstColumn v-model="characters[idCharacter].specifications" />
      <CharacterSecondColumn
        :vitality="characters[idCharacter].vitality"
        :attacks="characters[idCharacter].attacks"
        :equipment="characters[idCharacter].equipment"
      />
      <CharacterThirdColumn
        v-model="characters[idCharacter].personalityPropertys"
        :skills="characters[idCharacter].skills"
      />
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
const route = useRoute();
const idCharacter = route.params.id;
const characters = ref({
  Guts: {
    image: "guts.jpg",
    mainPropertys: {
      namePlayer: "kereeshka",
      nameCharacter: "Guts",
      classCharacter: "Berserk",
      race: "Human",
      faith: "The God Hand",
      age: 21,
      level: 21,
      expirience: 21,
    },
    skills: [
      {
        name: "Berserker Rage",
        modifer: "+5",
      },
    ],
    equipment: {
      weapons: [
        {
          name: "Dragon Slayer",
          type: "Greatsword",
          damage: 50,
          bonus: "+10 to damage when raging",
        },
      ],
      armor: [
        {
          name: "Berserker Armor",
          armorClass: "15",
        },
      ],
      items: [
        {
          name: "Crossbow",
          description: "A powerful crossbow for ranged attacks.",
        },
        {
          name: "Crossbow Bolts",
          description: "Ammunition for the crossbow.",
        },
      ],
    },
    attacks: [
      {
        name: "Greatsword Slash",
        bonus: 10,
        damage: "2d6 + 10",
      },
      {
        name: "Crossbow Shot",
        bonus: 8,
        damage: "1d10 + 5",
      },
    ],
    vitality: {
      shield: 5,
      initiative: 3,
      speed: 30,
      hits: 100,
      tmp_hits: 20,
    },
    specifications: {
      perception: 15,
      other: "Berserker",
      main: {
        strength: 18,
        agility: 14,
        physique: 16,
        intelligence: 10,
        wisdom: 12,
        charisma: 8,
      },
      inspiration: false,
      bonus: 2,
      savingThrows: {
        strength: 5,
        agility: 3,
        physique: 4,
        intelligence: 1,
        wisdom: 2,
        charisma: 0,
      },
      skills: {
        acrobatics: 2,
        analysis: 1,
        athletics: 5,
        perception: 3,
        survival: 4,
        performance: 0,
        intimidation: 5,
        history: 1,
        sleightOfHand: 0,
        magic: 0,
        medicine: 1,
        deception: 0,
        nature: 1,
        insight: 2,
        religion: 0,
        stealth: 2,
        persuasion: 1,
        animalHandling: 2,
      },
    },
    personalityPropertys: {
      weaknesses: ["Impulsive", "Haunted by past", "Struggles with trust"],
      ideals: ["Strength", "Freedom", "Survival"],
      characterTraits: ["Determined", "Loyal", "Fierce"],
      attachments: ["Casca", "Friends from the Band of the Hawk"],
    },
  },
  Griffith: {
    image: "griffith.jpg",
    mainPropertys: {
      namePlayer: "kereeshka",
      nameCharacter: "Griffith",
      classCharacter: "Leader",
      race: "Human",
      faith: "The God Hand",
      age: 24,
      level: 24,
      expirience: 24,
    },
    skills: [
      {
        name: "Charismatic Leadership",
        modifer: "+6",
      },
    ],
    equipment: {
      weapons: [
        {
          name: "Sword of the Falcon",
          type: "Longsword",
          damage: 40,
          bonus: "+5 to attack rolls",
        },
      ],
      armor: [
        {
          name: "Falcon Armor",
          armorClass: "18",
        },
      ],
      items: [
        {
          name: "Falcon Pendant",
          description: "A symbol of Griffith's ambition and leadership.",
        },
        {
          name: "Healing Potion",
          description: "Restores 20 hit points.",
        },
      ],
    },
    attacks: [
      {
        name: "Sword Slash",
        bonus: 9,
        damage: "1d8 + 5",
      },
      {
        name: "Commanding Presence",
        bonus: 6,
        damage: "N/A",
      },
    ],
    vitality: {
      shield: 3,
      initiative: 4,
      speed: 30,
      hits: 80,
      tmp_hits: 10,
    },
    specifications: {
      perception: 18,
      other: "Strategist",
      main: {
        strength: 14,
        agility: 16,
        physique: 12,
        intelligence: 18,
        wisdom: 14,
        charisma: 20,
      },
      inspiration: true,
      bonus: 3,
      savingThrows: {
        strength: 2,
        agility: 4,
        physique: 1,
        intelligence: 6,
        wisdom: 3,
        charisma: 5,
      },
      skills: {
        acrobatics: 3,
        analysis: 5,
        athletics: 2,
        perception: 4,
        survival: 2,
        performance: 6,
        intimidation: 4,
        history: 5,
        sleightOfHand: 1,
        magic: 0,
        medicine: 1,
        deception: 5,
        nature: 2,
        insight: 4,
        religion: 1,
        stealth: 3,
        persuasion: 6,
        animalHandling: 1,
      },
    },
    personalityPropertys: {
      weaknesses: ["Ambitious to a fault", "Manipulative", "Cold"],
      ideals: ["Ambition", "Power", "Destiny"],
      characterTraits: ["Charismatic", "Strategic", "Visionary"],
      attachments: ["The Band of the Hawk", "Casca"],
    },
  },
});
const imageFile = ref(null);
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
