<template>
<div>
     <v-container >
        <v-card class="mx-auto mb-4" height=180>
            <v-row no-gutters>
                <v-col cols="12" md="4">
                    <v-img :src="require('@/assets/images/courses/Robotech_course.png')" height="180" aspect-ratio="1" ></v-img>
                </v-col>
                <v-col cols="12" md="6">
                    <v-card-title>Робототехника</v-card-title>
                    <v-card-subtitle>Святов К.В.</v-card-subtitle>
                    <v-card-text>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt, suscipit!</v-card-text>
                </v-col>
                <v-col cols="12" md="2" class="course__col_link">
                    <a href="#" class="course__link">Перейти</a>
                </v-col>
            </v-row>
        </v-card>
    </v-container>
  
</div>

   
</template>
<script>
export default {
     data: () => ({
    }),
}
</script>
<style>
.course__col_link{
    display: flex;
}
.course__link{
    text-align: right;
    margin-right: 1rem;
    margin-bottom: 1rem;
    color:blue !important;
    align-self: flex-end;
}
</style>