<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-7">
                <h1 class="text-h4 mb-2">Лаборатории</h1>
                <v-breadcrumbs
                    class="pa-0 pb-2"
                    :items="breadcrumbs"
                ></v-breadcrumbs>
            </v-col>
            <v-col class="d-none d-md-block"> </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block" />
            <v-col class="col col-12 col-md-7">
                <v-text-field
                    class="courses__input_search"
                    placeholder="Поиск лабораторий..."
                    persistent-hint
                    append-icon="mdi-magnify"
                    dense
                    solo
                    v-model="query"
                ></v-text-field>
                <Filters
                    class="mx-0 d-auto d-md-none mb-2"
                    @applyFilters="applyFilters"
                    :tags="tags"
                />
                <h1 class="text-h5 mb-4">Текущие лаборатории</h1>
                <v-container
                    v-if="filteredLabs.length !== 0"
                    class="pb-2 d-flex flex-wrap justify-space-between"
                >
                    <LabCard
                        class="labs_item mt-4"
                        v-for="(item, index) in filteredLabs"
                        :lab="item"
                        :key="index"
                    />
                </v-container>
                <v-container v-else>
                    <w-no-info></w-no-info>
                </v-container>
                <v-container class="d-flex mb-2 justify-center align-center">
                    <v-btn
                        v-if="labs.length > filteredLabs.length"
                        @click="showMore"
                        color="primary"
                        >Больше</v-btn
                    >
                    <v-btn
                        v-else-if="
                            labs.length == filteredLabs.length && toShow > 4
                        "
                        @click="toShow = 4"
                        color="primary"
                        >Скрыть</v-btn
                    >
                </v-container>
            </v-col>
            <v-col class="d-none d-md-block">
                <Filters
                    class="mx-6"
                    @applyFilters="applyFilters"
                    :tags="tags"
                />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import QuestionForm from "@/components/faq/QuestionForm";
import TagList from "@/components/UI/TagList";
import Filters from "@/components/UI/Filters";
import LabCard from "@/components/labs/LabCard";
import NoInfo from "~/components/UI/NoInfo.vue";

export default {
    components: {
        Filters,
        TagList,
        QuestionForm,
        LabCard,
        "w-no-info": NoInfo,
    },
    async fetch() {
        this.labs = await this.$store.dispatch("labs/setLabs");
    },
    head() {
        let descr =
                "Текущие лаборатории факультета информационных систем и технологий",
            title = "Лаборатории",
            type = "site";
        return {
            title: title,
            meta: [
                { hid: "description", name: "description", content: descr },
                { hid: "og:title", name: "og:title", content: descr },
                {
                    hid: "og:description",
                    name: "og:description",
                    content: descr,
                },
                { hid: "og:type", name: "og:type", content: type },
            ],
        };
    },
    data() {
        return {
            filters: {
                reverse: false,
                selectedTag: "",
            },
            toShow: 4,
            query: "",
            labs: [],
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                },
                {
                    text: "labs",
                    to: "/labs",
                    exact: true,
                },
            ],
            tags: ["Js", "c#", "Робототех"],
        };
    },

    methods: {
        applyFilters(filters) {
            this.filters = filters;
        },
        showMore() {
            this.toShow = this.labs.length;
        },
        showLess() {
            this.toShow = 4;
        },
    },
    computed: {
        filteredLabs() {
            let labs = this.labs.filter((item) => {
                let tagMatch = false;
                for (let tag of item.tags) {
                    if (
                        tag.name
                            .trim()
                            .toLowerCase()
                            .includes(
                                this.filters.selectedTag.trim().toLowerCase()
                            )
                    ) {
                        tagMatch = true;
                    }
                }
                if (
                    (item.name
                        .trim()
                        .toLowerCase()
                        .includes(this.query.trim().toLowerCase()) ||
                        item.description
                            ?.trim()
                            .toLowerCase()
                            .includes(this.query.trim().toLowerCase())) &&
                    tagMatch
                ) {
                    return item;
                }
            });
            labs = labs.slice(0, this.toShow);
            return this.filters.reverse ? labs : labs.reverse();
        },
    },
};
</script>
