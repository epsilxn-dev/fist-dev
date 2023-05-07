<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8">
                <h1 class="text-h4 my-2">{{ vacancie.title }}</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs" />
                <v-card>
                    <v-card-text class="pa-2 pa-md-4">
                        <h2 class="text-h5 my-2">Информация о вакансии</h2>
                        <v-row class="mt-2">
                            <v-container class="pa-3 d-flex align-center">
                                <v-img v-if="vacancie.company" class="v_img" :src="base + vacancie.company.avatar"
                                    width="80%" height="100px">
                                </v-img>
                            </v-container>
                        </v-row>
                        <h2 class="text-h5 my-2">Описание</h2>
                        <div class="my-2" v-html="vacancie.information"></div>
                        <v-row>
                            <v-col>
                                <div class="my-3">Требуемый опыт работы: {{ vacancie.work_exp }}</div>
                                <div class="my-3">Предлагаемая з/п: {{ vacancie.salary_min }}-{{ vacancie.salary_max }}
                                    {{ vacancie.currency_type }}</div>
                                <div class="mb-4">
                                    Желательный пол:
                                    {{ vacancie.gender }}
                                </div>
                                <v-row class="d-flex align-end justify-space-between pa-3">
                                    <div v-if="vacancie.tags">
                                        <div class="my-2">Тэги:</div>
                                        <TagList :tags="vacancie.tags" />
                                        <v-spacer></v-spacer>
                                        <div class="caption">
                                            <v-icon small>
                                                mdi-eye-outline
                                            </v-icon>
                                            {{ vacancie.views }}
                                        </div>
                                    </div>
                                    <v-btn width="200px" @click="showContacts" color="primary" small>
                                        <caption>
                                            Контакты
                                        </caption>
                                    </v-btn>
                                </v-row>

                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import Swal from 'sweetalert2'
import TagList from '~/components/UI/TagList.vue'
import { mapState } from 'vuex'
export default {
    components: {
        TagList
    },
    head() {
        let descr = this.vacancie.description,
            title = this.vacancie.title,
            type = 'site',
            image = this.base + this.vacancie?.company?.avatar
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
        this.vacancieId = this.$route.params.id
        if (this.$store.getters['job/getVacancies'].length == 0) {
            this.vacancie = await this.$store.dispatch('job/setVacancies')
        }
        else {
            this.vacancie = await this.$store.getters['job/getVacancies']
        }

        this.vacancie = this.vacancie.find(item => item.id == this.vacancieId)
        this.breadcrumbs.push({
            text: this.vacancieId,
            disabled: true,
            to: `/job/resumes/${this.vacancieId}`,
            exact: true,
        })
    },
    data() {
        return ({

            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                    exact: true,
                },
                {
                    text: 'job',
                    to: '/job',
                    exact: true,
                },
                {
                    text: 'vacancies',
                    to: '/job/vacancies',
                    exact: true,
                }

            ],
            vacancie: {},
            vacancieId: 0
        })
    },
    methods: {
        showContacts() {
            Swal.fire({
                position: 'center',
                icon: 'info',
                title: `${this.vacancie.email}`,
                text: `${this.vacancie.phone}`,
                footer: ` Адрес компании: ${this.vacancie.company.address}`,
                showConfirmButton: false,
                timer: 40000
            })
        }
    },
    computed:{
        ...mapState("auth", ['base'])
    }
}
</script>

<style lang="scss" scoped>
.v_img {
    height: 300px !important;
    width: 80% !important;

    @media screen and(max-width: 800px) {
        width: 100% !important;

        height: 250px !important
    }
}
</style>
