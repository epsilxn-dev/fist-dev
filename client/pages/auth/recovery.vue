<template>
    <div class="auth_container">
        <RecoveryForm @submit="submit"/>
    </div>
</template>

<script>
import Swal from 'sweetalert2'
import RecoveryForm from '@/components/auth/recovery_form.vue'

export default {
    head(){
        let descr = 'форма восстановления пароля на портале ФИСТ',
            title = 'Восстановление',
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
    mounted(){
        this.token = this.$route.query.token
        if (!this.token) this.$router.push("/auth")
    },
    components:{
        RecoveryForm
    },
    data(){
        return{
            token: null,
            errors: null
        }
    },
    methods: {
        submit(data){
            this.$axios.post('api/auth/confirm_password/', {...data, token: this.token}).then(res=>{
                Swal.fire(
                    'Успешно',
                    'Пароль успешно изменён!',
                    'success'
                )
                this.$router.push("/auth")
            }).catch(res=>{
                Swal.fire(
                    'Ошибка',
                    'Проверьте данные',
                    'error'
                )
            })
            
        }
    },
}
</script>

