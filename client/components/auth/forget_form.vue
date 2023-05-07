<template>
    <div class="form_container">
        <v-card width="500">
            <v-card-title>Восстановление пароля</v-card-title>
            <v-card-text>
                <form @keyup.enter="submit">
                    <v-text-field
                        v-model="email"
                        :error-messages="emailErrors"
                        label="E-mail"
                        required
                        @input="$v.email.$touch()"
                        @blur="$v.email.$touch()"
                    ></v-text-field>
                   
                    <v-btn
                        class="mr-4 primary"
                        @click="submit"
                    >
                        Отправить
                    </v-btn>
                    <v-btn @click="clear">
                        Очистить
                    </v-btn>
                    <v-alert
                      border="bottom"
                      color="pink darken-1"
                      dark
                      v-if="errors"
                      class="mt-4"
                    >
                      {{errors}}
                    </v-alert>
                </form>
            </v-card-text>
            <v-card-subtitle>
                <nuxt-link to="/auth/">
                    Войти в аккаунт
                </nuxt-link>
            </v-card-subtitle>
           
        </v-card>
    </div>
</template>


<script>
  import { validationMixin } from 'vuelidate'
  import { required, email } from 'vuelidate/lib/validators'

  export default {
    mixins: [validationMixin],

    validations: {
      email: {required, email}
    },

    data: () => ({
      email: ''
    }),
    props:{
      errors:{
        type: String,
        default: null
      }
    },

    computed: {
      
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Неверная почта')
        !this.$v.email.required && errors.push('Введитте почту')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()
        if(this.$v.$anyError) return
        let user = {
          email: this.email
        }
        this.$emit('submit', user)
      },
      clear () {
        this.$v.$reset()
        this.email = ''
      },
    },
  }
</script>


<style>
    .form_container{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
</style>

