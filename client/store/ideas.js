export const state = () => ({
    ideas: []
})

export const actions = {
    setIdeas({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/ideas').then(res => {
                commit('setIdeas', res.data.data)
                resolve(res.data.data)
            }).catch((err) => {
                reject('Ошибка получения идей', err)
            })
        })
    }
}

export const mutations = {
    setIdeas(state, ideas) {
        state.ideas = ideas
    }
}


export const getters = {
    getIdeas: s => s.ideas
}