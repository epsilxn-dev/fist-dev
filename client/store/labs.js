export const state = () => ({
    labs: []
})

export const actions = {
    setLabs({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/laboratories/').then(res => {
                commit('setLabs', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения лабораторий', err)
            })
        })
    }
}

export const mutations = {
    setLabs(state, labs) {
        state.labs = labs
    }
}
export const getters = {
    getLabs: s => s.labs
}