<template>
    <v-list class="ma-0">
        <v-list-item class="ma-0" v-for="(item, index) in items" :key="index">
            <v-row>
                <v-icon x-small class="mr-2">mdi-circle</v-icon>
                <div class="text--secondary ma-0">{{item.name}}</div>
            </v-row>
        </v-list-item>
    </v-list>
        
</template>
<script>
export default {
    props: {
        items: []
    }
}
</script>
