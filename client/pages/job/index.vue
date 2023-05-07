<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-7">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4">Трудоустройство</h1>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="success lighten-2"
                        small
                        fab
                        nuxt
                        to="job/resumes/create"
                    >
                        <v-icon>
                            mdi-plus
                        </v-icon>
                    </v-btn>
                </v-row>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
                <v-text-field
                    class="courses__input_search"
                    placeholder="Поиск резюме..."
                    persistent-hint
                    append-icon="mdi-magnify"
                    dense
                    solo
                    v-model="query"
                >
                </v-text-field>
                <Filters class="mx-0 d-auto d-md-none mb-2" @applyFilters="applyFilters" :tags="tags"/>
                <h1 class="text-h5 mb-4">Доступные резюме</h1>
            </v-col>
            <v-col class="d-none d-md-block">
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"/>
            <v-col class="col col-12 col-md-7">
                <v-container v-if="filteredResumes.length">
                    <ResumeItem v-for="(resume, index) in filteredResumes" :key="index" :resume="resume"/>
                    <div class="d-flex justify-center">
                        <v-btn v-if="resumes.length > filteredResumes.length" @click="showMore" color="primary">
                            Больше
                        </v-btn>
                        <v-btn v-else-if="resumes.length == filteredResumes.length && toShow > 7" @click="toShow = 7" color="primary">
                            Скрыть
                        </v-btn>
                    </div>
                </v-container>
                <v-container v-else>
                    <w-no-info></w-no-info>
                </v-container>
            </v-col>
            <v-col class="col d-none d-md-block" >
                <Filters class="mx-6" @applyFilters="applyFilters" :tags="tags"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import ResumeItem from '@/components/job/ResumeItem'
import Filters from '@/components/UI/Filters'
import {mapState} from 'vuex'
import NoInfo from "~/components/UI/NoInfo.vue";
export default {
    components: {
        ResumeItem,
        Filters,
        "w-no-info": NoInfo
    },
    async fetch(){
        this.resumes = await this.$store.dispatch('job/setResumes')
    },
    head(){
        let descr = 'Доступные резюме для студентов факультета информационных систем и технологий',
            title = 'Резюме',
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
    data(){
        return ({
            filters:{
                reverse: false,
                selectedTag: ''
            },

            query:'',
            resumes: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                    exact: true,

                },
                {
                    text: 'job',
                    to: '/job',
                    exact: true,
                },
            ],
            toShow: 7,
            tags:[
                'Js',
                'c#',
                'Робототех'
            ]
        })
    },
    computed:{
        ...mapState('auth', ['base']),
        filteredResumes(){
            let resumes = this.resumes.filter(item=>{
                let tagMatch = false
                for (let tag of item.tags){
                    if (tag.name.includes(this.filters.selectedTag)){
                        tagMatch = true
                    }
                }
                if ((item.title.includes(this.query) || item.description.includes(this.query)) && tagMatch){
                    return item
                }
            })
            let result = !this.filters.reverse ? resumes : resumes.reverse()
            return result.slice(0, this.toShow)
        }
    },
    methods: {
        applyFilters(filters){
            this.filters=filters
        },
        showMore(){
            this.toShow+=7
            if(this.toShow>this.resumes.length)this.toShow=this.resumes.length
        }
    },
}
</script>

