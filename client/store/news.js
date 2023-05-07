export const state = () => ({
    news: [],

    isLazyLoading: false,
})
export const actions = {
    getMore({ commit, getters }, options) {

        if (options.counter === options.length) {
            return []
        }
        return new Promise((resolve, reject) => {
            let newNews = []
            for (let i = options.length; i < options.counter; i++) {
                newNews.push({
                    id: i,
                    title: 'Работа пошла',
                    date: '29.01.2021',
                    description: 'lorem svcvsd s csd scdkcdskcdsnkjsn dcjks ndcjksdnkjdsc nkjnsdc сыввввввввввввввввввв vdfdfvvdfdvf cds s csd sdccsdn jsdcn jksdc nsdnj cjksndc kjnsjk ncjs ndkjsdn cjksd n jksndc jksndckj nsdkj ndskjcn dskjn cdkjsn',
                    tags: [
                        'default',
                        'second',
                        'javaScript'
                    ],
                    image: 'https://rubtsovskmv.ru/wp-content/uploads/2021/12/предприниматели.jpeg'
                })

            }

            let payload = [...getters.getNews, ...newNews]
            commit('setNews', payload)
            resolve("Ок");

        })
    },
}
export const mutations = {
    setNews(state, newNews) {
        state.news = newNews
    },
    setLazyLoading(state, value) {
        state.isLazyLoading = value
    }
}

export const getters = {
    getNews: s => s.news,
    getLazyLoading: s => s.isLazyLoading,
    getNewsItem: s => (id) => s.news.find(n => n.id == id)
}