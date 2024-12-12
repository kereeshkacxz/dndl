<template>
  <div class="image_wrapper">
    <NuxtImg
      :src="file ? filePath : 'test.jpg'"
      class="image"
      @click="fileInput.click()"
      preload
    />
    <input
      type="file"
      ref="fileInput"
      @change="handleImageChange"
      accept="image/*"
      style="display: none"
    />
  </div>
</template>

<script setup>
const image = ref(null);
const fileInput = ref(null);
const file = ref(null);
const filePath = computed(() => {
  return URL.createObjectURL(file.value);
});

const handleImageChange = (event) => {
  const newFile = event.target.files[0];
  if (newFile) {
    const reader = new FileReader();
    reader.onloadend = () => {
      image.value = reader.result;
    };
    reader.readAsDataURL(newFile);
  }
  file.value = newFile;
  fileUpdate(newFile);
};
let fileUpdate;
onMounted(() => {
  fileUpdate = inject("fileUpdate");
});
</script>

<style scoped>
.image_wrapper {
  display: flex;
  position: relative;
  border: 1px solid var(--main-color);
}
.image {
  aspect-ratio: 1/1;
  height: 220px;
  object-fit: cover;
  cursor: pointer;
}
</style>
