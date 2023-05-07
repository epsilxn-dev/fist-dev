<template>
    <div 
        class="IIContainer"
        @dragover="drag = true"
        @mouseleave="drag = false"
        @dragleave="drag = false"
        :class="{dragover: drag}"

    >
        <v-img
            rounded
            max-height="400px"
            class='img'
            :src="require('@/assets/images/courses/Robotech_course.png')"
        >
            <v-container class="image_input__container pa-4">
                <label for="file_input" class="file_input__label">
                    <v-btn
                        icon
                        color="primary"
                        x-large
                        class="d-flex align-center flex-column justify-center"
                    >
                        <v-icon
                            class="icon"
                            large>
                            mdi-camera
                        </v-icon>
                    </v-btn>
                    <div v-if="error" class="red--text caption">{{error}}</div>
                    <div v-if="fileName" class="caption">{{fileName}}</div>
                </label>
                <input 
                    @change="filePicker" 
                    type="file" 
                    class="file_input" 
                    id="file_input"
                    accept="image/jpeg,image/png,image/jpg"
                >
            </v-container>
        </v-img>
    </div>
</template>

<script>
export default {
    data(){
        return {
            image: '',
            fileName: null,
            error: null,
            drag: false
        }
    },
    props: {
        rules: [Array],
    },
    methods:{
        filePicker(e){
            try{
                let file = e.target.files[0]

                if (file.type != 'image/png' && file.type != 'image/jpeg' &&file.type != 'image/jpg'){
                    this.error = 'Неверный формат'
                    this.fileName = ''
                    return
                }
                if (file.size >= 1000000){
                    this.error = 'Слишком большой размер'
                    this.fileName = ''
                    return
                }
                this.fileName = file.name
                this.error = ''
                this.$emit('change', file)
            }
            catch{
                this.error = 'Выберите файл'
                this.fileName = ''
            }
        }
    }
    
}
</script>


<style lang="scss">
    .image_input {
        min-height: auto !important;
    }

    .image_input__container {
        transition: all .3s ease-in-out;
        transform: translateY(-10px);
        opacity: 0;
        width: 100% !important;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        .file_input {
            width: 100% !important;
        }
    }
    .dragover{
         .img{

                transform: scale(1.1);

            }
            .image_input__container {
                transform: translateY(0px);
                opacity: 1;
            }
    }
    .IIContainer{
        overflow: hidden;
        *{
                transition: all .4s ease-in-out;

        }
        .img{
            position: relative;
        }
        &:hover{
            .img{

                transform: scale(1.1);

            }
            .image_input__container {
                transform: translateY(0px);
                opacity: 1;
            }
        }
        .file_input{
            opacity: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
            position: absolute;
            top: 0;
            left: 0
            
        }
        .file_input__label{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            color: white;
            flex-direction: column;
            transform: scale(1.1);
            background-color: rgba(0, 0, 0, 0.3); 
            
            .icon{
                background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%23E6E6E685' stroke-width='4' stroke-dasharray='6%2c 14' stroke-dashoffset='4' stroke-linecap='square'/%3e%3c/svg%3e");
                padding: 2em 4em;
                transform: scale(1.5)
            }
        }
    }

</style>


