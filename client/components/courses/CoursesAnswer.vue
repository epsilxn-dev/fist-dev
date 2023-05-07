<template>
    <div class="course_lesson mb-4">
        <v-card hover v-ripple shaped>
            <v-card-title >
                Вопрос 1
            </v-card-title>
            <v-card-subtitle>
                Какие типы данных относятся к примитивам
            </v-card-subtitle>
            <v-card-text class="mx-4 my-0 pa-0" v-for="val in inputValues" :key="val">
                <v-checkbox v-if="inputType === 'checkbox'" :label="val" v-model="inputRightAnswer" :value="val" dense></v-checkbox>
            </v-card-text>
            <v-card-actions right>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary lighten-2"
                    fab
                    outlined

                >
                    <v-icon>
                        mdi-pencil
                    </v-icon>
                </v-btn>
                <v-btn
                    color="red lighten-2"
                    outlined
                    fab

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
    data() {
        return {
            inputType: 'checkbox',
            inputValues: ['Object', 'Array', 'String', 'Number'],
            inputRightAnswer: ['Array']
        }
    }
}
</script>

<style>

</style>


