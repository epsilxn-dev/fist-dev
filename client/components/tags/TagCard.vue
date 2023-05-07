<template>
    <v-card class="d-flex flex-column justify-space-between">
        <v-card-title>
            {{item.name || item.question || item.title || `${item.last_name} ${item.first_name} ${item.patronymic}`}}
        </v-card-title>
        <v-card-subtitle class="align-self-start mb-0">
            {{item.description || item.preview || item.theme || item.science_rank}}
        </v-card-subtitle>
        <v-card-actions class="ma-0">
            <v-card-text class="my-0 pt-0 pb-1">
                <TagList :tags="item.tags"/>
            </v-card-text>
            <v-spacer></v-spacer>
            <v-btn
                nuxt
                :to="getLink(itemKey,item.id)"
                color="primary lighten-2"
                text
                small
            >
                Перейти
            </v-btn>
        </v-card-actions>
    </v-card>
</template>
<script>
import TagList from '@/components/UI/TagList.vue'
export default {
  components: { TagList },
    data() {
        return {
            
        }
    },
    props: {
        item: {},
        itemKey: ''
        
    },
    methods: {
        getLink(itemKey, itemId) {
            switch(itemKey) {
                case 'specialties':
                    return `/directions/${itemId}`
                    break;
                case 'lessoners':
                    return `/teachers/${itemId}`
                    break;
                case 'questions':
                    return `/faq`
                    break;
                default:
                    return `/${itemKey}/${itemId}`
                    break;
            }
        }    
    },
}
</script>

<style lang="scss" scoped>

</style>