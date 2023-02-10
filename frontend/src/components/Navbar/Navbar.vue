<script setup>
import OnlineIcon from './OnlineIcon.vue'
</script>

<template>
  <va-navbar color="primary" class="mb-2">
    <template #left>
      <va-navbar-item class="logo">Home dashboard</va-navbar-item>
    </template>
    <template #right>
      <va-navbar-item>
        <OnlineIcon />
      </va-navbar-item>
    </template>
  </va-navbar>
</template>

<script>
  export default {

  }
</script>

<style scoped>
.logo {
  font-weight: 600;
  font-size: 1.5rem;
}
</style>
