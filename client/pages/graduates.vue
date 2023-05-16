<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="d-md-flex d-none" />
            <v-col class="col col-12 col-md-8">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4 title text--primary">Выпускники</h1>
                </v-row>
                <v-breadcrumbs
                    class="pa-0 pb-2"
                    :items="breadcrumbs"
                ></v-breadcrumbs>
                <v-container
                    v-if="graduates.length"
                    class="d-flex justify-start flex-wrap"
                >
                    <GraduatesCard
                        v-for="(grad, index) in graduates"
                        :key="index"
                        :item="grad"
                        class="grad_card mt-2 mr-0 mr-md-2 mb-2"
                    ></GraduatesCard>
                </v-container>
                <NoInfo v-else />
            </v-col>
            <v-col class="d-md-flex d-none" />
        </v-row>
    </v-container>
</template>
<script>
import GraduatesCard from "@/components/graduates/GraduatesCard.vue";
import NoInfo from "~/components/UI/NoInfo.vue";
export default {
    components: {
        GraduatesCard,
        NoInfo,
    },
    head() {
        let descr = "Выпускники факультета информационных систем и технологий",
            title = "Выпускники",
            type = "site";
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
            ],
        };
    },
    async fetch() {
        this.graduates = await this.$store.dispatch("graduates/setGraduates");
        this.directions = await this.$store.getters["directions/getDirections"];

        for (let d of this.directions) {
            this.directionsColors[d.name] = this.colors[d.id];
        }
        for (let g of this.graduates) {
            g.directionColor = this.directionsColors[g.direction];
        }
    },
    data() {
        return {
            news: [],
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                },
                {
                    text: "graduates",
                    disabled: true,
                    exact: true,
                    to: "/graduates",
                },
            ],
            colors: [
                "primary",
                "success",
                "red",
                "green",
                "cyan",
                "indigo",
                "deep-purple",
            ],
            graduates: [],
            directions: [],
            directionsColors: [],
        };
    },
};
</script>
<style lang="scss" scoped>
.grad_card {
    width: 31.2% !important;
    @media screen and (max-width: 600px) {
        width: 98% !important ;
    }
}
</style>
