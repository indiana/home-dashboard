<template>
      <va-card class="mt-4" color="secondary">
        <va-card-content>
          <p>Name: {{ computer.name }}</p>
          <p>Address: {{ computer.ip }}</p>
          <p>Ping: {{ computer.ping }}ms</p>
        </va-card-content>
        <va-card-actions align="right">
          <va-button @click="closeClicked()">X</va-button>
        </va-card-actions>        
      </va-card>
</template>

<script>
  export default {
      props: {
          computer: Object
      },
      methods: {
        closeClicked() {
          this.$emit("closeDetails")
        }
      }
  }
</script>