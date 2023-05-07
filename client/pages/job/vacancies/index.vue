<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-md-7 col-12">
                <h1 class="text-h4 my-4">Трудоустройство</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
                <v-text-field 
                    class="courses__input_search"  
                    placeholder="Поиск резюме..."
                    persistent-hint
                    append-icon="mdi-magnify" 
                    dense
                    v-model="query"
                    solo
                >
                </v-text-field>
                <Filters class="mx-0 d-auto d-md-none mb-2" @applyFilters="applyFilters" :tags="tags"/>
                <h1 class="text-h5 mb-4">Доступные вакансии</h1>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2"/>
            <v-col class="col col-md-7 col-12">
                <v-container v-if="filteredVacancies.length!=0">
                    <VacancieItem v-for="(vacancie, index) in filteredVacancies" :key="index" :vacancie="vacancie"/>
                    <div class="d-flex justify-center">
                        <v-btn v-if="vacancies.length > filteredVacancies.length" @click="showMore" color="primary">
                            Больше
                        </v-btn>
                        <v-btn v-else-if="vacancies.length == filteredVacancies.length && toShow>7" @click="toShow = 7" color="primary">
                            Скрыть
                        </v-btn>
                    </div>
                    
                </v-container>
                <v-container
                    v-else
                >
                    <v-alert
                    border="bottom"
                    color="info darken-1"
                    dark
                    class="mt-4"
                    >
                        Совпадений не обнаружено
                    </v-alert>
                </v-container>
            </v-col>
            <v-col class="col d-none d-md-block" >
                <Filters class="mx-6" @applyFilters="applyFilters" :tags="tags"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import VacancieItem from '@/components/job/VacancieItem'
import Filters from '@/components/UI/Filters'
export default {
    head(){
        let descr = 'Список вакансий',
            title = 'Вакансии',
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
    components: {
        VacancieItem, Filters
    },
    async fetch(){
        this.vacancies = await this.$store.dispatch('job/setVacancies')
        if (this.vacancies.length!=0) return
        this.$axios.get('https://api.hh.ru/vacancies?area=1614&text=Разработчик').then((res)=>{
            this.vacancies=res.data.items
            let options = {
                year: 'numeric',
                month: 'numeric',
                day: 'numeric',
                timezone: 'UTC',
                hour: 'numeric',
                minute: 'numeric',
            };
            for(let item of this.vacancies){
                item.hh = true
                item.work_exp = item.snippet.requirement
                item.salary_min = item.salary?.from
                item.salary_max = item.salary?.to
                let created_at = new Date(item.created_at)
                item.company = {}
                item.description = item.snippet.responsibility
                item.company.avatar = item?.employer?.logo_urls?.original
                item.created_at = created_at.toLocaleString("ru", options)
            }
        })
    },

    data(){
        return ({
            filters: {
                selectedTag:''
            },
            query: '',
            toShow: 7,
            vacancies: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                },
                {
                    text: 'job',
                    to: '/job',
                    exact: true,
                },
                {
                    text: 'vacancies',
                    disabled: true,
                    to: '/job/vacancies',
                    exact: true,
                },
            ],
            tags:[
                'Js',
                'c#',
                'Робототех'
            ]
        })
    },
    methods: {
        applyFilters(filters){
            this.filters = filters
        },
        showMore(){
            this.toShow+=7
            if(this.toShow>this.vacancies.length)this.toShow=this.vacancies.length
        }
    },
    computed:{
        filteredVacancies(){
            let vacancies = this.vacancies.filter(item=>{
                let tagMatch = false
                if (!item.hh){
                    for (let tag of item.tags){
                        if (tag.name.includes(this.filters.selectedTag)){
                            tagMatch = true
                        }
                    }
                }
                else{
                    tagMatch = true
                }
                if ((item.name?.toLowerCase().includes(this.query.toLowerCase()) 
                    || item.title?.toLowerCase().includes(this.query.toLowerCase()) 
                    || item.description?.toLowerCase().includes(this.query.toLowerCase())) 
                    && tagMatch){
                    return item
                }
            })
            let result = !this.filters.reverse ? vacancies : vacancies.reverse()
            return result.slice(0, this.toShow)
        }
    }
}
</script>

