<template>
    <div>
        <v-card :class="{redBorder: errorMessages}">  
            <v-card-text :disabled="disable" class="pb-0">
                <v-expansion-panels>
                    <v-expansion-panel>
                        <v-expansion-panel-header>
                            Член команды
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <v-text-field
                                clearable
                                v-model="user.name"
                                outlined
                                @input="$v.user.name.$touch()"
                                @blur="$v.user.name.$touch()"
                                :error-messages="nameErrors"
                                label="Имя Фамилия"
                            ></v-text-field>
                            <v-text-field
                                clearable
                                v-model="user.email"
                                outlined
                                @input="$v.user.email.$touch()"
                                @blur="$v.user.email.$touch()"
                                :error-messages="emailErrors"
                                label="Электронная почта"
                            ></v-text-field>
                            <v-text-field
                                clearable
                                v-model="user.phone"
                                outlined
                                @input="$v.user.phone.$touch()"
                                @blur="$v.user.phone.$touch()"
                                :error-messages="phoneErrors"
                                label="Номер телефона"
                            ></v-text-field>
                            <div class="d-flex justify-center">
                                <v-btn color="success lighten-2" small fab nuxt>
                                    <v-icon @click="setTeam">
                                        mdi-plus
                                    </v-icon>
                                </v-btn>
                            </div>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>
            </v-card-text>
            <v-card-text class="pt-0">
                <ResultTeam @edit="editTeam" @delete="deleteTeam" v-if="resultTeam.length!=0" :team="resultTeam" class="mt-6"/>
            </v-card-text>
        </v-card>
    </div>
</template>


<script>
import Swal from 'sweetalert2'
import ResultTeam from '@/components/ideas/ResultTeam'
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, minValue, maxValue, numeric } from 'vuelidate/lib/validators'
export default {
    components: {
        ResultTeam
    },
    created(){
        this.team = this.teamList
        this.resultTeam = this.team
    },
    validations: {
        user:{
            name: { required, minLength: minLength(5), maxLength: maxLength(30) },
            email: {required, email},
            phone: {required, minValue: minValue(89000000000),maxValue: maxValue(89999999999)}
        }
    },
    mixins: [validationMixin],
    props: {
        teamList:[],
        errorMessages: false
    },
    data() {
        return({
            disable: false,
            user:{},
            team: [{}],
            resultTeam: []
        })
        
    },
    methods:{
        setTeam(){
            this.$v.user.$touch()
            if(this.$v.user.$anyError){
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: 'Проверьте данные',
                    showConfirmButton: false,
                    timer: 3000
                })
                return
            }
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'Член команды добавлен',
                showConfirmButton: false,
                timer: 3000
            })
            this.disable=true
            this.resultTeam.push(this.user)
            this.$emit('setTeam', this.resultTeam)
            this.user={}
        },
        editTeam(id){
            this.user = this.resultTeam[id]
            this.resultTeam.splice(id, 1)
        },
        deleteTeam(id){
            this.resultTeam.splice(id, 1)
            this.$emit('setTeam', this.resultTeam)
        }
    },
    computed:{
        nameErrors () {
            const errors = []
            if (!this.$v.user.name.$dirty) return errors
            !this.$v.user.name.maxLength && errors.push('Введите допустимое имя')
            !this.$v.user.name.minLength && errors.push('Введите допустимое имя')
            !this.$v.user.name.required && errors.push('Имя обязательно')
            return errors
        },
        emailErrors () {
            const errors = []
            if (!this.$v.user.email.$dirty) return errors
            !this.$v.user.email.email && errors.push('Неверный формат почты')
            !this.$v.user.email.required && errors.push('Почта обязательна')
            return errors
        },
        phoneErrors () {
            const errors = []
            if (!this.$v.user.phone.$dirty) return errors
            !this.$v.user.phone.minValue && errors.push('Неверный формат номера')
            !this.$v.user.phone.maxValue && errors.push('Неверный формат номера')
            !this.$v.user.phone.required && errors.push('Телефон обязателен')
            return errors
        },

    }
}
</script>

