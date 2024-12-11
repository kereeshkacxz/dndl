<template>
	<div class="wrapper">
		<ul class="topics_list">
			<li
				v-for="(message, id) in messages"
				:key="id"
			>
				<NuxtLink 
				:to="`/forum/${id}`"
				class="link_to_topic">{{ message }}</NuxtLink>
			</li>
		</ul>
		<NuxtLink
		:to="`forum/new-topic`"
		class="new_topic fc">NEW</NuxtLink>
	</div>
</template>

<script setup>
const { $api } = useNuxtApp();

const messages = [
  "How to make a best character",
  "Why am I drawing a prototype again, I'm a backender",
  "I'm too lazy, it will be stupid to list all the forums",
  "How to make a best character",
  "Why am I drawing a prototype again, I'm a backender",
  "I'm too lazy, it will be stupid to list all the forums",
  "How to make a best character",
  "Why am I drawing a prototype again, I'm a backender",
  "I'm too lazy, it will be stupid to list all the forums"
];

// async function fetchData() {
//   if (!localStorage.getItem("token")) router.push("/login");
//   try {
//     const responseInformation = await $api.get(`api/user/me`, {
//       headers: {
//         "Content-Type": "application/json",
//         Authorization: `Bearer ${localStorage.getItem("token")}`,
//       },
//     });
//     information.value = responseInformation.data;
//     if (information.value.avatar_id)
//       tempAvatar.value =
//         defaultUrl + "/api/get_file?id=" + information.value.avatar_id;
//   } catch (error) {
//     console.error("Ошибка загрузки данных", error);
//     createNotification(`${error.response.data.detail}`, "error");
//   }
// }

onMounted(() => {
  // fetchData();
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

.wrapper{
	display: flex;
	align-items: start;
}

.new_topic{
	/* margin-top: -50px; */
	line-height: 34%;
	text-decoration: none; 
  font-size: 100px; 
  transition: color 0.3s; 
}
.new_topic:hover {
	color: #ffd585;
}

.topics_list{
	display: flex;
	flex-direction: column;
	gap: 20px;
	align-items: start;
	font-size: 30px;
	margin-right: 200px;
}
.link_to_topic{
	text-decoration: none; 
  font-size: 30px; 
  transition: color 0.3s; 
}
.link_to_topic:hover {
	color: #ffd585;
}
</style>
