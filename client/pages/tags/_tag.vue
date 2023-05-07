<template>
    <v-container v-if="load" class="mt-4 mx-2">
        <v-row no-gutters>
            <v-col class=""/>
            <v-col class="col col-12 col-md-8">
                <h1 class="text-h4 text--primary mb-2">Тэги</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
                <v-text-field
                    class="courses__input_search"
                    placeholder="Поиск по содержанию..."
                    persistent-hint
                    append-icon="mdi-magnify"
                    dense
                    solo
                    v-model="query"
                >
                </v-text-field>
                <h1 class="text-h5 mb-4">Поиск по тегу: <span class="primary--text text-h5">{{tag}}</span> </h1>
                <div v-for="(item, key) in filteredResults" :key="key">
                    <v-chip
                        class="my-4"
                        v-if="filteredResults[key].length"
                    >
                        {{nameCompare[key]}}
                    </v-chip>
                    <v-container class="pb-0 d-flex justify-space-between flex-wrap ">
                        <TagCard
                            v-for="(item, indexTag) in filteredResults[key]"
                            :key="indexTag"
                            :item="item"
                            :itemKey="key"
                            class="tag__item mb-4"/>
                    </v-container>
                </div>
            </v-col>
            <v-col class="" >
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import TagCard from '~/components/tags/TagCard.vue'
export default {
    head(){
        let descr = "Поиск всей информации на сайте смежной с тегом",
            title = this.tag,
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
    components: { TagCard },
    fetch(){
        this.tag = this.$route.params.tag
        this.breadcrumbs.push({
            text: this.tag,
            to:'/tags/'+this.tag,
            disabled: true,
        })

        this.$axios.get(`api/v1/tags/contents/?tag=${this.tag}`).then(res=>{
            this.results = res.data.data
            this.load = true
        })

    },
    data(){
        return({
            results: {},
            query: '',
            tag: '',
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                },
                {
                    text: 'tags',
                    to: '/tags',
                    exact: true,
                }
            ],
            nameCompare: {
                disciplines: 'Дисциплины',
                ideas: 'Идеи',
                labs: 'Лаборатории',
                lessoners: 'Преподаватели',
                news: 'Новости',
                projects: 'Проекты',
                questions: 'Вопросы',
                specialties: 'Направления',
                default: 'Еще что-то'
            },
            load: false
        })
    },
    computed: {
        filteredResults(){
            let results = {...this.results}
            results.disciplines = []
            let keys = Object.keys(results)
            for (let key of keys){
                let filteredResults = results[key].filter(item=>{
                    if ((item?.title?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.name?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.text?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.science_rank?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.first_name?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.last_name?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.patronymic?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.theme?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.question?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.answer?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.information?.toLowerCase().trim().includes(this.query.toLowerCase().trim()) ||
                        item?.description?.toLowerCase().trim().includes(this.query.toLowerCase().trim()))){
                        return item
                    }
                })
                if (filteredResults){
                    results[key] = filteredResults
                }
                else {
                    results[key] = results[key]
                }
            }
            return results
        }
    }
}
</script>
<style lang="scss" scoped>
.tag__item {
    max-width: 49% !important;
    width: 49% !important;

    @media screen and (max-width: 960px) {
        max-width: 1000% !important;
        width: 100% !important;
    }
}
</style>
