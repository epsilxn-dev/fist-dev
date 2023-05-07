<template>
    <v-card class="pa-3">
        <h2 class="text-h5 mb-4">Смена пароля</h2>
        <v-text-field
            clearable
            @input="$v.password.$touch()"
            @blur="$v.password.$touch()"
            :error-messages="passwordErrors"
            v-model="password"
            class="mt-1"
            outlined
            type="password"
            label="Новый пароль"
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
        validations: {
            password: {required, minLength: minLength(8)}, 
            checkPassword: {minLength: minLength(8)}, 
        },
        data(){
            return({
                password: '',
                checkPassword: ''
            })
        },
        props: {
            error:{
                type: String,
                default: ''
            }
        },
        methods: {
            save(){
                this.$v.$touch()
                if(this.$v.$anyError) return
                this.$emit('changePassword', this.password, this.checkPassword)
            }
        },
        computed:{
            passwordErrors () {
                const errors = []
                if (!this.$v.password.$dirty) return errors
                !this.$v.password.minLength && errors.push('Слишком короткий пароль')
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

