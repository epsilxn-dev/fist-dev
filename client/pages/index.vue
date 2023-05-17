<template>
    <v-container v-if="show" class="">
        <v-img
            class="mt--2 d-flex text-center align-center justify-center rb"
            :src="require('@/assets/images/img/mainPreview.png')"
            dark
            width="100%"
            height="800px"
            gradient="to top right, rgba(0,0,0,.7), rgba(25,32,72,.8)"
        >
            <div class="main__header mx-auto">
                <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">
                    Факультет информационных систем и технологий УлГТУ
                </h1>
                <div class="main__header_description mx-auto mt-8">
                    <h2 class="subtitle text-h5 mb-8 text-center">
                        В 2022 году на ФИСТ выделено 322 бюджетных места! Это
                        почти в 2 раза больше, чем в 2020 году. Поступить стало
                        проще!
                    </h2>
                    <h3 class="subtitle text-h6 text-center">
                        А еще мы проводим
                        <NuxtLink class="subtitle text-h6" to="northvalley">
                            переподготовку взрослых
                        </NuxtLink>
                        и
                        <NuxtLink class="subtitle text-h6" to="computer_school">
                            обучение ИТ-технологиям детей </NuxtLink
                        >!
                    </h3>
                </div>
            </div>
        </v-img>
        <v-row no-gutters class="mb-8 px-2">
            <v-col class="col col-2 d-none d-flex"></v-col>
            <v-col class="col col-lg-8 col-12">
                <v-row
                    no-gutters
                    class="mt-4 mx-4 d-flex justify-space-between flex-md-row flex-column"
                >
                    <div
                        v-for="(advantage, index) in advantages"
                        :key="index"
                        class="d-flex flex-column justify-center align-center my-2"
                    >
                        <h3 class="text-h2 text--secondary font-weight-bold">
                            {{ advantage.hight }}
                        </h3>
                        <div class="text--secondary">{{ advantage.low }}</div>
                    </div>
                </v-row>
                <v-row
                    no-gutters
                    class="my-10 d-flex flex-column justify-center align-center"
                >
                    <h3
                        class="text--secondary text-h5 font-weight-bold ma-5 text-center"
                    >
                        Высшее образование это не просто диплом
                    </h3>
                    <div class="text--secondary max__width_80 text-center">
                        На ФИСТ УлГТУ мы готовим специалистов, способных решать
                        сложные задачи с использованием системных знаний в ИТ и
                        инженерии. Мы учим определять цели, основанные на
                        ценностях в бизнесе, а также создавать ИТ-решения для
                        достижения этих целей.
                    </div>
                </v-row>
                <v-container>
                    <div
                        class="d-flex justify-space-between flex-md-row flex-column align-md-stretch align-center"
                    >
                        <v-card
                            hover
                            class="d-flex align-center flex-lg-row flex-column my-5 py-10 mr-md-4 mr-0"
                            min-width="48%"
                        >
                            <v-img
                                :src="
                                    require('@/assets/images/img/mainKnowledge.png')
                                "
                                width="220px"
                                height="200px"
                                contain
                            >
                            </v-img>
                            <div class="d-flex align-center flex-column">
                                <v-card-title>Знания</v-card-title>
                                <v-card-text
                                    class="text--secondary body-1 font-weight-medium text-lg-left text-center"
                                >
                                    Получение системных знаний в области
                                    программирования и принципов проектирования
                                    ИТ-систем.
                                </v-card-text>
                            </div>
                        </v-card>
                        <v-card
                            hover
                            class="d-flex align-center flex-lg-row flex-column-reverse my-5 py-10 ml-md-4 mr-0"
                            min-width="48%"
                        >
                            <div class="d-flex align-center flex-column">
                                <v-card-title>Прагматизм</v-card-title>
                                <v-card-text
                                    class="text--secondary body-1 font-weight-medium text-lg-left text-center"
                                >
                                    В ИТ-компаниях нужны люди, которые умеют
                                    решать проблемы, а не просто писать код. Мы
                                    учим выявлять проблемы и решать их.
                                </v-card-text>
                            </div>
                            <v-img
                                :src="
                                    require('@/assets/images/img/mainPragmatism.png')
                                "
                                width="220px"
                                height="200px"
                                contain
                            >
                            </v-img>
                        </v-card>
                    </div>
                    <v-card
                        hover
                        class="d-flex align-center flex-md-row flex-column my-5 py-10"
                    >
                        <v-img
                            :src="
                                require('@/assets/images/img/mainExperience.png')
                            "
                            width="350px"
                            height="250px"
                            class="ml-5"
                            contain
                        >
                        </v-img>
                        <div
                            class="d-flex align-md-start align-center flex-column"
                        >
                            <v-card-title>Опыт</v-card-title>
                            <v-card-text
                                class="text--secondary body-1 font-weight-medium text-md-left text-center"
                            >
                                Мы работаем в сотрудничестве с ведущими
                                российскими ИТ-компаниями и предприятиями. Во
                                время обучения у студентов много возможностей
                                научиться решать реальные и полезные задачи.
                                Можно поступить по договору целевого обучения.
                            </v-card-text>
                        </div>
                    </v-card>
                </v-container>
                <v-row id="directions" no-gutters class="overflow-hidden">
                    <div
                        v-if="directions?.length > 0"
                        class="my-10 d-flex justify-center flex-column"
                        style="max-width: 100%"
                    >
                        <h3
                            class="text--secondary text-h5 font-weight-bold text-center"
                        >
                            Направления подготовки
                        </h3>
                        <div class="text--secondary text-center">
                            <v-container style="padding: 1rem;">
                                <DirectionItem
                                    v-for="(direction, index) in directions"
                                    :key="index"
                                    :direction="direction"
                                    :index="index"
                                    class="my-4"
                                ></DirectionItem>
                            </v-container>
                        </div>
                    </div>
                </v-row>
                <v-row
                    v-if="labs?.length > 0"
                    no-gutters
                    class="my-10 d-flex flex-column justify-center align-center"
                >
                    <h3
                        class="text--secondary text-h5 font-weight-bold ma-5 text-center"
                    >
                        Лаборатории факультета
                    </h3>
                    <div class="text--secondary max__width_80 text-center">
                        <v-container
                            class="pb-2 d-flex flex-wrap justify-space-between"
                        >
                            <LabCard
                                v-for="(item, index) in labs"
                                class="labs_item mt-4"
                                :lab="item"
                                :key="index"
                            ></LabCard>
                        </v-container>
                        <v-container
                            class="d-flex mt-4 justify-center align-center"
                        >
                            <v-btn color="primary" nuxt to="/labs">
                                Показать все
                            </v-btn>
                        </v-container>
                    </div>
                </v-row>
                <v-row
                    no-gutters
                    class="mt-10 d-flex flex-column justify-center align-center"
                >
                    <h3
                        class="text--secondary text-h5 font-weight-bold text-center mt-5"
                    >
                        Есть вопросы? Добро пожаловать в раздел "Часто
                        задаваемых вопросов"!
                    </h3>
                </v-row>
                <div
                    v-for="(value, name) in questions"
                    class="pt-4"
                    :key="name"
                >
                    <div v-if="value.length !== 0" class="py-4">
                        <v-chip>{{ name }}</v-chip>
                    </div>
                    <v-expansion-panels
                        v-for="(item, index) in value"
                        :key="index"
                    >
                        <v-expansion-panel class="mb-1">
                            <v-expansion-panel-header>
                                {{ item.question }}
                            </v-expansion-panel-header>
                            <v-expansion-panel-content>
                                {{ item.answer }}
                                <TagList :tags="item.tags" />
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </div>
                <v-container class="d-flex mt-8 justify-center align-center">
                    <v-btn color="primary" nuxt to="/faq">
                        Посмотреть все вопросы
                    </v-btn>
                </v-container>
            </v-col>
            <v-col class="d-none d-sm-flex"> </v-col>
        </v-row>
    </v-container>
</template>

<script>
import DirectionItem from "@/components/main/DirectionItem.vue";
import LabCard from "@/components/labs/LabCard";
import TagList from "@/components/UI/TagList";
import { mapState } from "vuex";
export default {
    components: {
        DirectionItem,
        LabCard,
        TagList,
    },
    async fetch() {
        this.show = true;
        await this.$axios
            .get("api/v1/specialties/", {
                headers: {
                    Authorization: `Bearer ${this.accessToken}`,
                },
            })
            .then((res) => {
                this.directions = res.data.data.results;
            })
            .catch((err) => {
                this.error = err;
            });
        await this.$store.dispatch("labs/setLabs").then((res) => {
            this.labs = res.slice(0, this.toShowLabs);
        });

        await this.$store.dispatch("faq/setQuestions").then((res) => {});
        this.questions = this.$store.getters["faq/getQuestions"];
        this.groupQuestions();
        this.show = true;
    },
    data() {
        return {
            directions: [],
            advantages: [
                {
                    hight: 1500,
                    low: "студентов",
                },
                {
                    hight: 4,
                    low: "кафедры",
                },
                {
                    hight: 6,
                    low: "направлений",
                },
                {
                    hight: "90%",
                    low: "трудоустройство",
                },
                {
                    hight: 322,
                    low: "бюджетных места",
                },
            ],
            labs: [],
            toShowLabs: 4,
            questions: [],
            show: false,
        };
    },
    methods: {
        groupQuestions() {
            let themes = [];
            let groupedQuestions = {};
            for (let quest of this.questions) {
                let currentTheme = quest.theme;
                if (themes.includes(currentTheme)) {
                    groupedQuestions[currentTheme].push({
                        question: quest.question,
                        answer: quest.answer,
                        tags: quest.tags,
                    });
                } else {
                    groupedQuestions[currentTheme] = [
                        {
                            question: quest.question,
                            answer: quest.answer,
                            tags: quest.tags,
                        },
                    ];
                }
                themes.push(currentTheme);
            }
            this.questions = groupedQuestions;
        },
    },
    computed: {
        ...mapState("auth", ["accessToken"]),
    },
};
</script>
<style lang="scss" scoped>
.main__header {
    max-width: 55%;

    @media screen and (max-width: 600px) {
        max-width: 100%;
    }
}

.main__header_description {
    max-width: 90%;
}

.max__width_80 {
    max-width: 80%;
}

.rb {
    clip-path: ellipse(100% 52% at 49% 45%);

    @media screen and (max-width: 600px) {
        clip-path: none;
    }
}
</style>
