<template>
    <v-card
        class="d-flex align-left align-lg-center my-5"
        hover
        :class="getParityBool(index) ? flexReverse : flexNormal"
        :to="`/directions/${direction.id}`"
    >
        <div>
            <v-card-title>
                {{ direction.full_name }}
            </v-card-title>
            <v-card-text class="text--secondary text-body-1 text-left">
                {{ direction.description }}
            </v-card-text>
        </div>
        <v-spacer/>
        <v-img
            height="300px"
            max-width="550px"
            :class="getParityBool(index) ? 'rl' : 'rr'"
            :src="base + direction.avatar"

        ></v-img>
        <v-chip class="chip">
            <div class="text-caption">
                Кафедра {{ direction.department.name }}
            </div>
        </v-chip>
    </v-card>
</template>

<script>
import {mapState} from "vuex"

export default {
    //Добавить кафедру в chip
    data() {
        return ({
            flexNormal: 'flex-column-reverse flex-lg-row-reverse',
            flexReverse: 'flex-column-reverse flex-lg-row',
        })
    },
    props: {
        direction: {
            type: Object,
            default: {
                img: '',
                name: ''
            }
        },
        index: 0,
    },
    methods: {
        getParityBool(index) {
            return index % 2 == 0
        }
    },
    computed: {
        ...mapState('auth', ['base'])

    }
}
</script>
<style lang="scss" scoped>
.rl {
    border-radius: 100% 0% 90% 16% / 0% 100% 0% 100% !important;
    // border-radius: 1% 1% 1% 8% / 25% 1% 1% 70% !important;
    width: 47% !important;
    max-width: 60% !important;

    @media screen and (max-width: 1264px) {
        border-radius: 1% 1% 0% 0% / 1% 1% 0% 0% !important;
        width: 100% !important;
        max-width: 100% !important;
    }

}

.rr {
    border-radius: 90% 16% 0% 0% / 0% 100% 0% 100% !important;
    // border-radius: 1% 8% 1% 1% / 1% 25% 70% 1% !important;
    width: 60% !important;
    max-width: 50% !important;

    @media screen and (max-width: 1264px) {
        border-radius: 1% 1% 0% 0% / 1% 1% 0% 0% !important;
        width: 100% !important;
        max-width: 100% !important;
    }
}

.chip {
    position: absolute;
    right: 0;
    top: 0;
    transform: translateY(-50%)
}

</style>
