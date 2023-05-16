<template>
    <v-container class="mt-4 pa-2">
        <v-row no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8">
                <v-row class="pa-2 mb-2">
                    <h1 class="text-h4 title text--primary">Преподаватели</h1>
                </v-row>
                <v-breadcrumbs
                    class="pa-0 pb-2"
                    :items="breadcrumbs"
                ></v-breadcrumbs>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="col col-2"></v-col>
            <v-col class="col col-12 col-md-8">
                <v-container
                    v-if="filteredTeachers.length"
                    class="d-flex flex-wrap"
                >
                    <teacher-item
                        v-for="(teacher, index) in filteredTeachers"
                        :key="index"
                        :item="teacher"
                        class="grad_card mr-4 mt-4 mb-2"
                    ></teacher-item>
                </v-container>
                <no-info v-else></no-info>
            </v-col>
            <v-col class="col">
                <department-filter
                    :departments="departments"
                    @applyFilters="applyFilters"
                ></department-filter>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import DepartmentFilter from "@/components/teachers/DepartmentFilter.vue";
import TeacherItem from "@/components/teachers/TeacherItem.vue";
import NoInfo from "~/components/UI/NoInfo.vue";

export default {
    components: {
        "teacher-item": TeacherItem,
        "department-filter": DepartmentFilter,
        "no-info": NoInfo,
    },
    head() {
        let descr =
                "Список всех преподаватаелей факультета информационных систем и технологий",
            title = "Преподаватели",
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
    async fetch() {
        this.$store
            .dispatch("departments/setDepartments")
            .then((res) => (this.departments = res));

        await this.$store
            .dispatch("teachers/setTeachers")
            .then((res) => (this.teachers = res));

        this.filter = [...this.departments.map((e) => e.name)];

        for (let d of this.departments) {
            this.departmentColors[d.name] = this.colors[d.id];
        }
        for (let t of this.teachers) {
            t.departmentColor = this.departmentColors[t.department];
        }
    },
    data() {
        return {
            news: [],
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                },
                {
                    text: "teachers",
                    disabled: true,
                    exact: true,
                    to: "/teachers",
                },
            ],
            departments: [],
            colors: [
                "primary",
                "success",
                "red",
                "green",
                "cyan",
                "indigo",
                "deep-purple",
            ],
            departmentColors: [],
            teachers: [],
            filter: [],
        };
    },
    methods: {
        applyFilters(filter) {
            this.filter = filter;
        },
    },
    computed: {
        filteredTeachers() {
            return this.teachers.filter((item) => {
                return this.filter.includes(item.department.name) && item;
            });
        },
    },
};
</script>
<style lang="scss" scoped>
.grad_card {
    width: 31.2% !important;
    @media screen and (max-width: 600px) {
        width: 98% !important;
    }
}
</style>
