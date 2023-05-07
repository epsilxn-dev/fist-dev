<template>
     <v-card v-bind="$attrs" width="31.5%" min-width="300px">
        <v-container class="d-flex flex-column align-center">
            <v-chip class="align-self-end transform__up" 
                small
                mandatory 
                :color="item.directionColor"
                nuxt
                dark
                :to="`/direction/${item.specialty.id}`"
            >
                <div class="caption">
                    {{item.specialty.name}}
                </div>
            </v-chip>

            <v-avatar width="150px" height="150px">
                <v-img :src="base+item.avatar" />
            </v-avatar>
            <v-card-title class="title text--primary text-center">
                {{item.fio}}
            </v-card-title>
            <v-card-subtitle class="text-subtitle-1 text--secondary text-center">
                {{item.rank}}
            </v-card-subtitle>
            <v-card-text class="text-center" v-html="item.information"/>
        </v-container>
    </v-card>
</template>
<script>
import { mapState } from "vuex"
export default {
    
    props:{
        item: {
            type: Object,
            required: true,
            default: {
                name: '',
                rank: '',
                avatar: '',
                description: '',
                directionColor: '',
                direction: '',
            }
        },
    },
    computed:{
        ...mapState('auth', ['base'])

    }
}
</script>
<style scoped>
.transform__up {
    transform: translateY(-12px);
}
</style>