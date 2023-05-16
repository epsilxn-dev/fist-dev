<template>
    <v-container v-if="direct" class="">
        <v-img
            class="mt--2 dir_img d-flex text-center align-center justify-center"
            :src="base+direct.avatar"
            dark
            width="100%"
            gradient="to top right, rgba(0,0,0,.2), rgba(25,32,72,.5)"
        >
            <h1 class="text-h2">
                {{ direct.name }}
            </h1>
        </v-img>
        <v-row no-gutters>
            <v-col class="col col-1 d-none d-md-flex"></v-col>
            <v-col class="col col-12 col-md-8 pa-2">
                <v-breadcrumbs
                    class="pa-0 py-4"
                    :items="breadcrumbs"
                />
                <v-card class="ma-2 d-block d-md-none">
                    <v-card-text>
                        <div class="text--primary mb-2">Сколько бюджетных мест?</div>
                        <div class="text--secondary mb-2">{{ direct.budget_seats }}</div>
                        <div class="text--primary mb-2">Сколько стоит обучение?</div>
                        <div class="text--secondary mb-2">{{ direct.price }}</div>
                        <div class="text--primary mb-2">Сколько учиться?</div>
                        <div class="text--secondary">{{ direct.years }} года</div>
                    </v-card-text>
                </v-card>
                <h2 class="text-h5">Описание</h2>
                <div v-html="direct.information" class="mt-2 text--secondary">
                    <!-- {{direct.description}} -->
                </div>
                <h2 class="text-h5 mt-2">Области технологий:</h2>
                <StackList :items="direct.stack_techs"/>
                <div v-if="disciplines?.length > 0">
                    <h2 class="text-h5 mt-2">Дисциплины:</h2>
                    <DisciplineList class="my-4" :disciplines="disciplines"/>
                </div>
<!--                <h2 class="text-h5 mt-2">Что в итоге?</h2>-->
<!--                <StackList :items="results"/>-->
                <TagList v-if="direct.tags" :tags="direct.tags"/>

            </v-col>
            <v-col class="col col-3 d-none d-md-block">
                <v-card class="ma-6">
                    <v-card-text v-if="direct.budget_seats">
                        <div class="text--primary mb-2">Сколько бюджетных мест?</div>
                        <div class="text--secondary mb-2">{{ direct.budget_seats }}</div>
                        <div class="text--primary mb-2">Сколько стоит обучение?</div>
                        <div class="text--secondary mb-2">{{ direct.price }}</div>
                        <div class="text--primary mb-2">Сколько учиться?</div>
                        <div class="text--secondary">{{ direct.years }}</div>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import {mapState} from 'vuex'
import TagList from '~/components/UI/TagList.vue'
import StackList from '~/components/labs/StackList.vue'
import DisciplineList from '~/components/directions/DisciplineList.vue'

export default {
    components: {
        TagList,
        StackList,
        DisciplineList
    },
    data() {
        return ({
            disciplines: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                    exact: true,
                },
                {
                    text: 'directions',
                    to: '/#directions',
                    exact: true,
                },
            ],
            direct: {},
            directId: 0,
            results: []
        })
    },
    head() {
        let descr = this.direct?.information,
            title = this.direct?.name,
            type = 'site',
            image = this.base + this.direct?.avatar
        return {
            title: title,
            meta: [
                {hid: 'description', name: 'description', content: descr},
                {hid: 'og:title', name: 'og:title', content: descr},
                {hid: 'og:description', name: 'og:description', content: descr},
                {hid: 'og:type', name: 'og:type', content: type},
                {hid: 'og:image', name: 'og:image', content: image},
                {hid: 'vk:image', name: 'vk:image', content: image},
            ]
        }
    },
    async fetch() {
        this.directId = this.$route.params.id
        let res = await (await this.$axios.get(`api/v1/specialties/${this.directId}/`)).data
        this.direct = res.data.specialty ?? []
        this.results = res.data.results ?? []
        this.disciplines = res.data.disciplines ?? []
        let disciplines = []
        for (let item of this.disciplines) {
            let res = (await this.$axios.get(`api/v1/disciplines/${item.id}`)).data
            console.log(res.data.discipline)
            disciplines.push({
                info: res.data.discipline,
                lessoners: res.data.lessoners
            })
        }
        this.disciplines = disciplines

        this.breadcrumbs.push({
            text: this.directId,
            disabled: true,
            to: `/directions/${this.directId}`,
            exact: true,
        })
    },
    computed: {
        ...mapState('auth', ['base'])
    },
    fetchOnServer: false
}
</script>

<style lang="scss" scoped>
.dir_img {
    height: 500px;
    @media screen and (max-width: 800px) {
        height: 300px;
    }
}
</style>
