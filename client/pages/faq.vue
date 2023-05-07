<template>
    <v-container class="mt-4">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-flex"></v-col>
            <v-col class="col col-12 col-md-7 pa-2">
                <h1 class="text-h4 mb-2">FAQ</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2" />
            <v-col class="col col-md-7 col-12 pa-2">
                <v-text-field class="courses__input_search" placeholder="Поиск вопросов..." persistent-hint
                    append-icon="mdi-magnify" dense solo v-model="query">
                </v-text-field>
                <Filters class="mx-0 d-auto d-md-none mb-2" @applyFilters="applyFilters" :tags="tags" />

                <h1 class="text-h5 mb-0">Самые волнующие вопросы</h1>
                <div v-if="Object.keys(filteredQuestions).length > 0" v-for="(value, name) in filteredQuestions"
                    class="pt-2" :key="name">
                    <div v-if="value.length != 0" class="py-4">
                        <v-chip>
                            {{ name }}
                        </v-chip>
                    </div>
                    <v-expansion-panels v-for="(item, index) in value" :key="index">
                        <v-expansion-panel class="mb-1">
                            <v-expansion-panel-header>
                                {{ item.question }}
                            </v-expansion-panel-header>
                            <v-expansion-panel-content>
                                {{ item.answer }}
                                <TagList :tags="item.tags" />
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </div>
                <NoInfo v-if="Object.keys(filteredQuestions).length == 0"/>
                <h1 class="text-h5 mt-6 my-4">Не нашли вопрос? Задайте свой!</h1>
                <QuestionForm @suggestQuestion="suggestQuestion" id="ask" />
            </v-col>
            <v-col class="col d-none d-md-block">
                <Filters class="mx-6 mt-2" @applyFilters="applyFilters" :tags="tags" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import QuestionForm from '@/components/faq/QuestionForm'
import TagList from '@/components/UI/TagList'
import Filters from '@/components/UI/Filters'
import Swal from 'sweetalert2'
import NoInfo from '@/components/UI/NoInfo.vue'
export default {
    head() {
        let descr = 'Вопросы, которые могли у вас возникнуть',
            title = 'FAQ',
            type = 'site'
        return {
            title: title,
            meta: [
                { hid: 'description', name: 'description', content: descr },
                { hid: 'og:title', name: 'og:title', content: descr },
                { hid: 'og:description', name: 'og:description', content: descr },
                { hid: 'og:type', name: 'og:type', content: type }
            ]
        }
    },
    components: {
    Filters,
    TagList,
    QuestionForm,
    NoInfo
},
    async fetch() {
        await this.$store.dispatch('faq/setQuestions').then(res => { })
        this.questions = this.$store.getters['faq/getQuestions']
        this.groupQuestions()
    },
    data() {
        return ({
            filters: {
                reverse: false,
                selectedTag: ''
            },

            query: '',
            questions: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    href: '/',
                },
                {
                    text: 'faq',
                    href: '/faq',
                    disabled: true
                }
            ],
            tags: [
                'Js',
                'c#',
                'Робототех',
                'деньги'
            ]
        })
    },

    methods: {
        applyFilters(filters) {
            this.filters = filters
        },
        groupQuestions() {
            let themes = []
            let groupedQuestions = {}
            for (let quest of this.questions) {
                let currentTheme = quest.theme
                if (themes.includes(currentTheme)) {
                    groupedQuestions[currentTheme].push({
                        question: quest.question,
                        answer: quest.answer,
                        tags: quest.tags
                    })
                }
                else {
                    groupedQuestions[currentTheme] = [
                        {
                            question: quest.question,
                            answer: quest.answer,
                            tags: quest.tags
                        }
                    ]
                }
                themes.push(currentTheme)
            }
            this.questions = groupedQuestions
        },
        suggestQuestion(question) {
            this.$axios.post('api/v1/questions/', {
                author_email: question.email,
                question: question.question
            }).then(res => {
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'Вопрос отправлен!',
                    showConfirmButton: false,
                    timer: 3000
                })
            }).catch(res => {
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: 'Что-то пошло не так',
                    showConfirmButton: false,
                    timer: 3000
                })
            })
        }
    },
    computed: {
        filteredQuestions() {
            let questions = { ...this.questions }
            let keys = Object.keys(questions)
            for (let key of keys) {
                let filteredQuestion = questions[key].filter(item => {
                    let tagMatch = false
                    for (let tag of item.tags) {
                        if (tag.name.toLowerCase().includes(this.filters.selectedTag.toLowerCase())) {
                            tagMatch = true
                        }
                    }
                    if ((item.question.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item.answer.toLowerCase().trim().includes(this.query.toLowerCase().trim())) && tagMatch) {
                        return item
                    }
                })
                if (filteredQuestion) {
                    questions[key] = filteredQuestion
                }
                else {
                    questions[key] = questions[key]
                }
            }
            return questions

        }
    },
}
</script>

