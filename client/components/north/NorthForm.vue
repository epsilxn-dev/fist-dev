 <template>
    <v-card class="pa-2">
        <v-card-text>
          <form @keyup.enter="submit">
            <v-text-field
                v-model="name"
                :error-messages="nameErrors"
                :counter="40"
                label="ФИО"
                required
                @input="$v.name.$touch()"
                @blur="$v.name.$touch()"
            ></v-text-field>
            <v-text-field
                v-model="email"
                :error-messages="emailErrors"
                label="Электронная почта"
                required
                @input="$v.email.$touch()"
                @blur="$v.email.$touch()"
            ></v-text-field>
            <v-text-field
                v-model="phone"
                :error-messages="phoneErrors"
                label="89ххххххххх"
                required
                @input="$v.phone.$touch()"
                @blur="$v.phone.$touch()"
            ></v-text-field>
            <v-checkbox
                v-model="checkbox"
                :error-messages="checkboxErrors"
                label="Согласие на обработку персональных данных?"
                required
                @change="$v.checkbox.$touch()"
                @blur="$v.checkbox.$touch()"
            ></v-checkbox>

            <v-btn
                color="primary"
                class="mr-4"
                @click="submit"
            >
                Отправить
            </v-btn>
            <v-btn @click="clear">
                очистить
            </v-btn>
          </form>
        </v-card-text>
    </v-card>
 </template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email, minValue, maxValue } from 'vuelidate/lib/validators'

  export default {
    mixins: [validationMixin],

    validations: {
      name: { required, maxLength: maxLength(40) },
      email: { required, email },
      phone: { required, minValue: minValue(89000000000), maxValue: maxValue(89999999999)},
      checkbox: {
        checked (val) {
          return val
        },
      },
    },

    data: () => ({
      name: '',
      email: '',
      checkbox: false,
      phone: ''
    }),

    computed: {
      checkboxErrors () {
        const errors = []
        if (!this.$v.checkbox.$dirty) return errors
        !this.$v.checkbox.checked && errors.push('Согласитесь, чтоб продолжить')
        return errors
      },
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Введите реальные ФИО')
        !this.$v.name.required && errors.push('ФИО обязательное поле')
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Неверный формат почты')
        !this.$v.email.required && errors.push('Почта обязательна')
        return errors
      },
      phoneErrors () {
        const errors = []
        if (!this.$v.phone.$dirty) return errors
        !this.$v.phone.minValue && errors.push('Неверный формат номера')
        !this.$v.phone.maxValue && errors.push('Неверный формат номера')
        !this.$v.phone.required && errors.push('Введите телефон')
        return errors
      }
    },

    methods: {
      submit () {
        this.$v.$touch()
        if (!this.$v.$invalid){
          let user = {}
          user.phone = this.phone
          user.email = this.email
          user.name = this.name
          this.$emit('submitForm', user)
          this.clear()
          return
        }
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.email = ''
        this.phone = ''
        this.checkbox = false
      },
    },
  }
</script>
 