<template>
    
    <v-card>
        <v-img
            height="130px"
            :src="base+project.image"
            gradient="to top right, rgba(0,0,0,.2), rgba(25,32,72,.5)"
            dark
            class="d-flex align-center text-center justify-center"
        >
            <h2 dark class="pa-2 text-h5">
                {{project.name}}
            </h2>
        </v-img>
        
            
        <v-card-text class="pb-2">
            <div class="d-flex align-center">
                {{project.likes.length}}
                <v-icon class="ma-2">
                    mdi-thumb-up
                </v-icon>
                {{project.dislikes.length}}
                <v-icon class="ma-2">
                    mdi-thumb-down
                </v-icon>
            </div>
            <v-breadcrumbs
                class="py-1 pa-0 primary--text"
                :items="stack"
            ></v-breadcrumbs>
            {{project.description}}
        </v-card-text>
        <v-card-actions class="pt-0 px-4 my-0">
            <TagList :tags="project.tags"/>
            <v-spacer></v-spacer>
            <v-btn
                nuxt
                :to="`/projects/${project.id}`"
                color="primary lighten-2"
                text
                small
            >
                <div class="text-subtitle-2">просмотреть</div>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapState } from 'vuex'
import TagList from '@/components/UI/TagList'
export default {
    created(){
        for(let item of this.project.areas){
            this.stack.push({
                text: item.title
            })
        }
    },
    components:{
        TagList
    },
    data(){
        return({
            stack:[]
        })
    },
    props: {
        project: {
            type: Object,
            default: {
                img: '',
                name: ''
            }
        }
    },
    computed:{
        ...mapState('auth', ['base'])

    }
}
</script>

