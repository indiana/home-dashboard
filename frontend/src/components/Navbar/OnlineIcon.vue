<template>
  <va-icon v-if="online" name="sync" hint="online" />
  <va-icon v-if="!online" name="sync_disabled" color="danger"/>
</template>

<script>
  export default {
    data: () => ({
        online: null
      }),
      created() {
        this.checkOnline()
      },
      methods: {
        checkOnline() {
          this.online=navigator.onLine
        }
      }
  }
</script>
