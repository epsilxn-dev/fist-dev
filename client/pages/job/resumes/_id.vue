<template>
    <v-container class="mt-4">
        <v-row v-if="show && resume" no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8 pa-2">
                <h1 class="text-h4 my-2">{{ resume.title }}</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs" />
                <v-card v-if="resume">
                    <v-card-text>
                        <h2 class="text-h5 my-2">Личная информация</h2>
                        <v-row class="mt-2">
                            <v-col
                                class="col col-12 col-md-3 d-flex flex-column"
                            >
                                <v-avatar
                                    class="d-none d-md-block"
                                    tile
                                    size="200px"
                                    color="grey"
                                >
                                    <v-img
                                        tile
                                        class="mx-0 ma-0"
                                        width="100%"
                                        :src="base + resume.image"
                                        color="grey"
                                    >
                                    </v-img>
                                </v-avatar>
                                <div class="d-block d-md-none my-0">
                                    <v-img
                                        tile
                                        class="mx-0 ma-0"
                                        width="100%"
                                        height="300px"
                                        :src="base + resume.image"
                                        color="grey"
                                    ></v-img>
                                </div>
                                <v-btn
                                    width="200px"
                                    class="my-4 align-self-start"
                                    @click="showContacts"
                                    color="primary"
                                    small
                                >
                                    <caption>
                                        Контакты
                                    </caption>
                                </v-btn>
                            </v-col>
                            <v-col class="col">
                                <div class="mb-4">
                                    <!-- {{resume.name}} -->
                                </div>
                                <div class="mb-4">
                                    Пол:
                                    {{ resume.gender }}
                                </div>
                                <div class="mb-4">
                                    О себе <br /><br />
                                    <div
                                        v-if="resume"
                                        v-html="resume.description"
                                    ></div>
                                </div>
                            </v-col>
                        </v-row>
                        <h2 class="text-h5 mb-2">Данные для работодателя</h2>
                        <v-row>
                            <v-col>
                                <div class="my-2">Ключевые навыки:</div>
                                <TagList active="false" :tags="resume.skills" />
                                <div class="my-3">
                                    Опыт работы: {{ resume.work_exp }}
                                </div>
                                <div class="my-3">
                                    Желаемая з/п: {{ resume.salary }}
                                </div>
                                <div class="my-3">
                                    Специальность:
                                    {{ resume.specialization.name }}
                                </div>
                                <div v-if="resume.tags[0] != undefined">
                                    <div class="my-2">Тэги:</div>
                                    <TagList :tags="resume.tags" />
                                </div>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col> </v-col>
        </v-row>
        <v-row v-else no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8 pa-2">
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs" />
                <div class="text-center">
                    Вероятно, резюме не было промодерировано
                </div>
            </v-col>
            <v-col> </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapState } from "vuex";
import Swal from "sweetalert2";
import TagList from "~/components/UI/TagList.vue";
export default {
    components: {
        TagList,
    },
    head() {
        let descr = this.resume.description,
            title = this.resume.title,
            type = "site",
            image = this.base + this.resume.avatar;
        return {
            title: title,
            meta: [
                { hid: "description", name: "description", content: descr },
                { hid: "og:title", name: "og:title", content: descr },
                {
                    hid: "og:description",
                    name: "og:description",
                    content: descr,
                },
                { hid: "og:type", name: "og:type", content: type },
                { hid: "og:image", name: "og:image", content: image },
                { hid: "vk:image", name: "vk:image", content: image },
            ],
        };
    },
    async fetch() {
        this.resumeId = this.$route.params.id;
        this.$axios
            .get(`api/v1/resumes/${this.resumeId}`)
            .then((res) => {
                this.show = true;
                this.resume = res.data.data;
            })
            .catch((res) => {
                this.show = false;
                this.resume = false;
                return;
            });
        this.breadcrumbs[3] = {
            text: this.resumeId,
            exact: "",
            disabled: true,
            to: `/job/resumes/${this.resumeId}`,
        };
    },
    data() {
        return {
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                    exact: true,
                },
                {
                    text: "job",
                    to: "/job",
                    exact: true,
                },
                {
                    exact: true,
                    text: "resumes",
                    to: "/job",
                },
            ],
            show: false,
            resume: false,
            resumeId: 0,
        };
    },
    methods: {
        showContacts() {
            Swal.fire({
                position: "center",
                icon: "info",
                title: `${this.resume.email}`,
                text: `${this.resume.phone}`,
                showConfirmButton: false,
                timer: 40000,
            });
        },
    },
    computed: {
        ...mapState("auth", ["base"]),
    },
};
</script>
