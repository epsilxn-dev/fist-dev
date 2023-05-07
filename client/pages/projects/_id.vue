<template>
    <v-container class="">
        <v-img
            v-if="project"
            class="mt--2 labs_img d-flex text-center align-center justify-center"
            :src="base+project.image"
            dark
            width="100%"
            gradient="to top right, rgba(0,0,0,.2), rgba(25,32,72,.5)"
        >
            <h1 class="text-h2">
                {{project.name}}
            </h1>
        </v-img>
        <v-snackbar
            v-model="snackbar"
            timeout="3000"
            >
            Авторизуйтесь для оценки или перезагрузите страницу

            <template v-slot:action="{ attrs }">
                <v-btn
                color="blue"
                text
                v-bind="attrs"
                @click="snack"
                >
                    Войти
                </v-btn>
            </template>
        </v-snackbar>
        <v-row class="pa-2" no-gutters>
            <v-col class="col"></v-col>
            <v-col class="col col-12 col-md-8">
                <h1 class="text-h4 my-2">Информация о проекте</h1>
                <v-breadcrumbs
                    class="pa-0 pb-2"
                    :items="breadcrumbs"
                />
                <div v-html="project.description"/>
                <h2 v-if="project.areas" class="text-h5 mt-2">Области технологий:</h2>
                <StackList :items="project.areas"/>
                <h2 class="text-h5 mb-2">Автор проекта</h2>
                <div v-if="project.teamlead" class="text--secondary mb-5">
                    <v-avatar
                        class="blue--text text--lighten-5"
                        size="48"
                        :color="colors[Math.floor(Math.random() * colors.length)]"
                    >
                        <v-img v-if="project.teamlead.avatar" :src="base+project.teamlead.avatar"></v-img>
                        <div v-else>
                           {{project.teamlead.username.slice(0,2)}}
                        </div>
                    </v-avatar>
                    {{project.teamlead.username}}
                </div>
                <h2 class="text-h5 my-2">Источник</h2>
                <a :href="project.source">{{project.source}}</a>
                <div class="my-4" v-if="project.lab">
                    <span class="text-h5 my-2">Лаборатория:</span>
                    <nuxt-link :to="`/labs/${project.lab.id}`">
                        {{project.lab.name}}
                    </nuxt-link>
                </div>
                <TagList v-if="project.tags" :tags="project.tags"/>
                <div v-if="project.likes" class="d-flex align-center">
                    <v-spacer/>
                    {{likes}}
                    <v-icon
                        :class="{'text--primary': isLiked}"
                        @click="like"
                        class="ma-2">
                        mdi-thumb-up
                    </v-icon>
                    {{dislikes}}
                    <v-icon
                        :class="{'text--primary': isDisliked}"
                        @click="dislike"
                        class="ma-2">
                        mdi-thumb-down
                    </v-icon>
                </div>
                <h2 class="text-h5 my-2">Команда</h2>
                <div v-if="project.contributors" class="my-4 d-flex justify-start">
                    <TeamItem
                        class="blue--text text--lighten-5 mr-2"
                        v-for="(item, index) in (project.contributors)"
                        :key="_id"
                        :user="item"
                        :color="colors[Math.floor(Math.random() * colors.length)]"
                    />
                </div>
                <div v-if="project.links && project.links.length!=0">
                    <h2 class="text-h5 my-2">Ссылки</h2>
                    <div class="mb-5">
                        <a
                            v-for="(item, index) in project.links"
                            :key="_id"
                            :href="item"
                        >
                            {{item}}
                            <br/>
                        </a>
                    </div>
                </div>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>

import { mapState } from 'vuex'
import TeamItem from '~/components/projects/TeamItem.vue'
import TagList from '~/components/UI/TagList.vue'
import StackList from '~/components/labs/StackList.vue'
import ProjectList from '~/components/labs/ProjectList.vue'
export default {
    head(){
        let descr = this.project.description,
            title = this.project.name,
            type = 'site',
            image = this.base+this.image
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
        TeamItem
    },
    async fetch(){

        this.projectId = this.$route.params.id
        if (this.$store.getters['projects/getProjects']==0){
            this.project = await this.$store.dispatch('projects/setProjects')
        }else{
            this.project = await this.$store.getters['projects/getProjects']
        }
        this.project = this.project.find(item=>item.id==this.projectId)
        this.likes = this.project.likes.length
        this.dislikes = this.project.dislikes.length
        for (let item of this.project.likes){
            if(item==this.user.id){
                this.isLiked = true
            }
        }
        for (let item of this.project.dislikes){
            if(item==this.user.id){
                this.isDisliked = true
            }
        }
        this.breadcrumbs.push({
            text: this.projectId,
            disabled: true,
            to: `/projects/${this.projectId}`,
            exact: true,
        })
    },
    data(){
        return ({
            snackbar: false,
            isLiked: false,
            isDisliked: false,
            colors: [
                'primary',
                'success',
                'cyan',
                'red',
                'green',
                'indigo',
                'deep-purple'
            ],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                    exact: true,
                },
                {
                    text: 'projects',
                    to: '/projects',
                    exact: true,
                },
            ],
            project:{},
            projectId: 0,
            likes: 0,
            dislikes: 0
        })
    },
    methods: {
        snack(){
            this.snackbar = false
            this.$router.push('/auth')
        },
        getRandomColor(){return this.colors[Math.floor(Math.random() * this.colors.length)]},
        like(){
            this.$axios.post('api/v1/projects/likes/',
                {
                    id:this.projectId
                },
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${this.accessToken}`,
                    }
                }
            ).then(res=>{
                if(res.data.data) {
                    this.likes+=1
                    if(this.isDisliked){
                        this.dislikes-=1
                    }
                } else{
                    this.likes-=1
                }
                this.isLiked = res.data.data
                this.isDisliked = false
            }).catch(()=>this.snackbar = true)
        },
        dislike(){
            this.$axios.post('api/v1/projects/dislikes/',
                {
                    id:this.projectId
                },
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${this.accessToken}`,
                    }
                }
            ).then(res=>{
                if(res.data.data) {
                    this.dislikes+=1
                    if(this.isLiked){
                        this.likes-=1
                    }
                } else{
                    this.dislikes-=1
                }
                this.isDisliked = res.data.data
                this.isLiked = false
            }).catch(()=>this.snackbar = true)
        },
    },
    computed:{
        commentaries(){
            let comments = [...this.ideaComments]
            for(let item of comments){
                item.author = item.user
                item.text = item.message
            }
            return comments
        },

        ...mapState('auth', ['accessToken', 'base']),
        user:{
            get() {
                return this.$store.getters['auth/getUser']
            },
            set(newValue) {
                this.$store.commit('auth/setUser', newValue)
            }
        }
    }
}
</script>
