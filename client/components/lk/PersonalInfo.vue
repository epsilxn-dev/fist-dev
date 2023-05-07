<template>
    <v-card class="pa-3">
        <h2 class="text-h5 mb-4">Личная информация</h2>
        <v-text-field
            clearable
            v-model="user.last_name"
            @blur="$v.user.last_name.$touch()"
            @input="$v.user.last_name.$touch()"
            :error-messages="last_nameErrors"
            class="mt-1"
            outlined
            label="Фамилия"
        ></v-text-field>
        <v-text-field
            clearable
            @blur="$v.user.first_name.$touch()"
            @input="$v.user.first_name.$touch()"
            :error-messages="first_nameErrors"
            v-model="user.first_name"
            class="mt-1"
            outlined
            label="Имя"
        ></v-text-field>
        <v-text-field
            clearable
            v-model="user.patronymic"
            class="mt-1"
            outlined
            label="Отчество"
        ></v-text-field>
        <h2 class="text-h5 mb-4">Контакты</h2>
        <v-text-field
            clearable
            v-model="user.skype"
            class="mt-1"
            outlined
            label="Skype"
        ></v-text-field>
        <v-text-field
            clearable
            v-model="user.discord"
            class="mt-1"
            outlined
            label="Discord"
        ></v-text-field>
        <v-text-field
            clearable
            v-model="user.phone"
            class="mt-1"
            outlined
            label="Телефон"
        ></v-text-field>
        <v-alert
            border="bottom"
            color="pink darken-1"
            dark
            v-if="error"
            class="mt-4"
        >
            {{error}}
        </v-alert>
        <v-card-actions
            class="mx-0 px-0"
        >
            <v-spacer></v-spacer>
            <v-btn 
                color="primary"
                @click="$emit('savePersonal', user)"
            >
                Сохранить
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, minValue, maxValue, numeric, url } from 'vuelidate/lib/validators'

export default {
    data(){
        return({
            user:{}
        })
    },
    mixins: [validationMixin],
    validations: {
        user: {
           first_name: {required, minLength: minLength(2)},
           last_name: {required, minLength: minLength(2)}, 
        }
        // email: {required, email},
    },
    mounted(){
        this.user = {...this.item}
    },
    props: {
        item: {
            required: true,
            type: Object
        },
        error:{
            type: String,
            default: ''
        }
    },
    methods:{
        save(){
            this.$v.$touch()
            if(this.$v.$anyError) return
            this.$emit('changePersonal', this.user)
        }
    },
    computed:{
        first_nameErrors () {
            const errors = []
            if (!this.$v.user.first_name.$dirty) return errors
            !this.$v.user.first_name.required && errors.push('Введите имя')
            !this.$v.user.first_name.minLength && errors.push('Введите имя')
            return errors
        },
        last_nameErrors () {
            const errors = []
            if (!this.$v.user.last_name.$dirty) return errors
            !this.$v.user.last_name.required && errors.push('Введите фамилию')
            !this.$v.user.last_name.minLength && errors.push('Введите фамилию')

            return errors
        },
    }
}
</script>

