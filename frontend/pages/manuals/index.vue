<template>
  <div class="list-manuals">
    <div
      v-for="(message, id) in generatedDictionary"
      :key="id"
      class="manual-wrapper"
    >
      <div :class="['manual', { official: message.official }]">
        <h2 class="title">{{ message.title }}</h2>
        <p class="description">{{ message.description }}</p>
				<a :href="message.filePath" download>
        	<NuxtImg :src="'pdf.png'" class="avatar" />
      	</a>
        <p class="createdAt">Created At: {{ formatDate(message.createdAt) }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
function generateRandomDate() {
  const start = new Date(2020, 0, 1);
  const end = new Date();
  return new Date(
    start.getTime() + Math.random() * (end.getTime() - start.getTime())
  );
}

function generateRandomBoolean() {
  return Math.random() < 0.5;
}

function generateDictionary() {
  const dictionary = [];
  for (let i = 1; i <= 10; i++) {
    const obj = {
      title: `Title ${i}`,
      description: `Description for item ${i} dassda dasdsadas dasdsadas dasdsadas dasdsadas dasdsadas`,
      filePath: `path/to/file${i}.txt`,
      createdAt: generateRandomDate().toISOString(),
      official: generateRandomBoolean(),
    };
    dictionary.push(obj);
  }
  return dictionary;
}

function formatDate(dateString) {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

const generatedDictionary = generateDictionary();
</script>

<style scoped>
.list-manuals {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
}

.manual {
  display: flex;
  flex-direction: column;
  gap: 13px;
  width: 500px;
  height: 300px;
  text-decoration: none;
  padding: 30px;
  border: 2px solid black;
  border-radius: 10px;
  background-color: rgba(105, 105, 105, 0.6);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
  transition: background-color 0.5s;
  position: relative;
}

.title {
  color: var(--main-color);
  text-align: center;
}

.description {
  color: lightgray;
}

.createdAt {
  position: absolute;
  bottom: 30px;
  right: 30px;
}

.manual.official {
  border-color: var(--main-color);
}
@media (max-width: 570px) {
	.manual {
		width: 310px; /* Устанавливаем ширину для экранов 570px и меньше */
		height: 340px;
	}
}
.avatar{
	width: 80px;
	transition: transform 0.3s ease;
}
.avatar:hover {
  transform: scale(1.1); /* Увеличение изображения при наведении */
}
</style>
