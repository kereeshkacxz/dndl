<template>
    <div class="wrapper">
			<div class="wrapper-topic">
					<h1 class="title">How to make a best character</h1>
					<p class="description">Offer your options, how to write the best character, ideas, tell us your experience</p>
			</div>
			<div class="send-comment">
				<textarea class="text-comment" placeholder="Some comment..."></textarea>
				<button class="send-btn">Send comment</button>
			</div>
			<div class="wrapper-comment">
				<h1>Comments</h1>
					<div v-for="(message, id) in messages"
					:key="id" class="comment">
					<NuxtImg :src="tempAvatar || 'test.jpg'" class="avatar" />
					{{ message }}
			</div>
			</div>
    </div>
</template>

<script setup>
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
document.querySelectorAll('textarea').forEach(el => {
    el.style.height = el.setAttribute('style', 'height: ' + el.scrollHeight + 'px');
    el.classList.add('auto');
    el.addEventListener('input', e => {
        el.style.height = 'auto';
        el.style.height = (el.scrollHeight) + 'px';
    });
});
</script>

<style scoped>
.wrapper{
    display: flex;
    flex-direction: column;
}
.wrapper-topic{
	display: flex;
	flex-direction: column;
	align-items: start;
	gap: 10px;
}
.description {
	text-align: left;
}
.title {
	text-align: left;
}
.send-comment{
	display: flex;
	flex-direction: column;
	align-items: start;
	gap: 20px;
	margin-top: 20px;
	margin-bottom: 20px;
}
.text-comment{
	width: 100%;
  height: 150px;
  padding: 12px 20px;
  box-sizing: border-box;
  border-radius: 4px;
	background-color: var(--editor-color);
  border: 2px solid var(--second-color);
  font-size: 16px;
  resize: none;
	color: white;
	border-radius: 10px;
}
.send-btn {
  background-color: #ffd585; 
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
	font-weight: bold;
  cursor: pointer; 
  transition: background-color 0.3s; 
	border-radius: 10px;
}
.send-btn:hover {
  background-color: #e6b86a; 
}
.wrapper-comment {
	display: flex;
	flex-direction: column;
	align-items: start;
	gap: 20px;
}
.comment {
	display: flex;
  text-align: left;
	align-items: center;
	padding: 20px;
  width: 540px;
  min-width: 300px;
	border: 2px solid black;
	gap: 20px;
	border-radius: 10px;
	background-color: rgba(105, 105, 105, 0.5);
	box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
}
.avatar {
  line-height: 0;
  display: inline-block;
  margin: 5px;
  border: 2px solid var(--main-color);
  border-radius: 50%;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
  transition: linear 0.25s;
  height: 76px;
  width: 76px;
  object-fit: cover;
}
@media (max-width: 600px) {
    .comment {
        width: 300px; 
    }
}
</style>