<template>
    <div class="auth_container">
        <AuthForm :errors="errors" @submit="submit"/>
    </div>
</template>

<script>
import AuthForm from '@/components/auth/auth_form.vue'

export default {
    head(){
        let descr = 'Авторизация на портале ФИСТ',
            title = 'Войти',
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
    components:{
        AuthForm
    },
    data(){
        return{
            errors: null
        }
    },
    methods: {
        submit(data){
            this.$store.dispatch('auth/login', data).then(res=>{
                if(res){
                    this.errors = null
                    this.$router.push('/')
                }
            }).catch(res=>this.errors=res)
        }
    },
}
</script>

