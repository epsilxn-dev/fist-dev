export const state = () => ({
    projects: []
})

export const actions = {
    setProjects({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/projects').then(res => {
                commit('setProjects', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения проектов', err)
            })
        })
    }
}

export const mutations = {
    setProjects(state, projects) {
        state.projects = projects
    }
}

export const getters = {
    getProjects: s => s.projects
}