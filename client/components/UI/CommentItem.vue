<template>
    <div>
        <v-card-text class="pa-0 d-flex justify-start align-center">
            <v-menu
                bottom
                rounded
                offset-x
            >
                <template v-slot:activator="{ on }">
                    <v-btn
                        v-ripple
                        icon
                        x-large
                        v-on="on"
                        :width="answer ? 50 : 70"
                        :height="answer ? 50 : 70"
                    >
                        <v-avatar dark color="primary" :size="answer ? 50 : 70">
                            <v-img v-if="comment.author.avatar" :src="base + comment.author.avatar"></v-img>
                            <div v-else>{{comment.author.username.slice(0,2)}}</div>
                        </v-avatar>
                    </v-btn>
                </template>

                <v-card class="pa-2 py-0">
                    <v-list-item-content class="justify-center">
                        <div class="mx-auto text-center">
                            <h3>{{ comment.author.username }}</h3>
                            <div class="text-caption mt-1 mt-3">
                                {{ comment.author.email }}
                            </div>
                        </div>
                    </v-list-item-content>
                </v-card>
            </v-menu>

            <div class="d-flex ml-4 flex-column justify-center">
                <div :class="{'text-body-1': answer}" class="text--primary mb-2">
                    {{comment.author.first_name}}
                    {{comment.author.last_name}}
                </div>
                <div class="text-body-2">
                    {{comment.text}}
                </div>

            </div>
        </v-card-text>
        <v-card-actions :class="{'pa-0': answer}" v-if="currentUser">
            <v-spacer></v-spacer>
            <v-btn @click="reply" href="#AddComments" color="primary" text v-if="currentUser.id && !answer">
                <v-icon>mdi-forum</v-icon>
            </v-btn>
            <v-btn
                @click="$emit('delete', comment.id, index)"
                color="red"
                icon
                v-if="currentUser.id == comment.author.id"
            >
                <v-icon style="transform: rotate(45deg)">mdi-plus</v-icon>
            </v-btn>
        </v-card-actions>
    </div>
</template>

<script>
import { mapState } from "vuex"
export default {
    props: {
        comment: {
            type: Object,
            required: true
        },
        answer:{
            type: Boolean,
            default: false
        },
        index: {
            type: Number,
            required: true
        }
    },
    methods: {
        reply(){
            this.$emit('reply', this.comment)
        }
    },
    computed:{
        ...mapState('auth', ['base', 'currentUser'])
    }
}
</script>

