<template>
    <v-card class="d-flex flex-column mb-3">
        <div class="d-flex flex-column flex-md-row justify-space-between">
            <div>
                <v-card-title>
                    {{ vacancie.title || vacancie.name }}
                </v-card-title>
                <div class="d-block d-md-none pa-2 my-0">
                    <v-img tile contain class="ma-0" width="100%" height="200px" v-if='vacancie.company'
                        :src="vacancie.hh ? vacancie.company.avatar : base + vacancie.company.avatar" color="grey">
                    </v-img>
                </div>
                <v-card-text class="d-flex flex-column align-left justify-space-between">
                    <div class="my-2">
                        <span v-if="!vacancie.hh">Требуемый стаж:</span> <span class="deep-purple--text"
                            v-html="vacancie.work_exp"></span>
                    </div>
                    <div v-html="vacancie.description" />
                    <div class="subtitle-1 my-2">
                        Оплата:
                        <span v-if="vacancie.salary_min || vacancie.salary_max" class="deep-purple--text ">
                            {{ vacancie.salary_min }}
                            <span v-if="vacancie.salary_min && vacancie.salary_max">-</span>
                            {{ vacancie.salary_max }} {{ vacancie.currency_type }}
                        </span>
                        <span v-else class="deep-purple--text ">Не указана</span>
                    </div>
                    <TagList v-if="vacancie.tags" class="justify-self-end" :tags="vacancie.tags" />
                </v-card-text>
            </div>
            <div class="d-none d-md-block">
                <v-avatar tile class="ma-4" size="150" color="white">
                    <v-img contain v-if='vacancie.company'
                        :src="vacancie.hh ? vacancie.company.avatar : base + vacancie.company.avatar"></v-img>
                </v-avatar>
            </div>

        </div>
        <v-card-actions>
            <v-card-text>
                {{ vacancie.created_at }}
            </v-card-text>
            <v-spacer></v-spacer>
            <v-btn v-if="vacancie.hh" :href="vacancie.alternate_url" color="primary lighten-2" text small>
                просмотреть
            </v-btn>
            <v-btn nuxt v-else :to="`/job/vacancies/${vacancie.id}`" color="primary lighten-2" text small>
                просмотреть
            </v-btn>
        </v-card-actions>
    </v-card>
</template>


<script>
import TagList from '@/components/UI/TagList'
import { mapState } from 'vuex'
export default {
    components: {
        TagList
    },
    props: {
        vacancie: {
            type: Object,
            required: true
        }
    },
    computed: {
        ...mapState('auth', ['base'])

    }
}
</script>

