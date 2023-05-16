<template>
    <v-card>
        <v-img height="130px" :src="base + lab.image"> </v-img>
        <v-card-title class="py-2">
            {{ lab.name }}
        </v-card-title>

        <v-card-text>
            <v-breadcrumbs
                class="py-1 pa-0 primary--text"
                :items="stack"
            ></v-breadcrumbs>
            {{ lab.description }}
        </v-card-text>
        <v-card-actions class="px-4">
            <TagList :tags="lab.tags" />
            <v-spacer></v-spacer>
            <v-btn
                nuxt
                :to="`/labs/${lab.id}`"
                color="primary lighten-2"
                text
                small
            >
                <div class="text-subtitle-2">просмотреть</div>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import TagList from "@/components/UI/TagList";
import { mapState } from "vuex";
export default {
    created() {
        for (let item of this.lab.areas) {
            this.stack.push({
                text: item.title,
            });
        }
    },
    components: {
        TagList,
    },
    data() {
        return {
            stack: [],
        };
    },
    props: {
        lab: {
            type: Object,
            default: {
                img: "",
                name: "",
            },
        },
    },
    computed: {
        ...mapState("auth", ["base"]),
    },
};
</script>
