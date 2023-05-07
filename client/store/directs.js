export const state = () => ({
    directs: [

    ],

})

export const actions = {
    setDirections({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/specialties').then(res => {
                commit('setDirections', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения направлений', err)
            })
        })
    }
}

export const mutations = {
    setDirections(state, directions) {
        state.directs = directions
    }
}
export const getters = {
    getDirections: s => s.directs
}