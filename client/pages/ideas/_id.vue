<template>
    <v-container>
        <div v-if="idea">
            <v-img
                class="mt--2 labs_img d-flex text-center align-center justify-center"
                :src="base + idea.image"
                dark
                width="100%"
                gradient="to top right, rgba(0,0,0,.2), rgba(25,32,72,.5)"
            >
                <h1 class="text-h2">
                    {{ idea.name }}
                </h1>
            </v-img>
            <v-snackbar v-model="snackbar" timeout="3000">
                Авторизуйтесь для оценки или перезагрузите страницу
                <template v-slot:action="{ attrs }">
                    <v-btn color="blue" text v-bind="attrs" @click="snack">
                        Войти
                    </v-btn>
                </template>
            </v-snackbar>
            <v-row class="pa-2" no-gutters>
                <v-col class="col col-2 d-none d-md-block"></v-col>
                <v-col class="col col-12 col-md-8">
                    <h1 class="text-h4 my-2">Информация об идее</h1>
                    <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs" />
                    <h2 class="text-h5 mt-2">Описание:</h2>
                    <div v-html="idea.information" />
                    <h2 class="text-h5 mt-2">Области технологий:</h2>
                    <StackList :items="idea.area_tech" />
                    <h2 class="text-h5 mb-2">Автор проекта</h2>
                    <div v-if="idea.author" class="text--secondary mb-5">
                        <v-menu bottom rounded offset-x>
                            <template v-slot:activator="{ on }">
                                <v-btn icon x-large v-on="on">
                                    <v-avatar
                                        v-bind="$attrs"
                                        class="blue--text text--lighten-5"
                                        :color="
                                            colors[
                                                Math.floor(
                                                    Math.random() *
                                                        colors.length
                                                )
                                            ]
                                        "
                                    >
                                        <v-img
                                            v-if="idea.author.avatar"
                                            :src="base + idea.author.avatar"
                                        ></v-img>
                                        <div v-else>
                                            {{
                                                idea.author.username.slice(0, 2)
                                            }}
                                        </div>
                                    </v-avatar>
                                </v-btn>
                            </template>

                            <v-card class="pa-2 py-0">
                                <v-list-item-content class="justify-center">
                                    <div class="mx-auto text-center">
                                        <h3>{{ idea.author.username }}</h3>
                                        <div class="text-caption mt-1">
                                            {{
                                                idea.author.first_name +
                                                " " +
                                                idea.author.last_name
                                            }}
                                        </div>
                                        <div class="text-caption mt-1">
                                            {{ idea.author.email }}
                                        </div>
                                        <div class="text-caption">
                                            {{ idea.author.phone }}
                                        </div>
                                    </div>
                                </v-list-item-content>
                            </v-card>
                        </v-menu>
                    </div>
                    <h2 class="text-h5 my-2">Тэги</h2>
                    <TagList v-if="idea.tags" :tags="idea.tags" />
                    <div v-if="idea.likes" class="d-flex align-center">
                        <v-spacer />
                        {{ likes }}
                        <v-icon
                            :class="{ 'text--primary': isLiked }"
                            @click="like"
                            class="ma-2"
                        >
                            mdi-thumb-up
                        </v-icon>
                        {{ dislikes }}
                        <v-icon
                            :class="{ 'text--primary': isDisliked }"
                            @click="dislike"
                            class="ma-2"
                        >
                            mdi-thumb-down
                        </v-icon>
                    </div>
                    <div v-if="idea.team">
                        <h2 class="text-h5 my-2">Команда</h2>
                        <div class="my-4 d-flex justify-start">
                            <TeamItem
                                v-for="(item, index) in idea.team"
                                class="blue--text text--lighten-5 mr-2"
                                :key="index"
                                :user="item"
                                :color="
                                    colors[
                                        Math.floor(
                                            Math.random() * colors.length
                                        )
                                    ]
                                "
                            ></TeamItem>
                        </div>
                    </div>
                    <div v-if="idea.links">
                        <h2 class="text-h5 my-2">Ссылки</h2>
                        <div class="mb-5">
                            <a
                                v-for="(item, index) in idea.links"
                                :key="index"
                                :href="item.link"
                            >
                                {{ item.link }}
                                <br />
                            </a>
                        </div>
                    </div>
                    <div
                        class="w-100 comments"
                        v-if="commentaries.length !== 0"
                    >
                        <div class="text-h5 text-center my-5">Комментарии</div>
                        <v-card
                            class="py-4 mt-2 pb-0 color--white d-flex flex-column justify-center align-center"
                        >
                            <div
                                v-for="(item, index) in commentaries"
                                :key="index"
                                v-if="!item.parent_id"
                                class="w-100 px-4 mb-2 d-flex flex-column"
                            >
                                <CommentItem
                                    :index="index"
                                    @reply="reply"
                                    @delete="deleteComment"
                                    :comment="item"
                                ></CommentItem>
                                <div
                                    v-if="item.replies"
                                    class="answers_container pl-10"
                                >
                                    <CommentItem
                                        class="answer ml-5 my-2 mb-4"
                                        v-for="(answer, j) in item.replies"
                                        :key="j"
                                        :index="j"
                                        :answer="true"
                                        @reply="reply"
                                        @delete="deleteComment"
                                        :comment="answer"
                                    ></CommentItem>
                                </div>
                                <v-divider
                                    v-if="index !== commentaries.length - 1"
                                ></v-divider>
                            </div>
                        </v-card>
                    </div>
                    <div
                        v-else
                        class="text-h5 text-center text--secondary my-5"
                    >
                        Пока комментариев нет
                    </div>
                    <AddComment
                        id="AddComments"
                        v-if="Object.keys(user).length"
                        @addComment="addComment"
                        @reset="reset"
                        class="my-5"
                        :to="to"
                    ></AddComment>
                    <div
                        v-else
                        class="text-h5 text-center text--secondary my-5"
                    >
                        <Nuxt-link class="text-h5" to="/auth"
                            >Авторизируйтесь</Nuxt-link
                        >
                        для отправки комментария
                    </div>
                </v-col>
                <v-col class="d-none d-md-block"> </v-col>
            </v-row>
        </div>
        <div v-else>
            <div class="text-center mt-10">
                Вероятно, идея не была промодерирована
            </div>
        </div>
    </v-container>
</template>

<script>
import TeamItem from "~/components/projects/TeamItem.vue";
import TagList from "~/components/UI/TagList.vue";
import { mapState } from "vuex";
import StackList from "~/components/labs/StackList.vue";
import AddComment from "~/components/news/AddComment.vue";
import CommentItem from "~/components/UI/CommentItem.vue";
export default {
    head() {
        let descr = this.idea.information,
            title = this.idea.name,
            type = "site",
            image = this.base + this.idea.image;
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
                { hid: "og:image", name: "og:image", content: image },
                { hid: "vk:image", name: "vk:image", content: image },
            ],
        };
    },
    components: {
        TagList,
        StackList,
        TeamItem,
        AddComment,
        CommentItem,
    },
    async fetch() {
        this.ideaId = this.$route.params.id;
        this.$axios
            .get(`api/v1/commentaries/?idea=${this.ideaId}`)
            .then((res) => {
                this.ideaComments = res.data.data.results;
            })
            .catch((err) => {
                this.error = err;
                this.ideaComments = [];
            });
        if (this.$store.getters["ideas/getIdeas"].length === 0) {
            this.idea = await this.$store.dispatch("ideas/setIdeas");
        } else {
            this.idea = await this.$store.getters["ideas/getIdeas"];
        }

        this.idea = this.idea.find((item) => item.id == this.ideaId);
        if (!this.idea) this.idea = false;
        this.likes = this.idea.likes.length;
        this.dislikes = this.idea.dislikes.length;
        for (let item of this.idea.likes) {
            if (item == this.user.id) {
                this.isLiked = true;
            }
        }

        for (let item of this.idea.dislikes) {
            if (item == this.user.id) {
                this.isDisliked = true;
            }
        }
        this.breadcrumbs.push({
            text: this.ideaId,
            disabled: true,
            to: `/ideas/${this.ideaId}`,
            exact: true,
        });
    },
    data() {
        return {
            authorId: false,
            snackbar: false,
            colors: [
                "primary",
                "success",
                "cyan",
                "red",
                "green",
                "indigo",
                "deep-purple",
            ],
            breadcrumbs: [
                {
                    text: "fist.ulstu.ru",
                    to: "/",
                    exact: true,
                },
                {
                    text: "ideas",
                    to: "/ideas",
                    exact: true,
                },
            ],
            idea: false,
            to: false,
            likes: 0,
            dislikes: 0,
            isLiked: false,
            isDisliked: false,
            ideaId: 0,
            ideaComments: [],
        };
    },
    methods: {
        reply(comment) {
            this.to = comment;
        },
        reset() {
            this.to = false;
        },
        snack() {
            this.snackbar = false;
            this.$router.push("/auth");
        },
        like() {
            this.$axios
                .post(
                    "api/v1/ideas/likes/",
                    {
                        id: this.ideaId,
                    },
                    {
                        withCredentials: true,
                        headers: {
                            Authorization: `Bearer ${this.accessToken}`,
                        },
                    }
                )
                .then((res) => {
                    if (res.data.data) {
                        this.likes += 1;
                        if (this.isDisliked) {
                            this.dislikes -= 1;
                        }
                    } else {
                        this.likes -= 1;
                    }
                    this.isLiked = res.data.data;
                    this.isDisliked = false;
                })
                .catch((res) => (this.snackbar = true));
        },
        dislike() {
            this.$axios
                .post(
                    "api/v1/ideas/dislikes/",
                    {
                        id: this.ideaId,
                    },
                    {
                        withCredentials: true,
                        headers: {
                            Authorization: `Bearer ${this.accessToken}`,
                        },
                    }
                )
                .then((res) => {
                    if (res.data.data) {
                        this.dislikes += 1;
                        if (this.isLiked) {
                            this.likes -= 1;
                        }
                    } else {
                        this.dislikes -= 1;
                    }
                    this.isDisliked = res.data.data;
                    this.isLiked = false;
                })
                .catch((res) => (this.snackbar = true));
        },
        deleteComment(id) {
            this.$axios
                .delete(`api/v1/commentaries/${id}`, {
                    withCredentials: true,
                    headers: {
                        Authorization: `Bearer ${this.accessToken}`,
                    },
                })
                .then((res) =>
                    this.ideaComments.splice(
                        this.ideaComments.findIndex((item) => item.id == id),
                        1
                    )
                );
        },

        addComment(comment) {
            this.$axios
                .post(
                    `api/v1/commentaries/`,
                    {
                        parent_id: this.to ? this.to.id : null,
                        idea: this.ideaId,
                        message: comment,
                    },
                    {
                        withCredentials: true,
                        headers: {
                            Authorization: `Bearer ${this.accessToken}`,
                        },
                    }
                )
                .then((res) => {
                    let result = JSON.parse(JSON.stringify(res.data.data));
                    if (!result.to) {
                        result = { ...result, replies: [] };
                        this.ideaComments.push(result);
                    }
                });
        },
        getRandomColor() {
            return this.colors[Math.floor(Math.random() * this.colors.length)];
        },
    },
    computed: {
        commentaries() {
            let comments = this.ideaComments ? [...this.ideaComments] : [];
            let parentCount = false;
            for (let item of comments) {
                item.replies = [];
                if (!item.parent_id) parentCount = true;
                item.author = item.user;
                item.text = item.message;
                for (let j of comments) {
                    if (item.id == j.parent_id && j.parent_id) {
                        j.to = item.id;
                        item.replies.push(j);
                    }
                }
            }
            return parentCount ? comments : [];
        },
        ...mapState("auth", ["accessToken", "base"]),
        user: {
            get() {
                return this.$store.getters["auth/getUser"];
            },
            set(newValue) {
                this.$store.commit("auth/setUser", newValue);
            },
        },
    },
};
</script>

<style>
.w-70 {
    width: 70% !important;
}

.w-100 {
    width: 100%;
}

.comments {
    margin: 0 auto;
}
</style>
