<template>
  <div class="wrapper_person">
    <div class="person_information">
      <h1>
        Личный кабинет <b class="username"> {{ information.username }}</b>
      </h1>
      <div class="profile_wrapper">
        <NuxtImg :src="tempAvatar || 'test.jpg'" class="avatar" />
        <CButton class="btn" @click="triggerFileInput">
          Изменить аватарку
        </CButton>
        <CButton class="btn" @click="openModal">
          Изменить информацию о себе
        </CButton>
        <input
          type="file"
          accept="image/*"
          ref="fileInput"
          @change="handleFileChange"
          style="display: none"
        />
      </div>
      <WrapperModal v-if="isOpenModal" @closeModal="closeModal">
        <div class="edit_user_info">
          <h1>Изменить</h1>
          <div class="menu">
            <div
              class="tab"
              :class="{ active: curTab === 0 }"
              @click="changeTab(0)"
            >
              Информацию о себе
            </div>
            <div
              class="tab"
              :class="{ active: curTab === 1 }"
              @click="changeTab(1)"
            >
              Пароль
            </div>
          </div>
          <div class="user_info_form" v-if="curTab === 0">
            <p>Старый пароль</p>
            <CInput
              class="input"
              placeholder="Введите старый пароль"
              v-model="information.oldPassword"
              type="password"
            />
            <p>Логин</p>
            <CInput
              class="input"
              placeholder="Введите логин"
              v-model="information.username"
            />
            <p>Email</p>
            <CInput
              class="input"
              placeholder="Введите почту"
              v-model="information.email"
            />
            <p>Пол</p>
            <GenderToggle v-model="information.gender" />
          </div>
          <div class="password_form" v-else>
            <p>Старый пароль</p>
            <CInput
              class="input"
              placeholder="Введите старый пароль"
              v-model="information.oldPassword"
              type="password"
            />
            <p>Новый пароль</p>
            <CInput
              class="input"
              placeholder="Введите новый пароль"
              v-model="information.newPassword"
              type="password"
            />
            <p>Повторите новый пароль</p>
            <CInput
              class="input"
              placeholder="Повторите новый пароль"
              v-model="information.newPasswordRepeat"
              type="password"
            />
          </div>
          <CButton class="btn" @click="validation"> Сохранить </CButton>
        </div>
      </WrapperModal>
    </div>
    <div class="characters_information">
      <CharactesTabs />
    </div>
  </div>
</template>

<script setup>
import CharactesTabs from "~/components/profile/charactesTabs.vue";
import GenderToggle from "~/components/profile/genderToggle.vue";

const { $api } = useNuxtApp();
const information = ref({});
const isOpenModal = ref(false);
const selectedFile = ref(null);
const fileInput = ref(null);
const router = useRouter();
const curTab = ref(0);
const tempAvatar = ref(null);
const config = useRuntimeConfig();
const defaultUrl = config.public.backendUrl;

function openModal() {
  isOpenModal.value = true;
}
function closeModal() {
  isOpenModal.value = false;
}

function changeTab(newVal) {
  curTab.value = newVal;
}

function validation() {
  if (curTab.value === 1) {
    if (!information.value.oldPassword) {
      createNotification("Введите старый пароль!", "error");
      return;
    }
    if (!information.value.newPassword) {
      createNotification("Введите пароль!", "error");
      return;
    }
    if (!information.value.newPasswordRepeat) {
      createNotification("Повторите пароль!", "error");
      return;
    }
    if (information.value.newPassword < 8) {
      createNotification("Пароль должен быть больше 7 символов!", "error");
      return;
    }
    if (information.value.newPassword != information.value.newPasswordRepeat) {
      createNotification("Введенные пароли не совпадают!", "error");
      return;
    }
  } else {
    if (!information.value.username) {
      createNotification("Введите логин!", "error");
      return;
    }
    if (information.value.username.length < 5) {
      createNotification("Логин должен быть больше 4 символов!", "error");
      return;
    }
  }
  saveChange();
}

async function fetchData() {
  if (!localStorage.getItem("token")) router.push("/login");
  try {
    const responseInformation = await $api.get(`api/user/me`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    information.value = responseInformation.data;
    if (information.value.avatar_id)
      tempAvatar.value =
        defaultUrl + "/api/get_file?id=" + information.value.avatar_id;
  } catch (error) {
    console.error("Ошибка загрузки данных", error);
    createNotification(`${error.response.data.detail}`, "error");
  }
}

async function saveChange() {
  try {
    let data;
    if (curTab.value === 0)
      data = {
        old_password: information.value.oldPassword,
        username: information.value.username,
        email: information.value.email,
        gender: information.value.gender ? information.value.gender : "male",
      };
    else
      data = {
        old_password: information.value.oldPassword,
        new_password: information.value.newPassword,
      };
    const response = await $api.post(`api/user/edit_user_info`, data, {
      headers: {
        Accept: "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    createNotification("Изменения внесены!", "success");
  } catch (error) {
    console.error("Ошибка сохранения:", error);
    createNotification(`${error.response.data.detail}`, "error");
  }
}

function handleFileChange(event) {
  selectedFile.value = event.target.files[0];
  if (selectedFile.value) {
    uploadAvatar();
  }
}

async function uploadAvatar() {
  if (!selectedFile.value) {
    createNotification("Пожалуйста, выберите файл", "error");
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await $api.post(`api/user/avatar_update`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    createNotification("Аватар успешно загружен!", "success");
    tempAvatar.value =
      defaultUrl + "/api/get_file?id=" + response.data.avatar_id;
    updateAvatar(tempAvatar.value);
  } catch (error) {
    console.error("Ошибка загрузки аватара:", error);
    createNotification(`${error.response.data.detail}`, "error");
  }
}

function triggerFileInput() {
  if (fileInput.value) {
    fileInput.value.click();
  }
}

onMounted(() => {
  fetchData();
  fetch();
});

let createNotification;
let updateAvatar;

function fetch() {
  createNotification = inject("createNotification");
  updateAvatar = inject("updateAvatar");
}
</script>

<style scoped>
.username {
  color: var(--main-color);
  font-size: 28px;
}
.person_information {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 33%;
}
.characters_information {
  border-radius: 10px;
  display: flex;
  width: 67%;
}
.profile_wrapper {
  position: relative;
  display: inline-block;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
}
.btn {
  width: 250px;
  min-height: 45px;
}

.avatar {
  line-height: 0;
  display: inline-block;
  margin: 5px;
  border: 2px solid var(--main-color);
  border-radius: 50%;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
  transition: linear 0.25s;
  height: 256px;
  width: 256px;
  object-fit: cover;
}
.edit_user_info {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 80vw;
  max-width: 500px;
  justify-content: center;
  align-items: center;
}
.menu {
  width: 100%;
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.tab {
  box-sizing: border-box;
  background-color: var(--second-color);
  display: flex;
  align-items: center;
  justify-content: center;
  height: 60px;
  border-radius: 10px;
  flex: 1 1 0;
  cursor: pointer;
  user-select: none;
  border: 1px solid transparent;
  transition: border-color 0.3s;
}

.tab.active {
  border: 1px solid var(--main-color);
}
.password_form,
.user_info_form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
}
.input {
  padding: 5px;
  height: 45px;
}
.wrapper_person {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  flex: 1;
  width: 100%;
}

@media (max-width: 1000px) {
  .wrapper_person {
    flex-direction: column;
  }
  .characters_information {
    width: 100%;
  }
}
</style>
