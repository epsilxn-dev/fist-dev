<template>
    <v-container class="">
        <v-img
            class="mt--2 d-flex text-center align-center justify-center rb"
            src="https://sun9-14.userapi.com/impf/c627530/v627530609/19ba9/Q0O2zmIgjQY.jpg?size=999x2048&quality=96&sign=9961ab09a328bf7add9bfd75891b1449&type=album"
            dark
            width="100%"
            height="800px"
            gradient="to top right, rgba(0,0,0,.7), rgba(25,32,72,.8)"
        >
            <div class="school__header mx-auto">
                <div class="subtitle text-body-1 my-4">
                    КШ ФИСТ(Факультета "Информационных систем и технологий")
                </div>
                <h1 class="text-h4 text-md-h2 my-7 font-weight-medium">
                    Компьютерная школа ФИСТ
                </h1>
                <div class="subtitle text-body-1 my-6">
                    входящая в состав "Детской Юношеской Инженерной Академии"
                    УлГТУ
                    <br />
                    Приглашает школьников 6-11 классов
                </div>
            </div>
        </v-img>
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-flex"></v-col>
            <v-col class="col col-12 col-md-8 pa-2">
                <h1 class="text-h5 text-md-h4 my-2 text--primary">
                    Направления подготовки
                </h1>
                <v-breadcrumbs class="pa-0 pb-2 mb-2" :items="breadcrumbs" />
                <v-container class="pb-2">
                    <CSDirectonItem
                        v-for="(direction, index) in computerSchoolDirections"
                        :key="index"
                        :item="direction"
                    />
                </v-container>
                <h2 class="text-h5 my-2">Как с нами связаться?</h2>
                <CSWidger class="d-flex d-md-none" v-if="isLoaded" />
                <CSBadgeList :items="computerSchoolBadges" />
            </v-col>
            <v-col class="d-none d-md-flex">
                <div id="vk_community_messages"></div>
                <CSWidger v-if="isLoaded" />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import CSBadgeList from "@/components/computer_school/CSBadgeList.vue";
import CSDirectonItem from "@/components/computer_school/CSDirectonItem.vue";
import CSWidger from "@/components/computer_school/CSWidger.vue";
export default {
    async fetch() {
        await this.$store.dispatch("cs/setDirections");
        this.computerSchoolDirections = await this.$store.getters[
            "cs/getDirections"
        ];
    },
    mounted() {
        this.isLoaded = true;
    },
    head() {
        let descr = `Компьютерная школа ФИСТ
            входящая в состав "Детской Юношеской Инженерной Академии" УлГТУ
            Приглашает школьников 6-11 классов`,
            title = "КШ ФИСТ",
            type = "site",
            image =
                "https://sun9-14.userapi.com/impf/c627530/v627530609/19ba9/Q0O2zmIgjQY.jpg?size=999x2048&quality=96&sign=9961ab09a328bf7add9bfd75891b1449&type=album";
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
            script: [
                {
                    src: "https://vk.com/js/api/openapi.js?169",
                    type: "text/javascript",
                    defer: true,
                },
            ],
        };
    },
    components: {
        CSDirectonItem,
        CSBadgeList,
        CSWidger,
    },
    data() {
        return {
            isLoaded: false,
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                },
                {
                    text: "computer_school",
                    to: "/computer_school",
                    exact: true,
                },
            ],
            computerSchoolDirections: [],
            computerSchoolBadges: [
                {
                    name: "Группа КШ ФИСТ",
                    image: "https://sun9-14.userapi.com/impf/c627530/v627530609/19ba9/Q0O2zmIgjQY.jpg?size=999x2048&quality=96&sign=9961ab09a328bf7add9bfd75891b1449&type=album",
                    to: "https://vk.com/fist_school",
                },
                {
                    name: "Лылова А.В",
                    image: "https://sun7-8.userapi.com/impf/c855320/v855320092/f6877/udTCsvJDfKw.jpg?size=1440x2160&quality=96&sign=eb9d4239625ddfdfa109e1655d0b05f1&type=album",
                    to: "https://vk.com/id197179609",
                },
            ],
        };
    },
};
</script>
<style lang="scss" scoped>
.hr {
    border: none;
    background-color: white;
    color: white;
    transform: scaleY(0.8);
    height: 1px;
}
.school__header {
    max-width: 60%;
    @media screen and (max-width: 800px) {
        max-width: 95%;
    }
}
.rb {
    clip-path: ellipse(100% 52% at 49% 45%);
    @media screen and (max-width: 600px) {
        clip-path: none;
    }
}
</style>
