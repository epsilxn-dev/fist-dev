export const state = () => ({
    teachers: []

})
export const actions = {
    setTeachers({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/lessoners').then(res => {
                commit('setTeachers', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения преподавателей', err)
            })
        })
    }
}

export const mutations = {
    setTeachers(state, teachers) {
        state.directs = teachers
    }
}

export const getters = {
    getTeachers: s => s.teachers,
}