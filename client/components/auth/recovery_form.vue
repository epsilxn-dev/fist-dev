<template>
    <div class="form_container">
        <v-card width="500">
            <v-card-title>Придумайте новый пароль</v-card-title>
            <v-card-text>
                <form @keyup.enter="submit">
                    <v-text-field
                        type="password"
                        v-model="password"
                        :error-messages="passErrors"
                        label="Пароль"
                        required
                        @input="$v.password.$touch()"
                        @blur="$v.password.$touch()"
                    ></v-text-field>
                    <v-text-field
                        type="password"
                        v-model="confirmPassword"
                        :error-messages="confPassErrors"
                        label="Подтвердите пароль"
                        required
                        @input="$v.confirmPassword.$touch()"
                        @blur="$v.confirmPassword.$touch()"
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
                <nuxt-link to="/auth/"> Войти в аккаунт </nuxt-link>
            </v-card-subtitle>
        </v-card>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength, sameAs } from "vuelidate/lib/validators";

export default {
    data: () => ({
        password: "",
        confirmPassword: "",
    }),
    mixins: [validationMixin],

    validations() {
        return {
            password: { required, minLength: minLength(8) },
            confirmPassword: {
                required,
                sameAs: sameAs("password"),
                minLength: minLength(8),
            },
        };
    },

    props: {
        errors: {
            type: String,
            default: null,
        },
    },

    computed: {
        passErrors() {
            const errors = [];
            if (!this.$v.password.$dirty) return errors;
            !this.$v.password.minLength && errors.push("Неверная длина");
            !this.$v.password.required && errors.push("Введите пароль");
            return errors;
        },
        confPassErrors() {
            const errors = [];
            if (!this.$v.confirmPassword.$dirty) return errors;
            !this.$v.confirmPassword.minLength && errors.push("Неверная длина");
            !this.$v.confirmPassword.sameAs &&
                errors.push("Пароли не совпадают");
            !this.$v.confirmPassword.required && errors.push("Введите пароль");
            return errors;
        },
    },

    methods: {
        submit() {
            this.$v.$touch();
            if (this.$v.$anyError) return;
            let user = {
                password: this.password,
            };
            this.$emit("submit", user);
        },
        clear() {
            this.$v.$reset();
            this.password = "";
            this.confirmPassword = "";
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
