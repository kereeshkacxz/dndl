<template>
  <div class="tabs_wrapper">
    <div class="tabs_menu">
      <div class="tab" :class="{ active: curTab === 0 }" @click="changeTab(0)">
        Мои персонажи
      </div>
      <div class="tab" :class="{ active: curTab === 1 }" @click="changeTab(1)">
        Доступные персонажи
      </div>
      <div
        class="tab"
        :class="{ active: curTab === 2 }"
        v-if="isAdmin"
        @click="changeTab(2)"
      >
        Все персонажи
      </div>
      <CSelectableList
        class="selectable"
        :items="tabs"
        :curIdx="curTab"
        @changeIndex="(i) => (curTab = i)"
      />
    </div>
    <div class="characters_wrapper">
      <Character
        v-for="(character, idx) in curTab === 0
          ? characters
          : characters.slice(3, 5)"
        :character="character"
        :key="idx"
        :curTab="curTab"
      />
    </div>
  </div>
</template>

<script setup>
import Character from "./Character.vue";
const isAdmin = ref(localStorage.getItem("admin") === "true");
const curTab = ref(0);

function changeTab(newValue) {
  curTab.value = newValue;
}
const characters = [
  {
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
    skills: {
      name: "Berserker Rage",
      modifier: "+5",
    },
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
  {
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
    skills: {
      name: "Charismatic Leadership",
      modifier: "+6",
    },
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
  {
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
    skills: {
      name: "Berserker Rage",
      modifier: "+5",
    },
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
  {
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
    skills: {
      name: "Charismatic Leadership",
      modifier: "+6",
    },
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
  {
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
    skills: {
      name: "Berserker Rage",
      modifier: "+5",
    },
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
  {
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
    skills: {
      name: "Charismatic Leadership",
      modifier: "+6",
    },
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
];
const tabs = isAdmin.value
  ? ["Мои персонажи", "Доступные персонажи", "Все персонажи"]
  : ["Мои персонажи", "Доступные персонажи"];
</script>

<style scoped>
.tabs_wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  height: 700px;
  background-color: rgb(32, 32, 32);
  border-radius: 10px;
  border: 1px solid var(--main-color);
  flex-direction: column;
  flex: 1;
}
.tabs_menu {
  padding: 10px;
  display: flex;
  gap: 20px;
  width: 100%;
  border-bottom: 1px solid var(--main-color);
  height: 80px;
}
.tab {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--second-color);
  height: 60px;
  border-radius: 5px;
  user-select: none;
  cursor: pointer;
  padding: 10px;
  border: 1px solid transparent;
  transition: all 0.3s;
}
.tab.active {
  border: 1px solid var(--main-color);
}
.characters_wrapper {
  flex: 1;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;
  background-color: var(--second-color);
  display: flex;
  padding: 20px;
  gap: 20px;
  overflow-x: scroll;
  width: 100%;
  margin-bottom: 5px;
}
.selectable {
  display: none;
}
@media (max-width: 500px) {
  .selectable {
    display: block;
  }
  .tab {
    display: none;
  }
  .characters_wrapper {
    border-radius: 10px;
  }
  .tabs_menu {
    height: 60px;
  }
}
</style>
