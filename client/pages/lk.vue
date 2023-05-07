<template>
    <v-container class="mt-4 pa-2">
        <v-row v-if="user" no-gutters>
            <v-col />
            <v-col class="col col-12 col-md-8">
                <h1 class="text-h4">Личный кабинет</h1>
                <v-card class="pa-4 mt-4">
                    <h2 class="text-h5 mb-2">Смените аватар</h2>
                    <ImageInput :background="user.avatar ? `${user.avatar}` : undefined" @change="setImage"
                        :rules="rules" />
                    <PersonalInfo @savePersonal="savePersonal" class="my-4" :item="user" />
                    <ChangePassword @changePassword="changePassword" :error="passwordError" class="my-4" />
                    <ChangeUsername :error="usernameError" @changeUsername="changeUsername" class="my-4"
                        :item="user.username" />
                    <h2 class="text-h5 mb-2">Изменить резюме</h2>
                    <Add v-if="!resume" @click="$router.push(`/job/resumes/create`)" class="w-100" />
                    <ResumeItem :class="{ 'deleted': resume.is_deleted }" @delete="deleteResume" :editable="true"
                        v-if="resume" :resume="resume"></ResumeItem>
                    <h2 class="text-h5 mb-2">Изменить идеи</h2>
                    <div v-if="ideas">
                        <IdeasItem @delete="deleteIdea" class="mb-2" :editable="true" v-for="(idea, i) in ideas"
                            :key="i" :idx="i" :idea="idea" />
                    </div>
                    <Add @click="$router.push('/ideas/suggest')" class="w-100" />
                </v-card>
            </v-col>
            <v-col />
        </v-row>
        <v-row class="d-flex justify-center align-center" v-else>
            <v-progress-circular :size="70" :width="7" color="primary" indeterminate></v-progress-circular>
        </v-row>
    </v-container>
</template>


<script>
import Swal from 'sweetalert2'
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, minValue, maxValue, numeric, url } from 'vuelidate/lib/validators'
import ImageInput from '@/components/UI/ImageInput'
import PersonalInfo from '@/components/lk/PersonalInfo'
import ChangePassword from '@/components/lk/ChangePassword'
import ChangeUsername from '@/components/lk/ChangeUsername'
import ChangeEmail from '@/components/lk/ChangeEmail'
import { mapState } from 'vuex';
import ResumeItem from '@/components/job/ResumeItem'
import IdeasItem from '@/components/ideas/IdeaCard'
import Add from '@/components/UI/Add'


export default {
    head() {
        let descr = 'Личный кабинет факультета информационных систем и технологий',
            title = 'Личный кабинет',
            type = 'site'
        return {
            title: title,
            meta: [
                { hid: 'description', name: 'description', content: descr },
                { hid: 'og:title', name: 'og:title', content: descr },
                { hid: 'og:description', name: 'og:description', content: descr },
                { hid: 'og:type', name: 'og:type', content: type },
            ]
        }
    },
    middleware: ['isLoggedIn'],
    components: {
        ImageInput,
        PersonalInfo,
        IdeasItem,
        ChangePassword,
        ChangeUsername,
        ChangeEmail,
        ResumeItem,
        Add
    },
    async created() {
        if (!this.currentUser) 
            this.$router.push('/auth')
        let token = this.$store.getters["auth/getAccessToken"]
        if (this.user.id) {
            this.ideas = (await this.$axios.get(`/api/v1/ideas/?author=${this.user.id}`,
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    }
                })
            ).data.data
            try {
                this.resume = await this.$store.dispatch('lk/setResume', this.user.id)
            }
            catch (err) {
            }
        }
    },

    data() {
        return ({
            resume: false,
            usernameError: '',
            passwordError: '',
            emailError: '',
            personalError: '',
            rules: [
                value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
            ],
            avatar: '',
            passwordError: '',
            emailError: '',
            usernameError: '',
            ideas: false
        })
    },
    mixins: [validationMixin],
    validations: {
        skills: { required },
        sex: { required },
        speciality: { required },
        exp: { required },
        salary: { required, minLength: minLength(4) },
        title: { required, minLength: minLength(5), maxLength: maxLength(30) },
        description: { required, minLength: minLength(10), maxLength: maxLength(120) },
        email: { required, email },
        phone: { required, minValue: minValue(80000000000), maxValue: maxValue(90000000000) }
    },
    methods: {
        deleteResume() {
            this.$axios.delete(`api/v1/resumes/${this.user.id}/`,
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${this.$store.getters["auth/getAccessToken"]}`,
                    }
                }
            )
        },
        deleteIdea(options) {
            this.$axios.delete(`api/v1/ideas/${options.id}/`,
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${this.$store.getters["auth/getAccessToken"]}`,
                    }
                }
            ).then((res) => {
                Swal.fire('Успешно!', 'Идея была удалена', 'success')
                this.ideas.splice(options.idx, 1)
            })
        },
        setImage(e) {
            let data = new FormData()
            data.append('avatar', e, e.name)
            this.image = e

            this.$axios.patch(
                'api/v1/users/change/avatar/',
                data,
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${this.$store.getters["auth/getAccessToken"]}`,
                        'Content-Type': `multipart/form-data`
                    }
                }
            ).then(res => {
                Swal.fire('Успешно', 'Данные изменены', 'success')
                let newUser = { ...this.user, avatar: res.data.data.avatar }
                this.$store.commit('auth/setUser', newUser)
                this.$cookiz.set('user', newUser, {
                    path: '/',
                    maxAge: 60 * 60 * 24 * 7
                })
            }).catch(res => {
                (res)
            })

        },
        savePersonal(user) {
            this.$axios.patch(
                'api/v1/users/change/private_data/',
                {
                    first_name: user.first_name,
                    last_name: user.last_name,
                    patronymic: user.patronymic,
                    discord: user.discord,
                    skype: user.skype,
                    phone: user.phone
                },
                {
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Authorization': `Bearer ${this.$store.getters["auth/getAccessToken"]}`,
                    }
                }
            ).then(res => {
                this.$cookiz.set('user', { ...this.user, ...user }, {
                    path: '/',
                    maxAge: 60 * 60 * 24 * 7
                })
                this.personalError = ''
                Swal.fire('Успешно', 'Данные изменены', 'success')
            }).catch(res => this.personalError = 'Произошла какая-то ошибка')
        },
        changePassword(password, checkPassword) {
            let token = this.$store.getters["auth/getAccessToken"]
            this.$axios.patch(
                'api/v1/users/change/password/',
                {
                    checkPassword,
                    password
                },
                {
                    withCredentials: true,
                    headers: {
                        'Accept': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    }
                }
            ).then(res => {
                this.passwordError = ''
                Swal.fire('Успешно', 'Данные изменены', 'success')
            }).catch(res => {
                this.passwordError = 'Введён неверный пароль'
            })

        },
        changeUsername(username, checkPassword) {
            let token = this.$store.getters["auth/getAccessToken"]
            this.$axios.patch(
                'api/v1/users/change/username/',
                {
                    username,
                    checkPassword
                },
                {
                    withCredentials: true,
                    headers: {
                        'Accept': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    }
                }
            ).then(res => {
                this.usernameError = ''
                Swal.fire('Успешно', 'Данные изменены', 'success')
                this.$cookiz.set('user', { ...this.user, username }, {
                    path: '/',
                    maxAge: 60 * 60 * 24 * 7
                })
            }).catch(res => this.usernameError = 'Возможно это имя занято или ещё какая хуйня на сервере')
        },
        changeEmail(email, checkPassword) {
            let token = this.$store.getters["auth/getAccessToken"]
            this.$axios.patch(
                'api/v1/users/change/email/',
                {
                    email,
                    checkPassword
                },
                {
                    withCredentials: true,
                    headers: {
                        'Accept': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    }
                }
            ).then(res => {
                this.emailError = ''
                this.$cookiz.set('user', { ...this.user, email }, {
                    path: '/',
                    maxAge: 60 * 60 * 24 * 7
                })
                Swal.fire('Успешно', 'Данные изменены', 'success')
            }).catch(res => this.emailError = 'Проверьте данные')

        }
    },
    computed: {
        ...mapState('auth', ['currentUser']),
        user() {
            return JSON.parse(JSON.stringify(this.currentUser))
        }
    }
}
</script>


<style scoped>
.w-100 {
    width: 100% !important
}

.deleted {
    opacity: .6;
}
</style>


