<script setup>
import ComputerOnline from './ComputerOnline.vue'
</script>

<template>
  <div class="row">
    <div class="flex items-center mt-2 ml-3 md6 lg4">
      <va-card>
        <va-card-title>Computers online</va-card-title>
        <va-card-content>
            <ComputerOnline v-for="computer in computers" :computerName="computer.name" />
        </va-card-content>
      </va-card>
    </div>
  </div>
</template>

<script>
    const API_URL = `http://localhost:5000/comps`

    export default {
        data: () => ({
          computers: null
        }),
        created() {
          this.fetchData()
        },
        methods: {
          async fetchData() {
            const url = API_URL
            this.computers = await (await fetch(url)).json()
          }
        }
    }
</script>
  