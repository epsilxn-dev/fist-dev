<template>
    <v-card class="ma-4">    
        <v-container fluid class="d-flex flex-column align-center">
            <v-card-title class="title text--primary">Кафедры</v-card-title>
            <v-checkbox 
                class="mx-4 align-self-start"
                v-for="(department,index) in departments"
                :key="index" v-model="departmentsApply"  
                :value="department.name" 
                :label="`${department.name}`"
            >
                {{department}}            
            </v-checkbox>
        </v-container>
    </v-card>
</template>
<script>
export default {
    props: {
        departments: {
            type: Array,
            required: true,
            default: []
        }
    },
    data() {
        return {
            departmentsApply: [...this.departments.map(e => e.name)]      
        }
    },
    watch: {
        departmentsApply: function(value, oldValue) {
            this.$emit('applyFilters', value)
        }
    },
}
</script>