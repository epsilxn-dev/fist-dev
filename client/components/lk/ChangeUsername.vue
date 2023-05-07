<template>
    <v-card class="pa-3">
        <h2 class="text-h5 mb-4">Смена имени пользователя</h2>
        <v-text-field
            clearable
            @input="$v.username.$touch()"
            @blur="$v.username.$touch()"
            :error-messages="usernameErrors"
            v-model="username"
            class="mt-1"
            outlined
            label="Имя пользователя"
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
        mixins: [validationMixin],
        mounted(){
            this.username = this.item
        },
        validations: {
            username: {required, minLength: minLength(3)}, 
            checkPassword: {minLength: minLength(8)}, 
        },
        data(){
            return({
                checkPassword: '',
                username: ''
            })
        },
        props: {
            item: {
                type: String,
                required: true
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
                this.$emit('changeUsername', this.username, this.checkPassword)
            }
        },
        computed:{
            usernameErrors () {
                const errors = []
                if (!this.$v.username.$dirty) return errors
                !this.$v.username.minLength && errors.push('Слишком короткий пароль')
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

