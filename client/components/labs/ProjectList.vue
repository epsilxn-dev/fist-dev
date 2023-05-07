<template>
    <v-expansion-panels class="py-2">
        <v-expansion-panel v-for="(item, index) in projects " :key="index">
            <v-expansion-panel-header>
                {{item.name}}
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                {{item.description}}
                <div class="d-flex justify-space-between">
                    <TagList :tags="item.tags"/>
                    <div class="d-flex align-center">
                        {{item.likes.length}}
                        <v-icon class="ma-2">
                            mdi-thumb-up
                        </v-icon>
                        {{item.dislikes.length}}
                        <v-icon class="ma-2">
                            mdi-thumb-down
                        </v-icon>
                    </div>
                </div>
                
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>

<script>
import TagList from '@/components/UI/TagList'
export default {
    components: {
        TagList
    },
    props:{
        projects: []
    }
}
</script>

