<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-7">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4 text--primary">Новости</h1>
                </v-row>
                <v-breadcrumbs
                    class="pa-0 pb-2"
                    :items="breadcrumbs"
                ></v-breadcrumbs>
            </v-col>
            <v-col class="d-none d-md-block"> </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-flex" />
            <v-col class="col col-md-7 col-12">
                <v-text-field
                    placeholder="Поиск новости..."
                    persistent-hint
                    append-icon="mdi-magnify"
                    dense
                    solo
                    v-model="query"
                />
                <Filters
                    class="d-auto d-md-none"
                    :tags="tags"
                    @applyFilters="applyFilter"
                />
                <h2 class="text-h5 text--primary">Доступные новости</h2>
                <v-container v-if="filteredNews.length != 0">
                    <NewsItem
                        v-for="(newsItem, index) in filteredNews"
                        :key="index"
                        :item="newsItem"
                        class="my-8"
                    />
                </v-container>
                <v-container v-else>
                    <w-no-info></w-no-info>
                </v-container>
                <v-alert
                    border="bottom"
                    color="pink darken-1"
                    dark
                    v-if="error.length !== 0"
                    class="mt-4"
                >
                    {{ error }}
                </v-alert>
                <div v-show="isLazyLoading" class="text-center">
                    <v-progress-circular indeterminate color="primary" />
                </div>
                <div
                    v-show="
                        !isLazyLoading && !nextExist && filteredNews.length != 0
                    "
                >
                    <h3 class="text-h5 text--primary text-center">
                        Вы просмотрели все новости
                    </h3>
                </div>
                <div
                    v-intersection="addNews"
                    v-show="
                        !isLazyLoading && nextExist && filteredNews.length != 0
                    "
                    class="makeMore"
                >
                    <v-btn
                        @click="addNews"
                        color="primary lighten-2"
                        text
                        small
                    >
                        Смотреть еще...
                    </v-btn>
                </div>
            </v-col>
            <v-col class="col d-none d-md-block">
                <Filters class="mx-6" @applyFilters="applyFilter" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import NewsItem from "@/components/news/NewsItem";
import Filters from "@/components/UI/Filters";
import NoInfo from "~/components/UI/NoInfo.vue";
export default {
    head() {
        let descr = "Новости факультета информационных систем и технологий",
            title = "Новости",
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
        NewsItem,
        "w-no-info": NoInfo,
    },
    fetch() {
        const params = new URLSearchParams([["page", this.count]]);
        this.$axios
            .get("api/v1/news", { params })
            .then((res) => {
                this.news = [...res.data.data.results];
                this.count++;
                if (res.data.data.next) {
                    this.nextExist = true;
                } else {
                    this.nextExist = false;
                }
                this.show = true;
            })
            .catch((err) => {
                this.error = err;
            });
    },
    data() {
        return {
            news: [],
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                },
                {
                    text: "news",
                    disabled: true,
                    exact: true,
                    to: "/news",
                },
            ],
            tags: ["js", "c#", "Новое"],
            isLazyLoading: false,
            count: 1,
            error: "",
            nextExist: false,
            filters: {
                selectedTag: "",
                reverse: false,
            },
            query: "",
            show: false,
        };
    },
    computed: {
        filteredNews() {
            let news = this.news.filter((item) => {
                let tagMatch = false;
                for (let tag of item.tags) {
                    if (
                        tag.name
                            .toLowerCase()
                            .includes(this.filters.selectedTag.toLowerCase())
                    ) {
                        tagMatch = true;
                    }
                }
                if (
                    item.title
                        .trim()
                        .toLowerCase()
                        .includes(this.query.trim().toLowerCase()) &&
                    tagMatch
                ) {
                    return item;
                }
            });
            return this.filters.reverse ? news : news.reverse();
        },
    },
    methods: {
        addNews() {
            if (!this.nextExist) {
                return;
            }
            this.isLazyLoading = true;
            const params = new URLSearchParams([["page", this.count]]);
            this.$axios
                .get("api/v1/news", { params })
                .then((res) => {
                    this.news = [...this.news, ...res.data.results];
                    this.count++;
                    if (res.data.next) {
                        this.nextExist = true;
                    } else {
                        this.nextExist = false;
                    }

                    this.isLazyLoading = false;
                })
                .catch((err) => {
                    this.error = err;
                    this.isLazyLoading = false;
                });
        },
        applyFilter(filters) {
            this.filters = filters;
        },
    },
};
</script>
<style scoped>
.makeMore {
    display: flex;
    justify-content: center;
    flex-direction: row;
}
</style>
