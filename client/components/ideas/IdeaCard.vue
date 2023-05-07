<template>
    
    <v-card>
        <v-img
            height="250px"
            :src="base + idea.image"
            gradient="to top right, rgba(0,0,0,.2), rgba(25,32,72,.5)"
            dark
            class="d-flex align-center text-center justify-center"
        >
            <h2 dark class="pa-2 text-h5">
                {{idea.name}}
            </h2>
        </v-img>
        <v-card-text class="pb-2">
            <div class="d-flex align-center">
                {{idea.likes.length}}
                <v-icon class="ma-2">
                    mdi-thumb-up
                </v-icon>
                {{idea.dislikes.length}}
                <v-icon class="ma-2">
                    mdi-thumb-down
                </v-icon>
            </div>
            <v-breadcrumbs
                class="py-1 pa-0 primary--text"
                :items="stack"
            ></v-breadcrumbs>
            {{idea.description}}
        </v-card-text>
        <v-card-actions v-if="!editable">
            
            <v-spacer></v-spacer>
            
            <v-btn
                v-if="idea.id"
                nuxt
                :to="`/ideas/${idea.id}`"
                color="primary lighten-2"
                text
                small
            >
                просмотреть
            </v-btn>
        </v-card-actions>
        <v-card-actions v-else>
            <v-spacer></v-spacer>
            <v-btn
                nuxt
                @click="$emit('delete', {id: idea.id, idx})"
                fab
                v-if="!idea.is_deleted"
                icon
                dark
                small
                outlined
                color="error"
            >
                <v-icon
                    dark
                >
                    mdi-bucket-outline
                </v-icon>
            </v-btn>
            <v-btn
                nuxt
                :to="`/ideas/edit/${idea.id}`"
                fab
                icon
                dark
                small
                outlined
                color="cyan"
            >
                <v-icon
                    dark
                >
                    mdi-pencil
                </v-icon>
            </v-btn>
            <v-btn
                outlined
                nuxt
                v-if="idea.id"
                :to="`/ideas/${idea.id}`"
                fab
                icon
                small
                dark
                color="primary"
            >
                <v-icon
                    dark
                >
                    mdi-eye
                </v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import TagList from '@/components/UI/TagList'
import {mapState} from 'vuex'

export default {
    created(){
        for(let item of this.idea.area_tech){
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
        editable: {
            type: Boolean,
            default: false
        },
        idea: {
            type: Object,
            default: {
                img: '',
                name: ''
            }
        },
        idx: {
            type: Number,
            required: false
        }
    } ,
    computed:{
        ...mapState('auth', ['base'])
    }
}
</script>

