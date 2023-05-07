<template>
    <v-expansion-panels>
        <v-expansion-panel
            v-if="disciplines"
            v-for="(item, i) in disciplines"
            :key="i"
        >
            <v-expansion-panel-header>
                <div v-if="item.info" class="text--primary">
                    {{item.info.name}}
                </div>
            </v-expansion-panel-header>
            <v-expansion-panel-content v-if="item.info">
                <div
                    v-html="item.info.information"
                    class="text--secondary"
                ></div>
                <div v-if="item.lessoners.length > 0">
                    <div class="text-primary my-3">Преподаватели</div>
                    <div class="d-flex flex-wrap">
                        <TeacherItem class="mr-2 mt-2" v-for="(teacher, j) in item.lessoners" :key="j" :item="teacher"/>
                    </div>
                </div>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>


<script>
import TeacherItem from '@/components/directions/TeacherItem.vue'
export default {
    mounted(){
    },
    components:{
        TeacherItem
    },
    props: {
        disciplines: []
    }
}
</script>

