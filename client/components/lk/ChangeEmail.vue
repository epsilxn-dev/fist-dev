<template>
    <v-card class="pa-3">
        <h2 class="text-h5 mb-4">Смена почты</h2>
        <v-text-field
            clearable
            @input="$v.email.$touch()"
            @blur="$v.email.$touch()"
            :error-messages="emailErrors"
            v-model="email"
            class="mt-1"
            outlined
            label="e-mail"
        ></v-text-field>
        <v-text-field
            clearable
            @input="$v.checkPassword.$touch()"
            @blur="$v.checkPassword.$touch()"
            type="password"
            :error-messages="checkPasswordErrors"
            v-model="checkPassword"
            class="mt-1"
            outlined
            label="Текущий пароль"
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
                @click="save"
            >
                Сохранить
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required, maxLength, minLength, email } from 'vuelidate/lib/validators'

    export default {
        mounted(){
            this.email = this.item
        },
        mixins: [validationMixin],
        validations: {
            email: {required, email}, 
            checkPassword: {minLength: minLength(8)}, 
        },
        data(){
            return({
                checkPassword: '',
                email: ''
            })
        },
        props: {
            item: {
                type: String,
                default: ''
            },
            error:{
                type: String,
                default: ''
            }
        },
        methods: {
            save(){
                this.$v.$touch()
                if(this.$v.$anyError) return
                this.$emit('changeEmail', this.email, this.checkPassword)
            }
        },
        computed:{
            emailErrors () {
                const errors = []
                if (!this.$v.email.$dirty) return errors
                !this.$v.email.email && errors.push('Введите почту')
                !this.$v.email.required && errors.push('Введите почту')
                return errors
            },
            checkPasswordErrors () {
                const errors = []
                if (!this.$v.checkPassword.$dirty) return errors
                !this.$v.checkPassword.minLength && errors.push('Слишком короткий пароль')
                return errors
            },
        }
    }
</script>

