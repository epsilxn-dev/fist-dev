<template>
    <v-card class="d-flex flex-md-row flex-column justify-start mb-3 ">         
        <v-img
            :src="base+item.image"
            class="card_img"
        ></v-img>     
        <div class="d-flex flex-column justify-space-between w-60">             
            <v-card-title class="text-h5 font-weight-medium">
                {{item.title}}
            </v-card-title>
            <v-card-subtitle class="body-2 text--secondary ">
                {{item.create_at}}
            </v-card-subtitle>
            <v-card-text class="text--secondary card_desc body-1 font-weight-medium">
                {{item.description}}            
            </v-card-text>

            <v-card-actions>
                <v-card-text>
                    <TagList :tags="item.tags"/>
                </v-card-text>
                <v-spacer></v-spacer>
                <v-btn
                    nuxt
                    :to="`/news/${item.id}`"
                    color="primary lighten-2"
                    text
                    small
                >
                    просмотреть
                </v-btn>
            </v-card-actions>
        </div>
    </v-card>
</template>


<script>
import TagList from '../UI/TagList.vue'
import { mapState } from 'vuex'
export default {
  components: { TagList },
    props:{
        item: {
            type: Object,
            required: true
        }
    },
    computed:{
        ...mapState('auth', ['base'])

    }
}
</script>

<style lang="scss" scoped>
.card_img{
    width: 40%;
    max-height: 300px !important;
    @media screen and (max-width: 950px) {
        width: 100% !important;
        max-height: 300px;
    }
    @media screen and (max-width: 600px) {
        max-height: 200px;
    }
}


.w-60{
    width: 100%;
    @media screen and (max-width: 950px) {
        width: 100% !important;
    }
}


</style>

