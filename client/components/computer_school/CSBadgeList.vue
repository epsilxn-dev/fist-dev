<template>
    <v-list class="ma-0">
        <v-list-item class="ma-0" v-for="(item, index) in items" :key="index">
            <v-row class="d-flex align-center justify-left flex-row">
                <v-avatar size="40">
                    <v-img :src="item.image"></v-img>
                </v-avatar>
                <a :href="item.to" class="text--secondary ml-4">{{item.name}}</a>
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
