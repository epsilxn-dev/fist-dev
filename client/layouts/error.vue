<template>
  <v-app class="d-flex align-center justify-center">
    <v-col class="d-flex flex-column align-center justify-center">
      <h1 v-if="this.error.statusCode" class="text-center font-weight-medium code__error">
        4<img :src="require('@/assets/images/img/something_went_wrong.png')"/>4
      </h1>
      <h1 v-else class="text-center font-weight-medium code__error">5<img :src="require('@/assets/images/img/something_went_wrong.png')"/>X</h1>
      <p>Неизвестная ошибка</p>
      <v-btn color="primary" nuxt to="/"> 
        <v-icon class="mr-2">mdi-arrow-left</v-icon>
        Главная
      </v-btn>
    </v-col>

  </v-app>
</template>

<script>
export default {
  layout: "empty",
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      pageNotFound: 'Ошибка 404',
      otherError: 'Неизвестная ошибка'
    }
  },
  head () {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  }
}
</script>

<style scoped>
.h-100{
  height: 100vh !important;
}
.h-100p{
  height: 100% !important;
}
.code__error {
  font-size: 300px;
  color: #161c2d;
  margin: 0;
  line-height: 320px;
}
</style>
