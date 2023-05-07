<template>
    <v-card>
        <v-card-text>
            <small>Поиск по тегам</small>
            <v-autocomplete
              class="mt-4"
              v-model="model"
              :items="foundedTags"
              :loading="isLoading"
              :search-input.sync="search"
              dense outlined
              hide-details
              hide-selected
              item-text="name"
              item-value="name"
              label="Другой тег"
              placeholder="Введите тег, чтоб найти"
              prepend-icon="mdi-magnify"
            >
              <template v-slot:no-data>
                <v-list-item>
                  <v-list-item-title>
                    Тега не найдено
                  </v-list-item-title>
                </v-list-item>
              </template>
              <template v-slot:selection="{ attr, on, item, selected }">
                <v-chip
                  v-bind="attr"
                  :input-value="selected"
                  color="blue-grey"
                  class="white--text"
                  v-on="on"
                  small
                >
                  <span class="caption" v-text="item.name"></span>
                </v-chip>
              </template>
            </v-autocomplete>
            <v-chip-group
                v-if="tags"
                column
                v-model="selectedTag"
                class="d-flex flex-wrap chip-group justify-center"
            >
                <v-chip
                    small
                    active-class="purple--text lighten-5 text--accent-5"
                    mandatory
                    dark
                    :color="colors[index % colors.length]"
                    v-for="(tag, index) in filteredTags" :key="index"
                >
                    <div v-if="tag" class="caption">
                        {{tag.name}}
                    </div>
                </v-chip>
                <v-btn v-if="toShow < tags.length" @click="showMore" class="mb-2" x-small fab>
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              <v-btn v-else @click="toShow=7" class="ma-2" x-small fab>
                <v-icon>mdi-minus</v-icon>
              </v-btn>
            </v-chip-group>
            <small>Сортировать</small>
            <v-radio-group v-model="reverse">
                <v-radio
                    :label="'Сначала новые'"
                    :value="false"
                ></v-radio>
                <v-radio
                    :label="'Сначала старые'"
                    :value="true"
                >
                </v-radio>
            </v-radio-group>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="applyFilters" color="primary" small>
                Найти
            </v-btn>
        </v-card-actions>
    </v-card>
</template>


<script>
export default {
    mounted() {
      this.$axios.get('api/v1/tags')
        .then(res => {
          this.tags = res.data.data.results
        })
        .catch((err) => {
        })
    },
    data(){
        return{
            toShow: 5,
            tags: false,
            tags2: [],
            model: null,
            search: '',
            isLoading: false,
            foundedTags: [],
            reverse: false,
            selectedTag: 0,
            colors: [
                'primary',
                'success',
                'cyan',
                'red',
                'green',
                'indigo',
                'deep-purple'
            ]
        }
    },
    methods:{
        applyFilters(){
            let filters = {}
            filters.selectedTag = this.tags[this.selectedTag]?.name ? this.tags[this.selectedTag].name : ''
            filters.reverse=this.reverse
            this.$emit('applyFilters', filters)
        },
        showMore(){
          this.toShow+=7
        },
    },
    computed: {
        filteredTags(){
          let tags = [...this.tags].slice(0,this.toShow)
          for (let item of tags){
            if (item.name.length > 20){
              item.name = item.name.slice(0,17)+'...'
            }
          }
          return tags
        }
    },
    watch:{
      search (val) {
        if (this.foundedTags.length > 0) return
        if (this.isLoading) return
        this.isLoading = true
        this.$axios.get(`api/v1/tags?tag=${val}`)
          .then(res => {
            this.foundedTags = res.data.data.results
          })
          .catch((err) => {
            this.error = err
          })
          .finally(() => (this.isLoading = false))
      },
      model(val){
        if(val){
          let filters = {}
          filters.selectedTag=val
          filters.reverse=this.reverse
          this.$emit('applyFilters', filters)
        }
      },
      selectedTag(val){
        let filters = {}
        filters.selectedTag = this.tags[val]?.name ? this.tags[val].name : ''
        filters.reverse=this.reverse
        this.$emit('applyFilters', filters)
      }
    },

}
</script>

