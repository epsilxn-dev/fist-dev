<template>
    <v-autocomplete
      v-model="model"
      :items="tags"
      :loading="isLoading"
      :search-input.sync="search"
      chips
      hide-details
      hide-selected
      item-text="name"
      item-value="name"
      label="Поиск по сайту..."
      outlined
      @change="searchOnTag"
      dense
      
    >
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>
            Введите название тега
          </v-list-item-title>
        </v-list-item>
      </template>
      <template v-slot:selection="{ attr, on, item, selected }" v-on:onEnter="searchOnTag">
        <v-chip
          v-bind="attr"
          :input-value="selected"
          color="blue-grey"
          class="white--text"
          v-on="on"
          x-small
        >
          <v-icon class="caption" left>
            mdi-pound
          </v-icon>
          <span class="caption" v-text="item.name"></span>
        </v-chip>
      </template>
      <template v-slot:item="{ item }">
        <v-chip
          color="indigo"
          class="font-weight-light white--text"
          x-small
        >
          <div class="curp caption">
            {{ item.name}}
          </div>
        </v-chip>

        <v-list-item-action>
          <v-icon class="caption">mdi-pound</v-icon>
        </v-list-item-action>
      </template>
    </v-autocomplete>
</template>
<script>
export default {
    data: () => ({
      isLoading: false,
      model: null,
      search: null,
      tab: null,
      err: '',
      tags: [],
      k: 0
    }),

    watch: {
      model (val) {
        if (val != null) this.tab = 0
        else this.tab = null
      },
      search (val) {
        if (this.tags.length > 0) return
        this.isLoading = true
        this.$axios.get('api/v1/tags')
          .then(res => {
            this.tags = res.data.data.results
          })
          .catch((err) => {
            this.error = err
          })
          .finally(() => (this.isLoading = false))
      },
    },
    methods: {
      searchOnTag() {
        if(this.model) {
          let url = `/tags/${this.model}`
          this.$emit('search', this.model)
          this.$router.push(url)

        }
      }
    },
}
</script>
<style scoped>

</style>
