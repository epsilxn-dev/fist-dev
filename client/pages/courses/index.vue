
<template>  
    <div >
        <div class="courses__preview">
            <div class="courses__preview_gradient">
            <div class="courses__preview_wpapper">
                <h2 class="curses__preview_title">
                    Курсы
                </h2>
                <h3 class="curses__preview_description">
                    бесплатные курсы для вашего саморазвития
                </h3>    
            </div>
            </div>
        </div>
    
        <v-container class="mt-6">
            <v-row no-gutters>
                <v-spacer></v-spacer>
                <v-col class="col col-7">
                    <v-text-field 
                        class="courses__input_search"  
                        v-text-field 
                        placeholder="Поиск курсов..."
                        persistent-hint
                        append-icon="mdi-magnify" 
                        dense
                        solo
                    >
                    </v-text-field>
                    <CourseItem  class="courses__item"></Courseitem>
                </v-col>
                <v-col>
                    <CourseParams class="courses__params"></CourseParams>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import CourseItem from '@/components/courses/courseItem.vue'
    import CourseParams from '@/components/courses/courseParams.vue'
    export default {
        components: { 
            CourseItem,
            CourseParams
        },
        data() {
            return {
                search: 'Поиск курсов...'
            }
        },
    }
</script>
<style>
    
</style>