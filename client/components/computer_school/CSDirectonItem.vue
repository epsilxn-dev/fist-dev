<template>
    <v-card v-bind="$attrs" class="my-5">
        <v-card-title class="text--primary ">
            {{item.name}}
        </v-card-title>
        <v-card-text>
            {{item.description}}
            <div class="text--primary my-3">Преподаватели</div>
            <div v-for="(i, index) in item.lessoners" :key="index">{{i.last_name}} {{i.first_name.slice(0,1).toUpperCase()}}.{{i.patronymic.slice(0,1).toUpperCase()}}.</div>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    props: {
        item: {
            type: Object,
            required: true,
            default: {
                name: '',
                description: '',
                teachers: []
            }
        }
    }
}
</script>
<style>
    
</style>