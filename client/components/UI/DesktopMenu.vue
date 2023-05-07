<template>
    <div class="text--secondary align-center">
        <div v-for="item in menu">
            <v-menu :key="item.to" v-if="!item.submenu" open-on-hover offset-y>
                <template v-slot:activator="{ on, attrs }">
                    <v-col color="primary" class="menu_item" @click="$router.push(item.to)">
                        {{ item.title }}
                    </v-col>
                </template>
            </v-menu>
            <v-menu v-else open-on-hover offset-y>
                <template v-slot:activator="{ on, attrs }">
                    <v-col color="primary" class="menu_item" v-bind="attrs" v-on="on">
                        {{ item.title }}
                    </v-col>
                </template>
                <v-list>
                    <v-list-item exact :key="subitem.to" :href="subitem.href ? subitem.href: ''" v-for="subitem in item.submenu" :nuxt="!!subitem.href" active-class="activeLink" :to="subitem.to">
                        <v-list-item-icon class="mr-1">
                            <v-icon small>{{ subitem.ico }}</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>{{ subitem.title }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        menu: []
    }
}
</script>

<style lang="scss">
.menu_item {
    &:hover {
        color: black !important;
        cursor: pointer
    }
}
</style>