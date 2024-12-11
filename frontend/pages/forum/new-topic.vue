<template>
	<div class="wrapper">
		<div class="wrapper-input">
			<p class="field">Название</p>
			<textarea class="name" placeholder="Название топика..."></textarea>
		</div>
		<div class="wrapper-input">
			<p class="field">Описание</p>
			<textarea class="description" placeholder="Описание топика..."></textarea>
		</div>
		<CButton class="btn_login" @click="validation">Создать топик</CButton>
	</div>
</template>

<script setup></script>

<style scoped>
.wrapper{
	display: flex;
	flex-direction: column;
	gap: 20px;
}
.field{
	user-select: none;
  font-size: 30px;
  color: var(--main-color);
}
.wrapper-input {
	display: flex;
	flex-direction: column;
	align-items: start;
	gap: 10px;
}
.name {
	width: 30vw;
	min-width: 220px;
  height: 140px;
	outline: none;
  border: none;
  background-color: var(--editor-color);
  border: 2px solid var(--second-color);
  padding: 4px 6px;
  font-size: 16px;
  border-radius: 5px;
  transition: border 0.2s ease, transform 0.2s ease;
  opacity: 80%;
}
.description {
	width: 40vw;
	min-width: 320px;
  height: 250px;
	outline: none;
  border: none;
  background-color: var(--editor-color);
  border: 2px solid var(--second-color);
  padding: 4px 6px;
  font-size: 16px;
  border-radius: 5px;
  transition: border 0.2s ease, transform 0.2s ease;
  opacity: 80%;
}
</style>