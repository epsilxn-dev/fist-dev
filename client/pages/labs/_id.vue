<template>
    <v-container class="">
        <v-img
            class="mt--2 labs_img d-flex text-center align-center justify-center"
            :src="base+lab.image"
            dark
            width="100%"
            gradient="to top right, rgba(0,0,0,.2), rgba(25,32,72,.5)"
        >
            <h1 class="text-h2">
                {{lab.name}}
            </h1>
        </v-img>
        <v-row class="pa-2" no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-8 col-sm-10">
                <h1 class="text-h5 text-md-h4 my-4">Информация о лаборатории</h1>
                <v-breadcrumbs
                    class="pa-0 pb-2"
                    :items="breadcrumbs"
                />
                <div v-html="lab.text"/>
                <h2 class="text-h5 mt-3">Области технологий:</h2>
                <StackList :items="lab.areas"/>
                <div v-if="projects.length!=0">
                    <h1 class="text-h5 mb-3">Проекты</h1>
                    <ProjectList class="mb-6" :projects="projects"/>
                </div>
                <h2 class="text-h5 mt-2">Адрес:</h2>
                <div class="text--secondary">{{lab.address}}</div>
            </v-col>
            <v-col class="col d-none d-md-block">
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import Swal from 'sweetalert2'
import TagList from '~/components/UI/TagList.vue'
import StackList from '~/components/labs/StackList.vue'
import ProjectList from '~/components/labs/ProjectList.vue'
import { mapState } from 'vuex'
export default {
    head(){
        let descr = this.lab.description,
            title = this.lab.name,
            type = 'site',
            image = this.base+this.lab.image
        return {
            title: title,
            meta: [
                {hid: 'description', name: 'description', content: descr},
                {hid: 'og:title', name: 'og:title', content: descr},
                {hid: 'og:description', name: 'og:description', content: descr},
                {hid: 'og:type', name: 'og:type', content: type},
                {hid: 'og:image', name: 'og:image', content: image},
                {hid: 'vk:image', name: 'vk:image', content: image},
            ]
        }
    },
    components:{
        TagList,
        StackList,
        ProjectList
    },
    async fetch(){
        this.labId = this.$route.params.id
        let response = (await this.$axios.get(`api/v1/laboratories/${this.labId}/`)).data.data
        this.lab = response.lab
        this.projects = response.projects
        this.breadcrumbs.push({
            text: this.labId,
            disabled: true,
            to: `/labs/${this.labId}`,
            exact: true,
        })
    },
    data(){
        return ({
            projects: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                    exact: true,
                },
                {
                    text: 'labs',
                    to: '/labs',
                    exact: true,
                },
            ],
            lab:{},
            labId: 0
        })
    },
    methods: {
        showContacts(){
            Swal.fire({
                position: 'center',
                icon: 'info',
                title: `${this.vacancie.email}`,
                text: `${this.vacancie.phone}`,
                showConfirmButton: false,
                timer: 40000
            })
        }
    },
    computed:{
        ...mapState('auth', ['base'])

    }
}
</script>
