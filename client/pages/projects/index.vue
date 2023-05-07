<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-7">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4">Проекты факультета</h1>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="success lighten-2"
                        small
                        fab
                        nuxt
                        to="ideas/suggest"
                    >
                        <v-icon>
                            mdi-plus
                        </v-icon>
                    </v-btn>
                </v-row>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
            </v-col>
<!--            <v-col class="d-none d-md-block">-->
<!--            </v-col>-->
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"/>
            <v-col class="col col-12 col-md-7">
                <v-text-field
                    placeholder="Поиск проектов..."
                    persistent-hint
                    append-icon="mdi-magnify"
                    dense
                    solo
                    v-model="query"
                ></v-text-field>
                <!--                <Filters-->
                <!--                    class="mx-0 d-auto d-md-none mb-2"-->
                <!--                    @applyFilters="applyFilters"-->
                <!--                    :tags="tags"-->
                <!--                ></Filters>-->
                <h1 class="text-h5 mb-2">Текущие проекты</h1>
                <v-container v-if="filteredProjects.length !== 0" class="pb-2 d-flex flex-wrap justify-space-between">
                    <ProjectCard
                        class="labs_item mt-4"
                        v-for="(item, index) in filteredProjects"
                        :project="item"
                        :key="index"
                    ></ProjectCard>
                </v-container>
                <v-container v-else>
                    <w-no-info></w-no-info>
                </v-container>
                <v-container class="d-flex mb-2 justify-center align-center">
                    <v-btn v-if="filteredProjects.length === 4" @click="showMore" color="primary">
                        Показать больше
                    </v-btn>
                    <v-btn v-if="filteredProjects.length > 4" @click="showLess" color="primary">
                        Скрыть
                    </v-btn>
                </v-container>
            </v-col>
<!--            <v-col class="col d-none d-md-block">-->
<!--                <Filters class="mx-6" @applyFilters="applyFilters" :tags="tags"/>-->
<!--            </v-col>-->
        </v-row>
    </v-container>
</template>

<script>
import QuestionForm from '@/components/faq/QuestionForm'
import TagList from '@/components/UI/TagList'
import Filters from '@/components/UI/Filters'
import ProjectCard from '@/components/projects/ProjectCard'
import NoInfo from "~/components/UI/NoInfo.vue";

export default {
    components: {
        TagList,
        QuestionForm,
        ProjectCard,
        "w-no-info": NoInfo
    },
    head() {
        let descr = 'Текущие проекты факультета информационных систем и технологий',
            title = 'Проекты',
            type = 'site'
        return {
            title: title,
            meta: [
                {hid: 'description', name: 'description', content: descr},
                {hid: 'og:title', name: 'og:title', content: descr},
                {hid: 'og:description', name: 'og:description', content: descr},
                {hid: 'og:type', name: 'og:type', content: type}
            ]
        }
    },
    async fetch() {
        this.projects = await this.$store.dispatch('projects/setProjects')
    },
    data() {
        return ({
            filters: {
                reverse: true,
                selectedTag: ''
            },
            toShow: 4,
            query: '',
            projects: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                },
                {
                    text: 'projects',
                    to: '/projects',
                    exact: true,
                }
            ],
            tags: [
                'Js',
                'c#',
                'Робототех'
            ]
        })
    },

    methods: {
        applyFilters(filters) {
            this.filters = filters
        },
        showMore() {
            this.toShow = this.projects.length
        },
        showLess() {
            this.toShow = 4
        }
    },
    computed: {
        filteredProjects() {
            let projects = [...this.projects].filter(item => {
                let tagMatch = false
                for (let tag of item.tags) {
                    if (tag.name.trim().toLowerCase().includes(this.filters.selectedTag.trim().toLowerCase())) {
                        tagMatch = true
                    }
                }
                if ((item.name.trim().toLowerCase().includes(this.query.trim().toLowerCase())
                    || item.description.trim().toLowerCase().includes(this.query.trim().toLowerCase())) && tagMatch) {
                    return item
                }
            })
            projects = projects.slice(0, this.toShow)
            return this.filters.reverse ? projects : projects.reverse()
        }
    },
}
</script>

