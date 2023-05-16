<template>
    <v-container class="">
        <v-img
            class="mt--2 rb d-flex text-center align-center justify-center"
            :src="require('@/assets/images/img/north_valley.jpeg')"
            dark
            width="100%"
            height="800px"
            gradient="to top right, rgba(0,0,0,.7), rgba(25,32,72,.8)"
        >
            <div class="north_head">
                <h1 class="text-body-1 mb-6">
                    Учебный центр компьютерных технологий "Северная долина"
                </h1>
                <h2 class="text-h3 font-weight-medium">
                    Стань программистом с нуля за год!
                </h2>
                <h2 class="text-body-1 mt-6">
                    Профессиональные курсы переподготовки по ИТ для взрослых от
                    ведущего ИТ-вуза региона!
                </h2>
                <v-btn class="mt-6" color="primary" v-scroll-to="'#form'">
                    записаться
                    <v-icon dark class="ml-1 mr-0"> mdi-chevron-down </v-icon>
                </v-btn>
            </div>
        </v-img>
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-sm-flex"></v-col>
            <v-col class="col col-md-8 col-sm-12 px-2">
                <h3 class="text-h4 mt-10 my-4 text-center">Для кого?</h3>
                <div class="text-center text--secondary my-4">
                    Для всех, кто хочет переквалифицироваться в программиста.
                </div>
                <div
                    class="for_who d-flex justify-space-between flex-md-row flex-xs-column flex-sm-column"
                >
                    <v-card
                        hover
                        min-width="31%"
                        class="my-2 my-sm-5 mr-0 mr-sm-2"
                    >
                        <v-img
                            class="rb"
                            :src="require('@/assets/images/img/photo-4.jpg')"
                            height="200px"
                        ></v-img>
                        <v-card-title> Выпускникам </v-card-title>
                        <v-card-text>
                            Тем, кто давно окончил вуз или СПО и хочет сменить
                            профессию.
                        </v-card-text>
                    </v-card>
                    <v-card
                        hover
                        min-width="31%"
                        class="my-2 my-sm-5 mr-0 mr-sm-2"
                    >
                        <v-img
                            class="rb"
                            :src="require('@/assets/images/img/photo-5.jpg')"
                            height="200px"
                        ></v-img>
                        <v-card-title> Студентам </v-card-title>
                        <v-card-text>
                            Тем, кто учится не по ИТ профилю.
                        </v-card-text>
                    </v-card>
                    <v-card
                        hover
                        min-width="31%"
                        class="my-2 my-sm-5 mr-0 mr-sm-2"
                    >
                        <v-img
                            class="rb"
                            :src="require('@/assets/images/img/photo-6.jpg')"
                            height="200px"
                        ></v-img>
                        <v-card-title> ИТ-специалистам </v-card-title>
                        <v-card-text>
                            Тем, кто уже работает в ИТ, но не хватает базовой
                            подготовки.
                        </v-card-text>
                    </v-card>
                </div>
            </v-col>
            <v-col class="d-none d-sm-flex" />
        </v-row>
        <v-row class="back-dark">
            <v-col class="col col-2 d-none d-sm-flex"></v-col>
            <v-col class="col col-md-8 col-sm-12 pa-2">
                <div
                    class="reasons d-flex align-center flex-xs-column justify-center mt-10"
                >
                    <ProgrammCard class="ml-8 ml-sm-0 w-50 card" />
                    <div class="ml-5 w-40 card-container">
                        <div class="text-h4 mt-5 text-center text-sm-left">
                            Зачем?
                        </div>
                        <div
                            class="text-h6 mt-5 text--secondary text-center text-sm-left font-weight-regular"
                        >
                            Чтобы освоить профессию веб-программиста, получить
                            базовую подготовку в ИТ и устроиться на
                            высокооплачиваемую работу в одну из более чем 200
                            ИТ-компаний Ульяновска или в другие компании России
                            и мира.
                        </div>
                        <div
                            class="text-body-1 text-center text-sm-left mt-5 text--secondary"
                        >
                            Посмотрите актуальные ульяновские вакансии на
                            <a
                                href="https://ulyanovsk.hh.ru/search/vacancy?area=1614&clusters=true&enable_snippets=true&specialization=1.221&only_with_salary=true&salary=100000&from=cluster_compensation&showClusters=true"
                                >hh.ru
                                <v-icon color="primary">
                                    mdi-open-in-new</v-icon
                                ></a
                            >
                        </div>
                    </div>
                </div>
                <div class="who mt-10 px-2">
                    <div class="text-h4 text-center pt-10">
                        Кто проводит курсы?
                    </div>
                    <v-card
                        class="d-flex align-center flex-xs-column my-8"
                        hover
                    >
                        <v-img
                            max-height="250px"
                            class="rr who_img"
                            :src="
                                require('@/assets/images/img/simbirsoft.jpeg')
                            "
                        ></v-img>
                        <div>
                            <v-card-title
                                >УлГТУ совместно с Simbirsoft</v-card-title
                            >
                            <v-card-text class="text--secondary text-body-1">
                                SimbirSoft - крупнейшая ИТ-компания Ульяновска.
                                20 лет на рынке, входит в TOP 100 лучших
                                разработчиков-аутсорсеров мира, более 900
                                сотрудников в разных городах России, более 900
                                реализованных проектов.
                            </v-card-text>
                        </div>
                        <v-chip class="chip"> Лидер ИТ-отрасли </v-chip>
                    </v-card>
                    <v-card
                        class="d-flex flex-xs-column-reverse align-center my-5"
                        hover
                    >
                        <div>
                            <v-card-title class="word-wrap">
                                Факультет информационных систем и технологий
                                УлГТУ.
                            </v-card-title>
                            <v-card-text class="text--secondary text-body-1">
                                SimbirSoft - крупнейшая ИТ-компания Ульяновска.
                                20 лет на рынке, входит в TOP 100 лучших
                                разработчиков-аутсорсеров мира, более 900
                                сотрудников в разных городах России, более 900
                                реализованных проектов.
                            </v-card-text>
                        </div>
                        <v-img
                            class="rl who_img"
                            max-height="250px"
                            :src="require('@/assets/images/img/fist.jpg')"
                        >
                        </v-img>
                        <v-chip class="chip"> Лидер ИТ-образования </v-chip>
                    </v-card>
                </div>
                <div class="placer" />
            </v-col>
            <v-col class="col-md-2 d-none d-sm-flex" />
        </v-row>
        <v-row>
            <v-col class="col col-2 d-none d-sm-flex"></v-col>
            <v-col class="col col-md-8 col-sm-12">
                <div class="time mt-10">
                    <div class="text-h4 text-center mb-10">
                        Сколько это займёт времени?
                    </div>
                    <div
                        class="text-center d-flex justify-center flex-xs-column align-center mb-10"
                    >
                        <div class="w-30">
                            <div class="text-h3 font-weight-bold primary--text">
                                9
                            </div>
                            <div class="text--secondary my-5 mb-10">
                                Месяцев обучения в течение года
                            </div>
                        </div>
                        <div class="w-30">
                            <div class="text-h3 font-weight-bold primary--text">
                                9-12
                            </div>
                            <div class="text--secondary my-5">
                                Часов в неделю, включая самостоятельную работу.
                            </div>
                        </div>
                        <div class="w-30">
                            <div class="text-h3 font-weight-bold primary--text">
                                2
                            </div>
                            <div class="text--secondary my-5">
                                Очных занятия в неделю по 3 часа каждое в
                                вечернее время.
                            </div>
                        </div>
                    </div>
                </div>
                <div class="placer" />
                <div
                    class="cost d-flex flex-xs-column text-center align-center"
                >
                    <div class="d-flex flex-column align-center mr-5">
                        <div class="text-h4 primary--text">
                            Сколько это стоит?
                        </div>
                        <p class="mt-4 text-body">
                            <b>60000</b> рублей за год. Возможна "посеместровая"
                            или ежемесячная оплата.
                        </p>
                        <p class="text--secondary text-body">
                            Это меньше одной зарплаты программиста среднего
                            уровня за месяц. По окончании обучения выдается
                            диплом о профессиональной переподготовке
                            государственного образца.
                        </p>
                    </div>
                    <v-img
                        :src="require('@/assets/images/img/illustration-3.png')"
                        class="ml-5 cost_img"
                    ></v-img>
                </div>
                <div class="placer" />
            </v-col>
            <v-col class="col col-2 d-none d-sm-flex"></v-col>
        </v-row>
        <v-row class="why_real back-dark">
            <v-col class="col col-2 col-md-2 d-none d-sm-flex"></v-col>
            <v-col class="col col-md-8 col-sm-12 px-2">
                <div class="white--text py-10 pa-4 pa-sm-10">
                    <div class="text-h4 w-50 mt-5">
                        Почему очное обучение лучше дистанционного?
                    </div>
                    <div class="mt-5 real--secondary">
                        Коммуникация - важнейший аспект обучения профессии.
                        Профессиональный преподаватель и наставник помогут в
                        освоении программы обучения и при выполнении проекта.
                    </div>
                    <div
                        class="align-center d-none d-sm-flex py-4 pb-0 justify-left text-center"
                    >
                        <div class="dot">1</div>
                        <v-divider dark></v-divider>
                        <div class="dot">2</div>
                        <v-divider dark></v-divider>

                        <div class="dot">3</div>
                        <v-spacer></v-spacer>
                    </div>
                    <div
                        class="d-flex align-start py-4 flex-xs-column justify-start text-left"
                    >
                        <div class="w-30">
                            <div
                                class="mb-4 mt-2 d-flex d-sm-none align-center"
                            >
                                <div class="dot mr-2">1</div>
                                Знания
                            </div>
                            <div class="mr-5 real--secondary">
                                Получение системных знаний в области
                                программирования и принципов функционирования
                                ИТ-систем.
                            </div>
                        </div>
                        <v-spacer></v-spacer>
                        <div class="w-30">
                            <div
                                class="mb-4 mt-2 d-flex d-sm-none align-center"
                            >
                                <div class="dot mr-2">2</div>
                                Прагматичность
                            </div>
                            <div class="mr-5 real--secondary">
                                В ИТ-компаниях нужны люди, которые умеют решать
                                проблемы, а не просто переводить требования ТЗ в
                                программный код. На ФИСТ УлГТУ мы учим решать
                                задачи.
                            </div>
                        </div>
                        <v-spacer></v-spacer>
                        <div class="w-30">
                            <div
                                class="mb-4 mt-2 d-flex d-sm-none align-center"
                            >
                                <div class="dot mr-2">3</div>
                                Опыт
                            </div>
                            <div class="mr-5 real--secondary">
                                Большой объем информации по новой профессии
                                усвоить очень тяжело. Мы умеем объяснять сложные
                                вещи простыми словами.
                            </div>
                        </div>
                    </div>
                </div>
            </v-col>
            <v-col class="col col-2 d-none d-sm-flex"></v-col>
        </v-row>
        <v-row>
            <v-col class="col col-2 d-none d-sm-flex" />
            <v-col class="col col-md-8 col-sm-12 px-2">
                <div class="text-h4 text-center">Чему учиться?</div>
                <HoursTable class="back-dark mt-10" />
            </v-col>
            <v-col class="col col-2" />
        </v-row>
        <v-row class="back-dark">
            <v-col class="col col-2 d-none d-sm-flex" />
            <v-col class="col col-md-8 col-sm-12 px-2">
                <v-container
                    class="d-flex justify-center align-center flex-column"
                >
                    <div class="text-h4 text-center">Запишитесь на курсы!</div>
                    <div
                        id="form"
                        class="text-body mt-4 text--secondary text-center"
                    >
                        Заполните форму, мы обязательно свяжемся в Вами и все
                        расскажем.
                    </div>
                    <NorthForm @submitForm="submitForm" class="my-10 w-50" />
                </v-container>
            </v-col>
            <v-col class="col col-2 d-none d-sm-flex" />
        </v-row>
    </v-container>
</template>

<script>
import Swal from "sweetalert2";
import TagList from "@/components/UI/TagList";
import StackList from "@/components/labs/StackList";
import ProjectList from "@/components/labs/ProjectList";
import ProgrammCard from "@/components/north/ProgrammCard";
import HoursTable from "@/components/north/HoursTable";
import NorthForm from "@/components/north/NorthForm";
import { mapState } from "vuex";
import axios from "axios";

export default {
    head() {
        let descr =
                "Профессиональные курсы переподготовки по ИТ для взрослых от ведущего ИТ-вуза региона!",
            title = "Северная долина",
            type = "site",
            image = this.base + "assets/images/img/north_valley.jpeg";
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
    components: {
        TagList,
        StackList,
        NorthForm,
        ProjectList,
        ProgrammCard,
        HoursTable,
    },
    data() {
        return {
            info: {},
            err: "",
        };
    },
    methods: {
        submitForm(info) {
            this.info = info;

            this.$axios
                .post("api/v1/northvalley/", info)
                .then((res) => {})
                .catch((err) => {
                    this.error = err;
                });
        },
    },
    computed: {
        ...mapState("auth", ["base"]),
    },
};
</script>

<style lang="scss" scoped>
.who_img {
    width: 47%;
    @media screen and (max-width: 600px) {
        width: 100% !important;
    }
}
.back-dark {
    background-color: #f5f7fa;
}
.w-30 {
    width: 30%;
    @media screen and (max-width: 600px) {
        width: 100% !important;
    }
}
.dot {
    background-color: #282f3f;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    width: 40px;
    height: 40px;
}
.placer {
    height: 100px;
    width: 100%;
    @media screen and (max-width: 600px) {
        height: 20px !important;
    }
}
.w-50 {
    width: 50% !important;
    @media screen and (max-width: 600px) {
        width: 95% !important;
    }
}
.cost_img {
    width: 45%;
    @media screen and (max-width: 600px) {
        width: 95% !important;
    }
}
.w-40 {
    width: 40% !important;
    @media screen and (max-width: 600px) {
        width: 95% !important;
    }
}
.card-container {
    transform-origin: y x;
    transform-style: preserve-3d;
    perspective: 400px;
}

.word-wrap {
    word-break: keep-all !important;
}
.rl {
    border-radius: 100% 0% 90% 16% / 0% 100% 0% 100% !important;
    @media screen and (max-width: 600px) {
        border-radius: 0 !important;
    }
}
.rr {
    border-radius: 90% 16% 0% 0% / 0% 100% 0% 100% !important;
    @media screen and (max-width: 600px) {
        border-radius: 0 !important;
    }
}
.card {
    transform-style: preserve-3d;
    perspective: 100px;
    transform-origin: y x;
    transform: perspective(400px) rotate3d(0, 12, -4, 12deg) scale(0.9);
}
.chip {
    position: absolute;
    right: 0;
    top: 0;
    transform: translateY(-50%);
}
.rb {
    clip-path: ellipse(100% 52% at 49% 45%);
    @media screen and (max-width: 600px) {
        clip-path: none;
    }
}

.why_real {
    background-color: #161c2d;
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 86%);
    @media screen and (max-width: 600px) {
        clip-path: polygon(0 0, 100% 0, 100% 100%, 0 95%);
    }
}
.real--secondary {
    color: #73849e;
}
</style>
