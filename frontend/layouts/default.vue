<template>
  <Notification>
    <div class="fwh main_div">
      <Header />
      <div class="content">
        <slot></slot>
      </div>
      <Footer />
    </div>
  </Notification>
</template>

<script setup>
import Notification from "./notification.vue";
import Header from "./header.vue";
import Footer from "./footer.vue";
</script>

<style scoped>
.main_div {
  background: var(--bg-grad);
  width: 100%;
  min-height: 100vh;
}
.content {
  padding: calc(40px + var(--header-height)) 60px;
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: calc(100vh - 250px);
}
</style>
