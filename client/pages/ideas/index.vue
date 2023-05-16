<template>
    <v-container class="mt-4 pa-2 d-sm">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-7">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4">Идеи факультета</h1>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="success lighten-2"
                        small
                        fab
                        nuxt
                        to="ideas/suggest"
                    >
                        <v-icon> mdi-plus </v-icon>
                    </v-btn>
                </v-row>
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
                    placeholder="Поиск идей..."
                    persistent-hint
                    append-icon="mdi-magnify"
                    dense
                    solo
                    v-model="query"
                />

                <Filters
                    class="mx-0 d-auto d-md-none mb-2"
                    @applyFilters="applyFilters"
                    :tags="tags"
                />
                <h1 class="text-h5 mb-2">Идеи на рассмотрении</h1>
                <v-container
                    v-if="filteredIdeas.length !== 0"
                    class="pb-2 d-flex flex-wrap justify-space-between"
                >
                    <IdeaCard
                        class="labs_item mt-4"
                        v-for="(item, index) in filteredIdeas"
                        :idea="item"
                        :key="index"
                    />
                    <Add
                        @click="$router.push('/ideas/suggest')"
                        class="labs_item mt-4"
                    />
                </v-container>
                <v-container v-else>
                    <w-no-info></w-no-info>
                </v-container>
                <div class="d-flex justify-center">
                    <v-btn
                        v-if="ideas.length > filteredIdeas.length"
                        @click="showMore"
                        color="primary"
                    >
                        Больше
                    </v-btn>
                    <v-btn
                        v-else-if="
                            ideas.length === filteredIdeas.length && toShow > 4
                        "
                        @click="toShow = 4"
                        color="primary"
                    >
                        Скрыть
                    </v-btn>
                </div>
            </v-col>
            <v-col class="col d-none d-md-block">
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
import IdeaCard from "@/components/ideas/IdeaCard";
import Add from "@/components/UI/Add";
import NoInfo from "~/components/UI/NoInfo.vue";

export default {
    head() {
        let descr = "Идеи факультета информационных систем и технологий",
            title = "Идеи",
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
    components: {
        Filters,
        TagList,
        QuestionForm,
        IdeaCard,
        Add,
        "w-no-info": NoInfo,
    },
    async fetch() {
        this.ideas = await this.$store.dispatch("ideas/setIdeas");
    },
    data() {
        return {
            filters: {
                reverse: true,
                selectedTag: "",
            },
            toShow: 4,
            query: "",
            ideas: [],
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                },
                {
                    text: "ideas",
                    to: "/ideas",
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
            this.toShow = this.ideas.length;
        },
        showLess() {
            this.toShow = 4;
        },
    },
    computed: {
        filteredIdeas() {
            if (this.ideas.length > 0) {
                let ideas = this.ideas.filter((item) => {
                    let tagMatch = false;
                    for (let tag of item.tags) {
                        if (
                            tag.name
                                .trim()
                                .toLowerCase()
                                .includes(
                                    this.filters.selectedTag
                                        .trim()
                                        .toLowerCase()
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
                ideas = ideas.slice(0, this.toShow);
                return this.filters.reverse ? ideas : ideas.reverse();
            }
            return [];
        },
    },
};
</script>
