<template>
    <va-avatar @click="avatarClicked(computer.id)" class="ml-2 mr-2" color="primary">
      {{computer.name.split(" ").map(x => x[0]).join(" ")}}
    </va-avatar>
</template>

<script>
    export default {
        props: {
            computer: Object
        },
        methods: {
            avatarClicked(id) {
                this.$emit('avatarClicked', id)
            }
        }
    }
</script>