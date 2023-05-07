<template>
   <v-container class="d-flex mt-4">
        <v-spacer
            class="
                d-sm-none
                d-lg-block
            "
        ></v-spacer>
        <v-row class="col-sm-14 pa-6 col-lg-8">
            <h1 class="text-h4">Создание урока #{{lessonNum}}</h1>
            <v-container>
                <v-text-field
                    clearable
                    v-model="title"
                    class="mt-4"
                    solo
                    counter="60"
                    hint="Укажите название вашего урока"
                    label="Название"
                ></v-text-field>
                <v-textarea
                    v-model="description"
                    class="mt-4"
                    solo
                    counter="250"
                    hint="Введите описание для вашего урока"
                    label="Описание"
                ></v-textarea>
                <h2 class="text-h5 mt-5">Теоретическая часть</h2>
                <v-card>
                    <wysiwyg class='mt-4' v-model="myHTML"/>
                </v-card>
                <h2 class="text-h5 mt-4">Тестовая часть</h2>
                <QuestionCreate :quests="questions"></QuestionCreate>
                <v-row class="pa-4">
                    <v-spacer></v-spacer>
                    <v-btn small class="mr-4 caption" color="red lighten-2 pa-4">Отмена</v-btn>
                    <v-btn small class="pa-4 caption"  color="primary lighten-2">Сохранить</v-btn>
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
import QuestionCreate from '~/components/courses/QuestionCreate.vue'
export default {
    components: {
        QuestionCreate
    },
    created() {
        this.lessonNum = this.$route.params.id
    },
    data(){
        return {
            myHTML: '',
            title: '',
            description: '',
            rules: [
                value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
            ],
            lessonNum: null,
            questions: [
                {
                    contain: 'При чём здесь ёжики?',
                    answers: [
                        'Смешарики',
                        'Лошарики',
                        'Кикорики'
                    ],
                    type: 'Множественный выбор',
                    rightAnswer: ['Смешарики']
                },
                {
                    contain: 'Какие размеры у объекта?',
                    answers: [
                        'Да',
                        'нет',
                    ],
                    type: 'Выбор',
                    rightAnswer: ['Да']
                },
                {
                    contain: 'Оказавшись перед Путиным, что вы ему скажете?',
                    answers: [],
                    type: 'Вписать ответ',
                    rightAnswer: ['Ненавижу вас']
                },
                {
                    contain: 'Расставьте в верно порядке',
                    answers: [
                        '1000',
                        '2000',
                        '3000'
                    ],
                    type: 'Расположить по порядку',
                    rightAnswer: ['1000', '2000', '3000']
                }
            ]
        }
    }
}
</script>
<style>

</style>
