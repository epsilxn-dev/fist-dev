<template>
    <div class="auth_container">
        <RegForm class="ma-2 my-10" :errors="errors" @submit="submit"/>
    </div>
</template>


<script>
import RegForm from '~/components/auth/reg_form.vue'
import Swal from 'sweetalert2'
export default {
    head(){
        let descr = 'Регистрация на портале ФИСТ',
            title = 'Регистрация',
            type = 'site'
        return {
            title: title,
            meta: [
                {hid: 'description', name: 'description', content: descr},
                {hid: 'og:title', name: 'og:title', content: descr},
                {hid: 'og:description', name: 'og:description', content: descr},
                {hid: 'og:type', name: 'og:type', content: type},
            ]
        }
    },
    components: {
        RegForm
    },
    data(){
        return{
            errors: null
        }
    },
    methods: {
        submit(data){
            this.$store.dispatch('auth/signUp', data).then(res=>{
                Swal.fire('Успешно', 'Ccылка для подтверждения отправлена на почту','success')
                this.errors = null
            }).catch(res=>this.errors=res)
        }
    },
}
</script>
