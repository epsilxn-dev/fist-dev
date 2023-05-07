<template>
    <div>
        <v-expansion-panels>
            <v-expansion-panel>
                <v-expansion-panel-header class="py-0 my-0">
                    Итоговая команда
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-list>
                        <v-list-item
                            class="mx-0 pa-0"
                            v-for="(item, index) in team"
                            :key="index"
                        >
                            <v-list-item-content class="pa-0">
                                <div class="text--secondary mx-0 my-1">
                                    <v-avatar
                                        class="blue--text text--lighten-5"
                                        size="48"
                                        :color="colors[Math.floor(Math.random() * colors.length)]"
                                    >
                                    {{item.name.split(' ')[0].slice(0,1) + item.name.split(' ')[1].slice(0,1)}} 
                                    </v-avatar>
                                        {{item.name}}
                                    <v-btn
                                        color="success lighten-2"
                                        x-small
                                        class="ml-5"
                                        fab
                                        outlined
                                        nuxt
                                        @click="edit(index)"
                                    >
                                        <v-icon >
                                            mdi-pencil
                                        </v-icon>
                                    </v-btn>
                                    <v-btn
                                        color="error lighten-2"
                                        x-small
                                        fab
                                        outlined
                                        nuxt
                                        @click="deleteItem(index)"
                                    >
                                        <v-icon>
                                            mdi-delete
                                        </v-icon>
                                    </v-btn>
                                </div>
                            </v-list-item-content>
                        </v-list-item>
                        </v-list>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </div>
</template>

<script>
export default {
    data(){
        return({
            colors: [
                'primary',
                'success',
                'cyan',
                'red',
                'green',
                'indigo',
                'deep-purple'
            ],
        })
    },
    props:{
        team: []
    },
    methods:{
        edit(id){
            this.$emit('edit', id)
        },
        deleteItem(id){
            this.$emit('delete', id)
        }
    }
}
</script>

