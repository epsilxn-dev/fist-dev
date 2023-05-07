<template>
    <div style="max-width: 50px">
        <v-menu
            bottom
            rounded
            offset-x
        >
            <template v-slot:activator="{ on }">
                <v-btn
                    icon
                    x-large
                    v-on="on"
                >
                    <v-avatar
                        v-bind="$attrs"
                        size="48"
                        dark
                    >   <v-img v-if="user.avatar" :src="base+user.avatar"></v-img>
                        <div v-else>
                            {{user.username.slice(0,2)}} 
                        </div>
                    </v-avatar>
                </v-btn>
            </template>
            
            <v-card class="pa-2 py-0">
                <v-list-item-content class="justify-center">
                    <div class="mx-auto text-center">
                        <h3>{{ user.name }}</h3>
                        <div class="text-caption mt-1">
                            {{ user.email }}
                        </div>
                        <div class="text-caption">
                            {{ user.phone }}
                        </div>
                    </div>
                </v-list-item-content>
            </v-card>
        </v-menu>
    </div>
</template>

<script>
import { mapState } from "vuex"
export default {
    props: {
        user: {

        }
    },
    computed: {
        ...mapState('auth', ['base'])
    }
}
</script>

