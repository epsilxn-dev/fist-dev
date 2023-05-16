<template>
    <div class="auth_container">
        <h3 v-if="!errors" class="text-center text-h5 mt-10">
            Подтверждение почты...
        </h3>
        <h3 v-else class="text-center text-h5 red--text mt-10">{{ errors }}</h3>
    </div>
</template>

<script>
import AuthForm from "@/components/auth/auth_form.vue";

export default {
    head() {
        let descr = "Подтверждение почты",
            title = "Подтверждение",
            type = "site";
        return {
            title: title,
            meta: [
                { hid: "description", name: "description", content: descr },
                { hid: "og:title", name: "og:title", content: descr },
            ],
        };
    },
    mounted() {
        this.$store
            .dispatch("auth/confirm", { token: this.$route.query.token })
            .then((res) => {
                if (res) {
                    this.$router.push("/auth");
                }
            })
            .catch((res) => (this.errors = "Ошибка подтверждения"));
    },
    components: {
        AuthForm,
    },
    data() {
        return {
            errors: null,
        };
    },
    methods: {
        submit(data) {},
    },
};
</script>
