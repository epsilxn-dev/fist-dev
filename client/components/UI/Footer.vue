<template>
    <v-footer
        dark
        padless
    >
        <v-card
            flat
            tile
            class="white--text text-center bg__footer"
        >
            <div class="d-flex flex-column flex-sm-row justify-space-around my-4">
                <v-card-text v-for="(item, index) in contactItems" :key="index" class="d-flex flex-column align-center">
                    <v-btn
                        class="mx-2"
                        fab
                        color="#161c2d"
                        depressed
                        large
                        :href="item.action"
                        >
                        <v-icon dark large>
                            {{item.icon}}
                        </v-icon>
                    </v-btn>
                    <v-card-text class="pt-2 pb-2" v-for="(desc, indexDesc) in item.description" :key="indexDesc">
                        {{desc}}
                    </v-card-text>
                </v-card-text>
            </div>
            <v-divider></v-divider>
            <v-card-text class="white--text my-2">
                {{ new Date().getFullYear() }} — ФИСТ УлГТУ
            </v-card-text>
        </v-card>
    </v-footer>
</template>
<script>
export default {
    data() {
        return {
            contactItems: [
                {
                    icon: 'mdi-walk',
                    description: ['г. Ульяновск, ул. Северный Венец, 32, 3-ий корпус, ауд. 419'],
                    action: 'https://yandex.ru/maps/195/ulyanovsk/?ll=48.390124%2C54.350887&mode=poi&poi%5Bpoint%5D=48.387666%2C54.352498&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1062524416&z=15',
                },
                {
                    icon: 'mdi-phone-in-talk',
                    description: ['+7 (8422) 778-085','Деканат ФИСТ УлГТУ'],
                    action: 'tel:+79023573567'
                },
                {
                    icon: 'mdi-email',
                    description: ['fist@ulstu.ru'],
                    action: 'mailto:fist@ulstu.ru'
                }
            ]
        }
    },
}
</script>
<style scoped>
.bg__footer {
    background-color: #161c2d;
    width: 100%;
}
.pointer__cursor:hover{
cursor: auto;
}
</style>