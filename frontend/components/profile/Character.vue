<template>
  <div class="character_wrapper">
    <NuxtImg :src="props.character.image" class="image_character" preload />
    <p>
      Character :
      <span class="main_color">{{
        character.mainPropertys.nameCharacter
      }}</span>
    </p>
    <p>
      Player :
      <span class="main_color">{{ character.mainPropertys.namePlayer }}</span>
    </p>
    <p>
      Race :
      <span class="main_color">{{ character.mainPropertys.race }}</span>
    </p>
    <p>
      Age : <span class="main_color">{{ character.mainPropertys.age }}</span>
    </p>
    <p>
      Level :
      <span class="main_color">{{ character.mainPropertys.level }}</span>
    </p>
    <div class="btn_wrapper">
      <CButton
        @click="
          router.push(
            `/character/${props.character.mainPropertys.nameCharacter}`
          )
        "
      >
        {{ curTab === 0 ? "Редактировать" : "Просмотреть" }}
      </CButton>
      <CButton @click="openModal"> Удалить </CButton>
    </div>
  </div>
  <WrapperModal v-if="isOpenModal" @closeModal="closeModal">
    <div class="wrapper_modal">
      <h2>Вы подтверждаете удаление?</h2>
      <div class="btn_wrapper">
        <CButton @click="closeModal"> Отмена </CButton>
        <CButton @click="deleteCharacter"> Удалить </CButton>
      </div>
    </div>
  </WrapperModal>
</template>

<script setup>
const props = defineProps({
  character: { default: {} },
  curTab: { default: 0 },
});
const isOpenModal = ref(false);
const router = useRouter();
function closeModal() {
  isOpenModal.value = false;
}

function openModal() {
  isOpenModal.value = true;
}

function deleteCharacter() {
  createNotification("Персонаж успешно удален!", "success");
  closeModal();
}
onMounted(() => {
  fetch();
});

let createNotification;

function fetch() {
  createNotification = inject("createNotification");
}
</script>

<style scoped>
.main_color {
  color: var(--main-color);
}
.character_wrapper {
  background-color: var(--editor-color);
  padding: 10px;
  border: 1px solid var(--main-color);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.image_character {
  aspect-ratio: 1/1;
  height: 256px;
  width: 256px;
  border: 2px solid white;
  border-radius: 10px;
}
.btn_wrapper {
  display: flex;
  gap: 20px;
  justify-content: center;
}
.wrapper_modal {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
}
</style>
