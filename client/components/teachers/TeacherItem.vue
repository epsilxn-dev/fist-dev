<template>
    <v-card v-bind="$attrs" :to="`/teachers/${item.id}`">
        <v-container class="d-flex flex-column align-center">
            <v-chip
                class="align-self-end transform__up"
                small
                mandatory
                :color="item.departmentColor"
                nuxt
                dark
                :to="`/directions/${item.department.id}`"
            >
                <div class="caption">
                    {{ item.department.name }}
                </div>
            </v-chip>

            <v-avatar size="150">
                <v-img :src="base + item.avatar" />
            </v-avatar>
            <v-card-title class="title text--primary text-center">
                {{ item.first_name }}
                {{ item.patronymic }}
                {{ item.last_name }}
            </v-card-title>
            <v-card-subtitle
                class="text-subtitle-1 text--secondary text-center"
            >
                {{ item.science_rank }}
            </v-card-subtitle>
        </v-container>
    </v-card>
</template>
<script>
import { mapState } from "vuex";

export default {
    props: {
        item: {
            type: Object,
            required: true,
            default: {
                name: "",
                rank: "",
                avatar: "",
                departmentColor: "",
                department: "",
            },
        },
    },
    computed: {
        ...mapState("auth", ["base"]),
    },
};
</script>
<style scoped>
.transform__up {
    transform: translateY(-12px);
}
</style>
