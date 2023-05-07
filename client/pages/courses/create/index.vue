<template>
    <v-container class="d-flex mt-4">
        <CourseLessonsListDraggable
            v-model="show"
            @close="close"
            :lessonsList="lessons"
            @changeOrder="changeOrder"
        ></CourseLessonsListDraggable>
        <v-spacer
            class="
                d-sm-none
                d-lg-block
            "
        ></v-spacer>
        <v-row class="col-sm-14 pa-6 col-lg-9">
            <h1 class="text-h4">Создайте свой курс</h1>
            <v-container class="image_input mt-4">
                <ImageInput @change="setImage" :rules="rules"/>
            </v-container>
            <v-container>
                <v-text-field
                    clearable
                    v-model="courseTitle"
                    class="mt-4"
                    solo
                    counter="60"
                    hint="Укажите название вашего курса"
                    label="Название"
                ></v-text-field>
                <h2 class="text-h5 mt-5">Описание курса</h2>
                <v-card>
                    <wysiwyg class='mt-4' v-model="courseDescription"/>
                </v-card>
                <v-container class="mt-4 d-flex justify-center align-center">
                    <h2 class="text-h5">Список уроков</h2> 
                    <v-spacer></v-spacer>
                    <v-btn
                        color="success lighten-2"
                        small
                        fab
                        @click="show = true"
                    >
                        <v-icon>
                            mdi-shuffle
                        </v-icon>
                    </v-btn>
                </v-container>
                
                <v-container class='mt-4 d-flex justify-space-between flex-wrap'>
                    <CourseLesson 
                        class="w-50"
                        v-for="(i,index) in lessons" 
                        :key="index"
                        :lesson="i"
                        :position="index+1"
                        @deleteLesson="deleteLesson"
                    />
                    <AddLesson @click="addLesson"/>
                </v-container>
                <v-row class="pa-4">
                    <v-spacer></v-spacer>
                    <v-btn small class="mr-4 caption" color="red lighten-2 pa-4">Отмена</v-btn>
                    <v-btn @click="saveCourse" small class="pa-4 caption"  color="primary lighten-2">Сохранить</v-btn>
                </v-row>
            </v-container>
        </v-row>
        <v-spacer
            class="
                d-sm-none
                d-lg-block
            "
        ></v-spacer>
    </v-container>
</template>

<script>
import ImageInput from '@/components/courses/ImageInput.vue'
import CourseLesson from '@/components/courses/CourseLesson.vue'
import CourseLessonsListDraggable from '@/components/courses/CourseLessonsListDraggable.vue'
import AddLesson from '@/components/courses/AddLesson.vue'
import { Container, Draggable } from "vue-dndrop";
import { applyDrag } from "@/helpers/applyDrag.js";
export default {
    components:{
        ImageInput,
        CourseLesson,
        AddLesson,
        Container,
        Draggable,
        CourseLessonsListDraggable
    },
    data(){
        return {
            courseDescription: '',
            courseTitle: '',
            courseImage: '',
            rules: [
                value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
            ],
            lessons: [
                {   
                    id: 0,
                    title: 'Обзор частей колеса',
                    description: 'Рассмотрим, из чего же состоит колесо'
                },
                {
                    id: 1,
                    title: 'Сбор своего квадратного колеса',
                    description: 'Рассмотрим, из чего же состоит колесо'
                },
                {
                    id: 2,
                    title: 'Теория робототехники',
                    description: 'Рассмотрим, из чего же состоит колесо'
                }
            ],
            show: false,
        }
    },
    methods:{
        addLesson(){
            this.$router.push(`create/createLesson/${this.lessons.length+1}`)
        },
        deleteLesson(id){
            this.lessons.splice(id,1)
        },
        setImage(e){
            this.courseImage = e
        },
        saveCourse(){
            let course = {}
            course.title = this.courseTitle
            course.image = this.courseImage
            course.description = this.courseDescription
        },

        onDrop(dropResult) {
            this.lessons = applyDrag(this.lessons, dropResult);
        },
        
        close(show){
            this.show=show
        },
        changeOrder(newLessonsList){
            this.close()
            this.lessons = newLessonsList
        }
    }
}
</script>

<style lang="scss">

    .w-50{
        width: 49%
    }
</style>





