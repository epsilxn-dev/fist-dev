<template>
    <v-container v-if="user" class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-8">
                <h1 class="text-h4 my-2">Предложить идею</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs" />
                <v-card>
                    <v-card-text class="pa-2 pa-md-4">
                        <v-container class="avatar_input mt-4">
                            <ImageInput :background="background" @change="setImage" :rules="rules" />
                        </v-container>
                        <v-container>
                            <h2 class="text-h5 my-2">Краткая информация</h2>
                            <v-text-field @input="$v.idea.name.$touch()" @blur="$v.idea.name.$touch()"
                                :error-messages="nameErrors" clearable v-model="idea.name" class="mt-3" solo
                                counter="30" label="Название идеи"></v-text-field>
                            <v-textarea @input="$v.idea.description.$touch()" @blur="$v.idea.description.$touch()"
                                :error-messages="descriptionErrors" outlined hint="Эта информация будет в карточке"
                                label="Краткое описание" class='mt-1' v-model="idea.description" />

                            <h2 class="text-h5 mb-2">Развёрнутая информация</h2>
                            <v-card class="mb-5"
                                :class="{ redBorder: $v.idea.information.$dirty && $v.idea.information.$invalid }">
                                <div @click="$v.idea.information.$touch()">
                                    <wysiwyg v-model="idea.information" />
                                </div>
                            </v-card>
                            <v-combobox v-model="idea.links" chips clearable label="Полезные ссылки" multiple required
                                outlined>
                                <template v-slot:selection="{ attrs, item, select, selected }">
                                    <v-chip v-bind="attrs" :input-value="selected" close @click="select" small
                                        @click:close="removeLink(item)">
                                        <div class="caption">{{ item }}</div>&nbsp;
                                    </v-chip>
                                </template>
                            </v-combobox>
                            <v-combobox v-model="idea.area_tech" chips clearable label="Стек технологий" multiple
                                required outlined>
                                <template v-slot:selection="{ attrs, item, select, selected }">
                                    <v-chip v-bind="attrs" :input-value="selected" close @click="select" small
                                        @click:close="remove(item)">
                                        <div class="caption">{{ item }}</div>&nbsp;
                                    </v-chip>
                                </template>
                            </v-combobox>
                            <h2 class="text-h5 my-2">Команда</h2>
                            <v-autocomplete v-model="idea.team" :items="users" :search-input.sync="search" chips
                                small-chips label="Укажите username" multiple outlined></v-autocomplete>
                        </v-container>
                        <h2 class="text-h5 my-2">Тэги</h2>
                        <v-combobox v-model="idea.tags" chips clearable label="Укажите тэги" multiple outlined
                            :error-messages="tagsErrors">
                            <template v-slot:selection="{ attrs, item, select, selected }">
                                <v-chip v-bind="attrs" :input-value="selected" close @click="select" small
                                    @click:close="removeTag(item)">
                                    <div class="caption">{{ item }}</div>&nbsp;
                                </v-chip>
                            </template>
                        </v-combobox>

                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn nuxt to="/job" class="mr-4 caption" color="red lighten-2 pa-4">Отмена</v-btn>
                        <v-btn @click="saveIdea" class="pa-4 caption" color="primary lighten-2">Сохранить</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col class="d-none d-md-block">
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import ImageInput from '~/components/UI/ImageInput.vue'
import CreateTeam from '~/components/ideas/CreateTeam.vue'
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, minValue, maxValue, numeric, url } from 'vuelidate/lib/validators'
export default {
    head() {
        let descr = 'Редактировать идею для факультета информационных систем и технологий',
            title = 'Редактировать идею',
            type = 'site'
        return {
            title: title,
            meta: [
                { hid: 'description', name: 'description', content: descr },
                { hid: 'og:title', name: 'og:title', content: descr },
                { hid: 'og:description', name: 'og:description', content: descr },
                { hid: 'og:type', name: 'og:type', content: type }
            ]
        }
    },
    middleware: ['isLoggedIn'],
    async created() {
        this.token = this.$store.getters['auth/getAccessToken']
        this.ideaId = this.$route.params.id
        this.idea = (await this.$axios.get(`/api/v1/ideas/${this.ideaId}`,
            {
                withCredentials: true,
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                }
            })
        ).data.data

        if (this.user.id !== this.idea.author.id) this.$router.push('/')
        for (let i in this.idea.area_tech) {
            this.idea.area_tech[i] = this.idea.area_tech[i].title
        }
        if (this.idea.image) this.background = this.idea.image

        for (let i in this.idea.tags) {
            this.idea.tags[i] = this.idea.tags[i].name
        }
        for (let i in this.idea.team) {
            this.idea.team[i] = this.idea.team[i].username
        }
        this.users = this.idea.team
    },
    components: {
        ImageInput,
        CreateTeam
    },
    mixins: [validationMixin],
    validations: {
        idea: {
            name: { required, minLength: minLength(5), maxLength: maxLength(30) },
            description: { required, minLength: minLength(10), maxLength: maxLength(120) },
            information: { required, minLength: minLength(20) },
            tags: { required },
        },
    },
    data() {
        return ({
            background: false,
            token: '',
            id: 0,
            counter: 0,
            search: null,
            idea: {
                name: '',
                description: '',
                lab: '',
                source: '',
                links: [],
                tags: [],
                team: [],
                area_tech: [],
                image: '',
                information: ''
            },
            users: [],
            rules: [
                value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
            ],
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    exact: true,
                    to: '/',
                },
                {
                    text: 'ideas',
                    exact: true,
                    to: '/ideas',
                },
                {
                    text: 'edit',
                    disabled: true,
                    exact: true,
                    to: '/ideas/edit'
                }
            ],
        })
    },
    methods: {
        setImage(e) {
            this.idea.image = e
            let reader = new FileReader();
            reader.readAsDataURL(e);
            reader.onload = function () {
                this.background = reader.result
            }.bind(this);
        },
        remove(item) {
            this.idea.area_tech.splice(this.idea.area_tech.indexOf(item), 1)
            this.idea.area_tech = [...this.idea.area_tech]
        },
        removeLink(item) {
            this.idea.links.splice(this.idea.links.indexOf(item), 1)
            this.idea.links = [...this.idea.links]
        },
        removeTag(item) {
            this.idea.tags.splice(this.idea.tags.indexOf(item), 1)
            this.idea.tags = [...this.idea.tags]
        },
        removeTeam(item) {
            this.idea.team.splice(this.idea.team.indexOf(item), 1)
            this.idea.team = [...this.idea.team]
        },
        async saveIdea() {
            let idea = { ...this.idea }
            this.$v.$touch()
            if (this.$v.$anyError) {
                this.$showMsg()
                return
            }
            if(typeof idea.image === 'string' || idea.image instanceof String){
                delete idea.image
            }
            let formData = this.$toFormData(idea)
            if(this.counter>2) return
            this.counter++
            this.$axios.patch(`/api/v1/ideas/${this.ideaId}/`,
                formData,
                {
                    withCredentials: true,
                    headers: {
                        'Accept': 'application/json',
                        'Authorization': `Bearer ${this.token}`,
                    }
                }).then(res => {
                    this.$showMsg("Идея отправлена на модерацию", "success")
                }).catch(err => {
                    if (err.response.status == 403 || err.response.status == 401) {
                        this.$store.dispatch("auth/tokenPair").then(res => {
                            this.saveIdea()
                        }).catch(err => {
                            this.$showMsg("Ошибка автооизации")
                        })
                    }
                })
        },
    },
    computed: {
        user: {
            get() {
                return this.$store.getters['auth/getUser']
            },
            set(newValue) {
                this.$store.commit('auth/setUser', newValue)
            }
        },
        nameErrors() {
            const errors = []
            if (!this.$v.idea.name.$dirty) return errors
            !this.$v.idea.name.maxLength && errors.push('Слишком длинное название')
            !this.$v.idea.name.minLength && errors.push('Слишком короткое название')
            !this.$v.idea.name.required && errors.push('Название обязательно')
            return errors
        },
        descriptionErrors() {
            const errors = []
            if (!this.$v.idea.description.$dirty) return errors
            !this.$v.idea.description.maxLength && errors.push('Сократите описание')
            !this.$v.idea.description.minLength && errors.push('Описание должно быть содержательно')
            !this.$v.idea.description.required && errors.push('Описание обязательно')
            return errors
        },
        informationErrors() {
            const errors = []
            if (!this.$v.idea.information.$dirty) return errors
            !this.$v.idea.information.minLength && errors.push('Описание должно быть содержательным')
            !this.$v.idea.information.required && errors.push('Описание обязательно')
            return errors
        },
        tagsErrors() {
            const errors = []
            if (!this.$v.idea.tags.$dirty) return errors
            !this.$v.idea.tags.required && errors.push('Укажите тэги')
            return errors
        },


    },
    watch: {
        async search(val) {
            if (val != null && val.length > 2) {
                let query = `api/v1/users/?q=${val}`
                this.users = await (await this.$axios.get(query)).data.data.results
                let users = []
                for (let i in this.users) {
                    users[i] = await this.users[i].username
                }
                this.users = [...users, ...this.idea.team]
            }
        }
    }
}
</script>

<style>
.redBorder {
    border: 2px red solid !important;
    border-radius: 4px
}
</style>

