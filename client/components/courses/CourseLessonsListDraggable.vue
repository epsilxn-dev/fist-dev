<template>
    <v-dialog
        @click:outside="close"
        :value="value"
        scrollable
        max-width="600px"
        width="100%"
    >
      <v-card>
        <v-card-title class="text-h5">
          Изменить порядок уроков
        </v-card-title>

        <v-card-text>
            <v-container class='mt-4 d-flex justify-space-between flex-wrap'>
                <Container
                    @drop="onDrop"
                    orientation='vertical'
                >
                    <Draggable v-for="(i,index) in lessons" 
                            :key="index">

                    <div class="draggable-item">
                        <CourseLesson 
                            :lesson="i"
                            :position="index+1"
                        />
                        
                    </div>

                    </Draggable>
                </Container>
                
            </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="red darken-1"
            text
            @click="close"
          >
            Отмена
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="saveClose"
          >
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>


<script>
import CourseLesson from '@/components/courses/CourseLesson.vue'
import { Container, Draggable } from "vue-dndrop";
import { applyDrag } from "@/helpers/applyDrag.js";
export default {
    data(){
        return {
            lessons: []
        }
    },
    components:{
        Container,
        Draggable,
        CourseLesson
    },
    props:{
        value: {
            type: Boolean,
            default: false
        },
        lessonsList: Array
    },
    beforeMount() {
        this.lessons = this.lessonsList
    },
    methods: {
        close(){
            this.$emit('close', this.show)
        },
        saveClose(){
            this.$emit('changeOrder', this.lessons)
        },
        onDrop(dropResult) {
            this.lessons = applyDrag(this.lessons, dropResult);

        },
    },
    
}
</script>


<style lang="scss">
    .dndrop-container{
        width: 100% !important ;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column
    }
    .draggable-item{
        width: 100% !important;
        padding: .7em !important;
        input{
            cursor: ns-resize !important;

        }
        .curp {
            cursor: pointer !important;
        }
    }
    .dndrop-draggable-wrapper{
        overflow: auto !important;
        width: 100%;
    }
    
</style>
