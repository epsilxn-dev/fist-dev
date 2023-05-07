<template>
    <v-chip-group 
        column 
        class="d-flex flex-wrap"
    >
        <v-chip 
            small
            :class="{'unactive':active}"
            active-class="deep-purple--text text--accent-4"
            mandatory 
            :color="tag.color"
            nuxt
            dark
            :to="`/tags/${tag.content}`"
            v-for="(tag, index) in coloredTags" :key="index">
            <div class="caption">
                {{tag.content}}
            </div>
        </v-chip>
    </v-chip-group>
</template>

<script>
export default {
    created(){
        for (let item of this.tags){
            this.coloredTags.push({
                content: item.name || item.title,
                color: this.getRandomColor()
            })
        }
    },
    data(){
        return({
            colors: [
                'primary',
                'success',
                'red',
                'green',
                'cyan',
                'indigo',
                'deep-purple'
            ],
            coloredTags: [],
            filters:{

            },
            query: ''
        })
    },

    props:{
        active: true,
        tags:[]
    },
    methods: {
        getRandomColor(){return this.colors[Math.floor(Math.random() * this.colors.length)]}
    }
}
</script>

