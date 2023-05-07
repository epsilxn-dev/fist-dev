export const state = () => ({
    graduates: [],

})

export const actions = {
    setGraduates({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/graduates').then(res => {
                commit('setGraduates', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения выпускников', err)
            })
        })
    }
}

export const mutations = {
    setGraduates(state, graduates) {
        state.directs = graduates
    }
}
export const getters = {
    getGraduates: s => s.graduates,
}