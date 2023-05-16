<template>
    <div class="form_container">
        <v-card width="500">
            <v-card-title>Регистрация</v-card-title>
            <v-card-text>
                <form @keyup.enter="submit">
                    <v-text-field
                        v-model="firstName"
                        :error-messages="firstNameErrors"
                        label="Ваше имя"
                        required
                        @input="$v.firstName.$touch()"
                        @blur="$v.firstName.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="lastName"
                        :error-messages="lastNameErrors"
                        label="Фамилия"
                        required
                        @input="$v.lastName.$touch()"
                        @blur="$v.lastName.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="email"
                        :error-messages="emailErrors"
                        label="E-mail"
                        required
                        @input="$v.email.$touch()"
                        @blur="$v.email.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="username"
                        :error-messages="nameErrors"
                        label="Имя пользователя"
                        required
                        @input="$v.username.$touch()"
                        @blur="$v.username.$touch()"
                    ></v-text-field>
                    <v-text-field
                        type="password"
                        v-model="password"
                        :error-messages="passErrors"
                        label="Пароль"
                        required
                        @input="$v.password.$touch()"
                        @blur="$v.password.$touch()"
                    ></v-text-field>
                    <v-btn class="mr-4 primary" @click="submit">
                        Отправить
                    </v-btn>
                    <v-btn @click="clear"> Очистить </v-btn>
                    <v-alert
                        border="bottom"
                        color="pink darken-1"
                        dark
                        v-if="errors"
                        class="mt-4"
                    >
                        {{ errors }}
                    </v-alert>
                </form>
            </v-card-text>
            <v-card-subtitle>
                <nuxt-link to="/auth/"> Уже есть аккаунт? </nuxt-link>
            </v-card-subtitle>
        </v-card>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import {
    required,
    maxLength,
    minLength,
    email,
} from "vuelidate/lib/validators";

export default {
    mixins: [validationMixin],

    validations: {
        firstName: { required, minLength: minLength(2) },
        lastName: { required, minLength: minLength(2) },
        username: { required },
        password: { required, minLength: minLength(8) },
        email: { required, email },
    },

    data: () => ({
        firstName: "",
        lastName: "",
        username: "",
        password: "",
        email: "",
    }),

    props: {
        errors: {
            type: String,
            default: null,
        },
    },

    computed: {
        nameErrors() {
            const errors = [];
            if (!this.$v.username.$dirty) return errors;
            !this.$v.username.required &&
                errors.push("Введите имя пользователя");
            return errors;
        },
        firstNameErrors() {
            const errors = [];
            if (!this.$v.firstName.$dirty) return errors;
            !this.$v.firstName.required && errors.push("Введите имя");
            !this.$v.firstName.minLength && errors.push("Введите имя");
            return errors;
        },
        lastNameErrors() {
            const errors = [];
            if (!this.$v.lastName.$dirty) return errors;
            !this.$v.lastName.required && errors.push("Введите фамилию");
            !this.$v.lastName.minLength && errors.push("Введите фамилию");
            return errors;
        },
        passErrors() {
            const errors = [];
            if (!this.$v.password.$dirty) return errors;
            !this.$v.password.minLength && errors.push("Неверная длина");
            !this.$v.password.required && errors.push("Введите пароль");
            return errors;
        },
        emailErrors() {
            const errors = [];
            if (!this.$v.email.$dirty) return errors;
            !this.$v.email.email && errors.push("Неверная почта");
            !this.$v.email.required && errors.push("Введитте почту");
            return errors;
        },
    },

    methods: {
        submit() {
            this.$v.$touch();
            if (this.$v.$anyError) return;
            let user = {
                first_name: this.firstName,
                last_name: this.lastName,
                username: this.username,
                password: this.password,
                email: this.email,
            };
            this.$emit("submit", user);
        },
        clear() {
            this.$v.$reset();
            this.email = "";
            this.username = "";
            this.password = "";
        },
    },
};
</script>

<style>
.form_container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}
</style>
