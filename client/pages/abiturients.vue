<template>
    <v-container class="mt-4">
        <v-row no-gutters>
            <v-col class="col col-1 d-none d-md-flex"/>
            <v-col class="col col-12 pa-4 col-md-10">
                <h1 class="text-h4 mb-2">Абитуриентам</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
                <h4 class="text-h5 mb-2">Направления подготовки</h4>
                <v-card v-if="directs.length" class="my-4">
                    <v-tabs
                        v-model="currentTab"
                        slider-color="primary"
                    >
                        <v-tab
                            v-for="i in directs"
                            :key="i.name"
                            :href="`#tab-${i.name}`"
                        >
                            {{ i.name }}
                        </v-tab>
                    </v-tabs>
                    <v-tabs-items v-model="currentTab">
                        <v-tab-item
                            v-for="i in directs"
                            :key="i.name"
                            :value="`tab-${i.name}`"
                        >
                            <v-card flat>
                                <v-card-text class="d-flex flex-column flex-md-row justify-space-between">
                                    <v-avatar class="dir_img mb-2 d-none d-md-flex" width="400px" height="300px"
                                              rounded>
                                        <v-img
                                            width="100%"
                                            :src="base+i.avatar"
                                        />
                                    </v-avatar>
                                    <div class="ml-0 ml-md-5">
                                        <div class="mb-2 text-h5 text--primary">
                                            {{ i.full_name }}
                                        </div>
                                        <v-avatar class="dir_img mb-2 d-flex d-md-none" height="300px" rounded>
                                            <v-img
                                                :src="base+i.avatar"
                                            />
                                        </v-avatar>
                                        <div class="text--h1 mb-2 d-flex flex-column">
                                            <div class="d-flex ">
                                                <v-icon class="mr-1 text-h5">
                                                    mdi-layers
                                                </v-icon>
                                                <div
                                                    class="py-0 mr-2 text-body-2"
                                                    v-text="makeStack(i.stack_techs).join(' / ')"
                                                ></div>
                                            </div>
                                            <div class="d-flex">
                                                <v-icon class="mr-1 text-h5">
                                                    mdi-account-box-multiple
                                                </v-icon>
                                                <div
                                                    class="text-body-2"
                                                >Бюджетных мест: {{ i.budget_seats }}
                                                </div>
                                            </div>
                                        </div>
                                        {{ i.description }}

                                    </div>

                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        color="primary"
                                        :to="`/directions/${i.id}`"
                                    >
                                        Подробнее
                                    </v-btn>
                                </v-card-actions>

                            </v-card>
                        </v-tab-item>
                    </v-tabs-items>
                </v-card>
                <NoInfo v-else/>
                <h2 class="text-h5 mb-2">Правила приёма</h2>
                <v-alert
                    text
                    outlined
                    class="mt-2"
                    type="info"
                >
                    Более подробно про поступление можно посмотреть на официальном сайте УлГТУ
                    <a target="_blank" referrerpolicy="no-referrer" href="https://ulstu.ru/">ulstu.ru</a>
                </v-alert>
                <Rules class="my-2"/>
                <h2 class="text-h5 mb-2">Полезные ссылки</h2>
                <div v-if="links.length">
                    <a v-for="(item, index) in links" class="my-4" :key="index"
                       :href="item.href">{{ item.text }}<br/></a>
                </div>
                <NoInfo v-else/>
            </v-col>
            <v-col class="col d-none d-md-flex"/>
        </v-row>
    </v-container>
</template>

<script>

import Rules from '@/components/abiturients/Rules'
import NoInfo from '~/components/UI/NoInfo.vue'
import {mapState} from 'vuex'

export default {
    head() {
        let descr = 'Направения подготовки и правила приёма на факультет информационных систем и технологий',
            title = 'Абитуриентам',
            type = 'site'
        // image = this.base+this.newsItem.image
        return {
            title: title,
            meta: [
                {hid: 'description', name: 'description', content: descr},
                {hid: 'og:title', name: 'og:title', content: descr},
                {hid: 'og:description', name: 'og:description', content: descr},
                {hid: 'og:type', name: 'og:type', content: type},
                // {hid: 'og:image', name: 'og:image', content: image},
                // {hid: 'vk:image', name: 'vk:image', content: image},
            ]
        }
    },
    components: {
        Rules,
        NoInfo
    },
    async fetch() {
        await this.$store.dispatch('directs/setDirections').then(res => {
        })
        this.directs = await this.$store.getters['directs/getDirections']
    },

    data() {
        return ({
            links: [
                {
                    href: 'https://ulstu.ru/abitur/bak-spec-mag/',
                    text: 'Приёмная комиссия'
                },
                {
                    href: 'https://ulstu.ru/school/prepare-for-admission/',
                    text: 'Подготовка к поступлению'
                },
                {
                    href: 'http://akademia.ulstu.ru/',
                    text: 'Инженерная академия'
                },
                {
                    href: 'https://ulstu.ru/abitur/it-litsey/',
                    text: 'IT-лицей'
                },
                {
                    href: 'https://old.ulstu.ru/main/view/article/21952',
                    text: 'Среднее профессиональное образование'
                },
                {
                    href: 'https://old.ulstu.ru/main/view/article/17959',
                    text: 'Аспирантура'
                },
                {
                    href: '/computer_school',
                    text: 'Компьютерная школа ФИСТ (портал ФИСТ)'
                }
            ],
            currentTab: 0,
            directs: [],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                },
                {
                    text: 'abiturients',
                    to: '/abiturients',
                    exact: true,
                }
            ]
        })
    },

    methods: {
        makeStack(stack) {
            let resultStack = []
            for (let i of stack) {
                resultStack.push(i.name.slice(0, 10).length == 20 ? i.name.slice(0, 20) + '..' : i.name.slice(0, 20))
            }
            return resultStack
        }

    },
    computed: {
        ...mapState('auth', ['base']),
        filteredLabs() {
            let labs = this.labs.filter(item => {
                let tagMatch = false
                for (let tag of item.tags) {
                    if (tag.trim().toLowerCase().includes(this.filters.selectedTag.trim().toLowerCase())) {
                        tagMatch = true
                    }
                }
                if ((item.name.trim().toLowerCase().includes(this.query.trim().toLowerCase())
                    || item.preview.trim().toLowerCase().includes(this.query.trim().toLowerCase())) && tagMatch) {
                    return item
                }
            })
            labs = labs.slice(0, this.toShow)
            return this.filters.reverse ? labs : labs.reverse()
        }
    },
}
</script>

<style lang="scss">
.dir_img {
    width: 100% !important;
    min-width: 400px !important;
    max-width: 400px;
    @media screen and (max-width: 900px) {
        min-width: 100% !important;
        max-height: 200px !important;
    }
}

.d_img {
    min-width: 100% !important;
    max-width: 100% !important;
}
</style>
