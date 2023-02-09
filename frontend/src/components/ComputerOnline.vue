<template>
    <va-avatar @click="avatarClicked(computerName)" class="ml-2 mr-2" color="primary">
      {{computerName.split(" ").map(x => x[0]).join(" ")}}
    </va-avatar>
</template>

<script>
    export default {
        props: {
            computerName: String
        },
        methods: {
            avatarClicked(msg) {
                alert(msg)
            }
        }
    }
</script>