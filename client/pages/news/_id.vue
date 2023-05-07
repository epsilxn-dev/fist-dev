<template>
    <v-container v-if="newsItem" class="mt-4 pa-2">
        <v-row no-gutters>

            <v-col class="col col-2 d-none d-flex"></v-col>
            <v-col class="col col-md-8 col-12">
                <h1 class="text-h4 my-2">{{newsItem.title}}</h1>
                <v-breadcrumbs class="pa-0 pb-2" :items="breadcrumbs"></v-breadcrumbs>
                <v-card>
                    <v-card-text class="">
                        <v-img :src="base+newsItem.image" height="400"></v-img>
                        <div class="d-flex justify-space-between align-center mt-4">
                            <div>{{newsItem.created_at}}</div>
                            <TagList v-if="newsItem.tags" :tags="newsItem.tags"/>
                        </div>
                        <div v-html="newsItem.text" class="news-paragraph-image mt-4"/>
                    </v-card-text>
                </v-card>
                <div class="w-100 comments" v-if="commentaries.length > 0">
                    <div class="text-h5 text-center my-5">Комментарии</div>
                    <v-card class="py-4 pb-0 color--white d-flex flex-column justify-center align-center">
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
                            />
                            <div class="answers_container pl-10" v-if="item.replies">
                                <CommentItem
                                    class="answer ml-5 my-2 mb-4"
                                    v-for="(answer, j) in item.replies"
                                    :key="j"
                                    :index="j"
                                    :answer="true"
                                    @reply="reply"
                                    @delete="deleteComment"
                                    :comment="answer"
                                />
                            </div>
                        </div>

                    </v-card>
                </div>
                <div v-else class="text-h5 text-center text--secondary my-5">Пока комментариев нет</div>
                <AddComment
                    id="AddComments"
                    v-if="Object.keys(user).length"
                    @addComment="addComment"
                    @reset="reset"
                    class="my-5"
                    :to="to"/>
                <div v-else class="text-h5 text-center text--secondary my-5">
                <Nuxt-link class="text-h5" to="/auth">Авторизируйтесь </Nuxt-link>для отправки комментария</div>
            </v-col>
            <v-col class="col d-none d-flex"></v-col>
        </v-row>
    </v-container>
</template>
<script>
import TagList from '~/components/UI/TagList.vue'
import { mapState } from 'vuex'
import AddComment from '~/components/news/AddComment.vue'
import CommentItem from '~/components/UI/CommentItem.vue'
export default {
    components:{
        TagList,
        AddComment,
        CommentItem
    },
    head(){
        let descr = this.newsItem.description,
            title = this.newsItem.title,
            type = 'article',
            image = this.base+this.newsItem.image
        return {
            title: title,
            meta: [
                {hid: 'description', name: 'description', content: descr},
                {hid: 'og:title', name: 'og:title', content: descr},
                {hid: 'og:description', name: 'og:description', content: descr},
                {hid: 'og:type', name: 'og:type', content: type},
                {hid: 'og:image', name: 'og:image', content: image},
                {hid: 'vk:image', name: 'vk:image', content: image},
            ]
        }
    },
    fetch() {
        this.id = this.$route.params.id

        this.$axios.get(`api/v1/news-commentaries/?news=${this.id}`).then(res => {
            this.newsComments = res.data.data.results
        }).catch((err) => {
            this.newsComments = false
        })


        this.$axios.get(`api/v1/news/${this.id}`).then(res => {
            this.newsItem = res.data.data
        }).catch((err) => {
            this.error = err
        })

        this.breadcrumbs.push({
            text: this.id,
            disabled: true,
            to: `/${this.id}`,
        })
    },
    data() {
        return ({
            to: false,
            id: -1,
            newsItem: false,
            breadcrumbs: [
                {
                    text: 'fist.ulstu.ru',
                    to: '/',
                },
                {
                    text: 'news',
                    exact: true,
                    to: '/news',
                },
            ],
            newsComments: []
        })
    },
    methods:{
        reset(){
            this.to = false
        },
        reply(comment){
            this.to = comment
        },
        addComment(comment){
            this.$axios.post(`api/v1/news-commentaries/`,
                {
                    parent_id: this.to ? this.to.id: false,
                    news: this.id,
                    text: comment
                },
                {
                    withCredentials: true,
                    headers: {
                        'Authorization': `Bearer ${this.accessToken}`,
                    }
            }).then((res)=> {
                this.newsComments.push(res.data.data)
            })
        },
        deleteComment(id, index){
            this.$axios.delete(`api/v1/news-commentaries/${id}`, {
                withCredentials: true,
                headers: {
                    'Authorization': `Bearer ${this.accessToken}`,
                }
            }).then(res=> this.newsComments.splice(this.newsComments.findIndex(item=>item.id==id), 1))
        }
    },
    computed:{
        commentaries(){
            if (!this.newsComments) return []
            let comments = this.newsComments ? [...this.newsComments] : []
            let parentCount = false
            for(let item of comments){
                item.replies = []
                if (!item.parent_id) parentCount=true
                item.author = item.author
                item.text = item.text
                for (let j of this.newsComments){
                    if(item.id == j.parent_id) {
                        j.to = item.id
                        item.replies.push(j)
                    }
                }
            }
            return parentCount ? comments : []
        },
        ...mapState('auth', ['accessToken', 'base']),
        user:{
            get() {
                return this.$store.getters['auth/getUser']
            },
            set(newValue) {
                this.$store.commit('auth/setUser', newValue)
            }
        }
    }

}
</script>
<style scoped>
.w-70{
  width: 70% !important
}

.w-100{
  width: 100% !important;
}
.comments{
  margin: 0 auto
}


</style>

<style>
.news-paragraph-image img{
    max-width: 100% !important;
}
</style>
