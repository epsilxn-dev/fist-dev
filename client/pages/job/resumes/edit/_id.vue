<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8">
                <h1 class="text-h4 my-2">Добавить резюме</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs" />
                <v-card>
                    <v-card-text class="pa-2 pa-md-4">
                        <h2 class="text-h5 my-2">Личная информация</h2>
                        <v-container class="image_input mt-4">
                            <v-tooltip left>
                                <template v-slot:activator="{ on, attrs }">
                                    <ImageInput :background="background" @change="setImage" :rules="rules" />
                                </template>
                                <span>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis odit nemo nisi cum
                                    asperiores corporis perferendis. Alias quis illo, omnis unde sit molestias officiis
                                    placeat obcaecati. Quo consectetur blanditiis beatae.</span>
                            </v-tooltip>
                        </v-container>
                        <v-radio-group :error-messages="sexErrors" v-model="sex">
                            <small class="mb-2 subtitle-1">Пол</small>
                            <v-radio :label="'Не указан'" :value="'Не указан'"/>
                            <v-radio :label="'Мужской'" :value="'Мужской'"/>
                            <v-radio :label="'Женский'" :value="'Женский'"/>
                        </v-radio-group>
                        <h2 class="text-h5 my-2">Данные для работодателя</h2>
                        <v-container>
                            <v-text-field @input="$v.title.$touch()" @blur="$v.title.$touch()"
                                :error-messages="titleErrors" clearable v-model="title" class="my-1" solo counter="30"
                                label="Название резюме"></v-text-field>
                            <v-textarea @input="$v.description.$touch()" @blur="$v.description.$touch()"
                                :error-messages="descriptionErrors" outlined label="Описание резюме" class='my-1'
                                v-model="description" />
                            <v-text-field clearable v-model="salary" class="my-1" outlined label="Желаемая з/п"
                                @input="$v.salary.$touch()" @blur="$v.salary.$touch()" :error-messages="salaryErrors">
                            </v-text-field>
                            <h2 class="text-h5 my-2">Навыки</h2>
                            <v-text-field clearable v-model="exp" @input="$v.exp.$touch()" @blur="$v.exp.$touch()"
                                :error-messages="expErrors" class="my-1" outlined label="Стаж"></v-text-field>
                            <v-select label="Специальность" class="my-2" outlined item-text="name" item-value="id"
                                v-model="speciality" :items="specialityItems"></v-select>
                            <v-combobox :items="items" v-model="skills" chips clearable label="Ключевые навыки" multiple
                                required @input="$v.skills.$touch()" @blur="$v.skills.$touch()"
                                :error-messages="skillsErrors" outlined>
                                <template v-slot:selection="{ attrs, item, select, selected }">
                                    <v-chip v-bind="attrs" :input-value="selected" close @click="select" small
                                        @click:close="remove(item)">
                                        <div class="caption">{{ item }}</div>&nbsp;
                                    </v-chip>
                                </template>
                            </v-combobox>
                        </v-container>
                        <h2 class="text-h5 my-2">Тэги</h2>
                        <v-combobox v-model="tags" chips clearable label="Укажите тэги" multiple outlined>
                            <template v-slot:selection="{ attrs, item, select, selected }">
                                <v-chip v-bind="attrs" :input-value="selected" close @click="select" small
                                    @click:close="removeTag(item)">
                                    <div class="caption">{{ item }}</div>&nbsp;
                                </v-chip>
                            </template>
                        </v-combobox>
                        <h2 class="text-h5 my-2">Контакты</h2>
                        <v-text-field clearable v-model="email" class="my-2" outlined @input="$v.email.$touch()"
                            @blur="$v.email.$touch()" :error-messages="emailErrors" label="Электронная почта">
                        </v-text-field>
                        <v-text-field clearable v-model="phone" class="my-2" outlined @input="$v.phone.$touch()"
                            @blur="$v.phone.$touch()" :error-messages="phoneErrors" label="Номер телефона">
                        </v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click="savePDF" class="pa-4 mr-4  caption" color="warning lighten-2">PDF</v-btn>
                        <v-btn nuxt to="/job" class="mr-4 caption" color="red lighten-2 pa-4">Отмена</v-btn>
                        <v-btn @click="saveResume" class="pa-4 caption" color="primary lighten-2">Сохранить</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapState } from 'vuex'
import pdfMake from "pdfmake/build/pdfmake";
import pdfFonts from "pdfmake/build/vfs_fonts";
pdfMake.vfs = pdfFonts.pdfMake.vfs;
import ImageInput from '~/components/UI/ImageInput.vue'
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, minValue, maxValue, numeric } from 'vuelidate/lib/validators'
import Swal from 'sweetalert2'
export default {
    head() {
        return {
            title: 'Редактировать резюме'
        }
    },
    middleware: ['isLoggedIn'],
    async created() {
        this.specialityItems = await (await this.$axios.get('api/v1/specialties/')).data.data.results
        this.$store.dispatch('lk/setResume', this.user.id).then(res => {
            this.resume = res
            if (this.resume.id.id !== this.user.id)
                this.$router.push('/auth')
            this.background = this.resume.image
            this.title = this.resume.title
            this.description = this.resume.description
            for (let item of this.resume.tags) {
                this.tags.push(item.name)
            }
            for (let item of this.resume.skills) {
                this.skills.push(item.name)
            }

            this.salary = this.resume.salary
            this.sex = this.resume.gender
            this.speciality = this.resume.specialization
            this.exp = this.resume.work_exp
            this.email = this.resume.id.email
            this.phone = this.resume.phone

        })

    },
    components: {
        ImageInput
    },
    mixins: [validationMixin],
    validations: {
        skills: { required },
        sex: { required },
        speciality: { required },
        exp: { required },
        salary: { required, minLength: minLength(4) },
        title: { required, minLength: minLength(5), maxLength: maxLength(30) },
        description: { required, minLength: minLength(10) },
        email: { required, email },
        phone: { required, minValue: minValue(80000000000), maxValue: maxValue(90000000000) }
    },
    data() {

        return ({
            counter: 0,
            background: '',
            specialityItems: [],
            resume: [],
            title: '',
            description: '',
            tags: [],
            skills: [],
            salary: '',
            sex: '',
            speciality: '',
            exp: '',
            email: '',
            phone: '',
            items: ['Грамотная речь', 'Высокий уровень владения office'],
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
                    text: 'job',
                    exact: true,
                    to: '/job',
                },
                {
                    text: 'resumes',
                    to: '/job',
                    exact: true,
                },
                {
                    text: 'edit',
                    disabled: true,
                    exact: true,
                    to: '/job/resumes/edit'
                }
            ],
        })
    },
    methods: {
        savePDF() {
            let base = this.$store.getters['auth/getBase']

            let docDefinition = {
                content: [
                    {
                        text: 'Личная информация \n\n',
                        style: 'header'
                    },
                    {
                        alignment: 'justify',
                        columns: [
                            {
                                image: '',
                                width: 200,

                            },
                            {
                                ul: [
                                    `Фамилия: ${this.user.last_name} \n\n`,
                                    `Имя: ${this.user.first_name} \n\n`,
                                    `Отчество: ${this.user.patronymic || 'Не указано'} \n\n`,
                                    `Номер телефона: ${this.phone} \n\n`,
                                    `Почта: ${this.email} \n\n`,
                                ],
                                margin: [10, 10],
                            },
                        ]

                    },
                    {
                        margin: [0, 20, 0, 0],
                        text: 'Данные для работодателя\n\n',
                        style: 'header'
                    },
                    {
                        ul: [
                            `Название: ${this.title} \n\n`,
                            `Опыт работы: ${this.exp} \n\n`,
                        ],
                    },
                    {
                        text: 'Специальность\n\n',
                        style: 'header'
                    },
                    {
                        ul: [
                            `Специальность: ${this.speciality.name} \n\n`,
                            `Желаемая зарплата: ${this.salary} \n\n`,
                            `Ключевые навыки: ${this.skills.join(', ')} \n\n`,
                            `О себе: ${this.description} \n\n`,
                        ],
                    },

                ],
                styles: {
                    header: {
                        fontSize: 18,
                        bold: true
                    },
                    bigger: {
                        fontSize: 15,
                        italics: true
                    }
                }
            };
            function getDataUri(url) {
                var image = new Image();
                let k = ''
                image.src = url;
                image.crossOrigin = "anonymous"
                image.onload = function () {
                    var canvas = document.createElement('canvas');
                    canvas.width = this.naturalWidth;
                    canvas.height = this.naturalHeight;
                    canvas.getContext('2d').drawImage(this, 0, 0);
                    canvas.toDataURL('image/png').replace(/^data:image\/(png|jpg);base64,/, '');
                    k = canvas.toDataURL('image/png');
                    docDefinition.content[1].columns[0].image = k
                };
            }
            getDataUri(base+this.resume.image)
            setTimeout(() => {
                pdfMake.createPdf(docDefinition).download('resume.pdf');
            }, 1000)

        },
        setImage(e) {
            this.image = e
            let reader = new FileReader();
            reader.readAsDataURL(e);
            reader.onload = function () {
                this.background = reader.result
            }.bind(this);
        },
        remove(item) {
            this.skills.splice(this.skills.indexOf(item), 1)
            this.skills = [...this.skills]
        },
        removeTag(item) {
            this.tags.splice(this.tags.indexOf(item), 1)
            this.tags = [...this.tags]
        },
        saveResume() {
            this.$v.$touch()
            if (this.$v.$anyError) {
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: 'Проверьте данные',
                    showConfirmButton: false,
                    timer: 3000
                })
                return
            }
            let resume = {
                title: this.title,
                description: this.description,
                gender: this.sex,
                phone: this.phone,
                image: this.image,
                work_exp: this.exp,
                email: this.email,
                salary: this.salary,
                specialization_id: this.speciality.id || this.speciality,
                tags: this.tags,
                skills: this.skills
            }
            let accessToken = this.$store.getters['auth/getAccessToken']
            if(this.counter > 2)
                return
            this.counter++
            let formData = this.$toFormData(resume, "image")
            this.$axios.patch(`api/v1/resumes/${this.user.id}/`, formData,
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${accessToken}`
                    }
                }
            ).then(res => {
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'Резюме успешно сохранено',
                    showConfirmButton: false,
                    timer: 3000
                })
            })

        }
    },
    computed: {

        ...mapState('auth', ['base, accessToken']),
        user: {
            get() {
                return this.$store.getters['auth/getUser']
            },
            set(newValue) {
                this.$store.commit('auth/setUser', newValue)
            }
        },
        sexErrors() {
            const errors = []
            if (!this.$v.sex.$dirty) return errors
            !this.$v.sex.required && errors.push('Укажите пол')
            return errors
        },
        specialityErrors() {
            const errors = []
            if (!this.$v.speciality.$dirty) return errors
            !this.$v.speciality.required && errors.push('Укажите специальность')
            return errors
        },
        skillsErrors() {
            const errors = []
            if (!this.$v.skills.$dirty) return errors
            !this.$v.skills.required && errors.push('Укажите ваши навыки')
            return errors
        },
        expErrors() {
            const errors = []
            if (!this.$v.exp.$dirty) return errors
            !this.$v.exp.required && errors.push('Укажите опыт')
            return errors
        },

        salaryErrors() {
            const errors = []
            if (!this.$v.salary.$dirty) return errors
            !this.$v.salary.minLength && errors.push('Слишком маленькое значение')
            !this.$v.salary.required && errors.push('Укажите зп')
            return errors
        },
        titleErrors() {
            const errors = []
            if (!this.$v.title.$dirty) return errors
            !this.$v.title.maxLength && errors.push('Слишком длинный заголовок')
            !this.$v.title.minLength && errors.push('Слишком короткий заголовок')
            !this.$v.title.required && errors.push('Заголовок обязателен')
            return errors
        },
        descriptionErrors() {
            const errors = []
            if (!this.$v.description.$dirty) return errors
            !this.$v.description.minLength && errors.push('Слишком короткое описание')
            !this.$v.description.required && errors.push('Заполние описание')
            return errors
        },
        emailErrors() {
            const errors = []
            if (!this.$v.email.$dirty) return errors
            !this.$v.email.email && errors.push('Неверный формат почты')
            !this.$v.email.required && errors.push('Почта обязательно')
            return errors
        },
        phoneErrors() {
            const errors = []
            if (!this.$v.phone.$dirty) return errors
            !this.$v.phone.minValue && errors.push('Неверный формат номера')
            !this.$v.phone.maxValue && errors.push('Неверный формат номера')
            !this.$v.phone.required && errors.push('Телефон обязателен')
            return errors
        },
    },
}
</script>
