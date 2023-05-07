export const state = () => ({
    users: []
})

export const actions = {
    setUsers({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/users/').then(res => {
                commit('setUsers', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения пользователей', err)
            })
        })
    }
}

export const mutations = {
    setUsers(state, users) {
        state.users = users
    }
}

export const getters = {
    getUsers: s => s.users
}