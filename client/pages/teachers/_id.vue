
<template lang="">
     <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4">Преподаватели</h1>
                </v-row>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
                <div class="mt-4 d-flex">
                    <div class="d-none d-md-block">
                        <v-avatar size="200px">
                            <v-img class="mr-5 teach_img" :src="base+teacher.avatar"/>
                        </v-avatar>
                    </div>
                    <div class="d-flex flex-column align-center align-md-start justify-center">
                        <div class="d-block d-md-none">
                            <v-avatar size="200px">

                                <v-img class="mr-0 mr-md-5 teach_img" :src="base+teacher.avatar"/>
                            </v-avatar>

                        </div>
                        <h2 class="text-h5 text--primary mt-4">{{teacher.last_name}} {{teacher.first_name}} {{teacher.patronymic}}</h2>
                        <h2 class="text-h5 text--secondary mt-4">{{teacher.science_rank}}</h2>
                        <div class="subtitle-1 text-center text-md-left text--secondary mt-4" v-html="teacher.information"></div>
                        <v-chip v-if="teacher.department">
                            {{teacher.department.name}}
                        </v-chip>
                    </div>
                </div>
                <h2 class="text-h4 text-center text-md-left text--primary mt-4">Дисциплины:</h2>
                <DisciplinesList :items="teacher.disciplines"/>
            </v-col>
            <v-col></v-col>
        </v-row>
    </v-container>
</template>
<script>
import DisciplinesList from '~/components/teachers/DisciplinesList.vue';
import { mapState } from 'vuex';
export default {
    components: {
        DisciplinesList
    },
    head() {
        let descr = this.teacher.information,
            title = this.teacher.last_name + this.teacher.first_name,
            type = 'site',
            image = this.base + this.teacher.avatar
        return {
            title: title,
            meta: [
                { hid: 'description', name: 'description', content: descr },
                { hid: 'og:title', name: 'og:title', content: descr },
                { hid: 'og:description', name: 'og:description', content: descr },
                { hid: 'og:type', name: 'og:type', content: type },
                { hid: 'og:image', name: 'og:image', content: image },
                { hid: 'vk:image', name: 'vk:image', content: image },
            ]
        }
    },
    async fetch() {
        this.id = this.$route.params.id
        if (this.$store.getters['teachers/getTeachers'].length == 0) {
            this.teacher = await this.$store.dispatch('teachers/setTeachers')
            this.teacher = this.teacher.find(item => item.id == this.id)
        }

        this.breadcrumbs.push({
            text: this.teacher.id,
            disabled: true,
            to: `/${this.id}`,
        })
    },
    data() {
        return {
            id: -1,
            teacher: {},
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                },
                {
                    text: 'teachers',
                    exact: true,
                    to: '/teachers',
                },]
        }
    },
    computed: {
        ...mapState('auth', ['base'])

    }
}
</script>

<style lang="scss" scoped>

</style>
