<template>
    <v-card>
        <v-card-text class="d-flex justify-space-between align-center">
            <div>
                <v-avatar  size="100" color="primary">
                    <v-img v-if="item.avatar" :src="base+item.avatar"></v-img>
                    <div v-else>{{item.last_name.slice(0,1)}}{{item.first_name.slice(0,1)}}</div>
                </v-avatar>
            </div>
            <div class="pa-2 text-center">
                <div class="text--primary">
                    {{item.last_name}} {{item.first_name}} {{item.patronymic}}
                </div>
                <v-card-subtitle>
                    {{item.science_rank}}
                </v-card-subtitle>
            </div>
        </v-card-text>
        
        
    </v-card>
</template>


<script>
import {mapState} from 'vuex'
export default {
    props: {
        item: {}
    },
    computed: {
        ...mapState('auth', ['base'])
    },
}
</script>
