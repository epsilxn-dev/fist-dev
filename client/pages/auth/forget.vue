<template>
    <div class="auth_container">
        <ForgetForm @submit="submit" />
    </div>
</template>

<script>
import Swal from "sweetalert2";
import ForgetForm from "@/components/auth/forget_form.vue";

export default {
    head() {
        let descr = "Восстановление пароля по почте",
            title = "Восстановление",
            type = "site";
        return {
            title: title,
            meta: [
                { hid: "description", name: "description", content: descr },
                { hid: "og:title", name: "og:title", content: descr },
                {
                    hid: "og:description",
                    name: "og:description",
                    content: descr,
                },
                { hid: "og:type", name: "og:type", content: type },
            ],
        };
    },
    components: {
        ForgetForm,
    },
    data() {
        return {
            token: null,
            errors: null,
        };
    },
    methods: {
        submit(data) {
            this.$axios
                .post("api/auth/forgot_password/", data)
                .then((res) => {
                    Swal.fire(
                        "Успешно",
                        "Ссылка для восстановления была отправлена на почту!",
                        "success"
                    );
                })
                .catch((res) => {
                    Swal.fire("Успешно!", "Ошибка!", "error");
                });
        },
    },
};
</script>
