<template>
    <div class="course_lesson mb-4">
        <v-card hover v-ripple shaped>
            <v-card-title>
                Урок {{position}}
            </v-card-title>
            <v-card-subtitle>
                {{lesson.title}}
            </v-card-subtitle>
            <v-card-text>
                {{lesson.description}}
            </v-card-text>
            <v-card-actions right>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary lighten-2"
                    fab
                    small
                >
                    <nuxt-link :to="`create/createLesson/${position}`">
                        <v-icon>
                            mdi-pencil
                        </v-icon>
                    </nuxt-link>
                </v-btn>
                <v-btn
                    color="red lighten-2"
                    small
                    fab
                    @click="deleteLesson(position-1)"
                >
                    <v-icon>
                        mdi-delete
                    </v-icon>
                </v-btn>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
export default {
    props:{
        lesson: Object,
        position: Number
    },
    methods: {
        deleteLesson(id){
            this.$emit('deleteLesson', id)
        }
    },
}
</script>

<style>
    .course_lesson{
        width: 100%;
    }
</style>


