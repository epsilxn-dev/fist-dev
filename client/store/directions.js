export const state = () => ({
    directions: [{
            id: 0,
            name: 'ПИбд'
        },
        {
            id: 1,
            name: 'ИСТ'
        },
        {
            id: 2,
            name: 'ИВТ'
        },
    ],
})

export const actions = {
    setDirections({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.post('api/v1/specialties/', data, { withCredentials: true }).then(res => {
                commit('setDirections', user)
                resolve(user)
            }).catch((err) => {
                reject('Ошибка получения напр2авлений')
            })
        })
    }
}

export const mutations = {
    setDirections(state, directions) {
        state.directions = directions
    }
}
export const getters = {
    getDirections: s => s.directions
}
