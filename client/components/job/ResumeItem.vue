<template>
    <v-card class="d-flex flex-column mb-3">
        <div :class="{'opacity-70': resume.isDeleted}" v-if="resume" class="d-flex flex-column flex-md-row justify-space-between">
            <div>
                <v-card-title>
                    {{resume.title}}
                </v-card-title>
                <div class="d-block d-md-none my-0 border-2">
                    <v-img
                        tile
                        class="mx-4 ma-0 border-2"
                        size="100%"
                        height="200px"
                        :src="base+resume.image"
                        color="grey"
                    ></v-img>
                </div>
                <v-card-subtitle>
                    Опыт работы: {{resume.work_exp}}
                </v-card-subtitle>
                <v-card-text class="d-flex flex-column align-left justify-space-between">
                    {{resume.description}}
                    <TagList v-if="resume.tags" class="justify-self-end" :tags="resume.tags"/>
                </v-card-text>
            </div>
            <div class="d-none d-md-block">
                <v-avatar
                    tile
                    class="ma-4 border-4"
                    size="200"
                    color="grey"
                    
                >
                    <v-img
                        class="border-4"
                        :src="base + resume.image"
                    ></v-img>
                </v-avatar>
            </div>
            
        </div>
        <v-card-actions v-if="!editable">
            <v-card-text >
                {{resume.updated_at}}
            </v-card-text>
            <v-spacer></v-spacer>
            
            <v-btn
                v-if="resume.id"
                nuxt
                :to="`/job/resumes/${resume.id.id}`"
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
                @click="$emit('delete')"
                fab
                v-if="!resume.is_deleted"
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
                :to="`/job/resumes/edit/${resume.id.id}`"
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
                v-if="resume.id"
                :to="`/job/resumes/${resume.id.id}`"
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
import { mapState } from 'vuex'
export default {
    components:{
        TagList
    },
    props:{
        editable: {
            type: Boolean,
            default: false
        },
        resume: {
            type: Object,
            required: true
        }
    },
    computed:{
        ...mapState('auth', ['base'])

    }
}
</script>

<style scoped>
    .opacity-70{
        opacity: 50% !important;
    }
</style>
