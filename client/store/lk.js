export const state = () => ({
    resume: {}
})

export const actions = {
    nuxtServerInit({ commit }) {

    },
    setResume({ commit }, id) {
        return new Promise((resolve, reject) => {
            let token = this.app.store.getters['auth/getAccessToken']
            this.$axios.get(`api/v1/resumes/${id}/`, {
                withCredentials: true,
                headers: {
                    'Authorization': `Bearer ${token}`,
                }
            }).then(res => {
                commit('setResume', res.data.data)
                resolve(res.data.data)
            }).catch((err) => {
                reject(err)
            })
        })
    }
}

export const mutations = {
    setResume(state, resume) {
        state.resume = resume
    }
}

export const getters = {
    getResume: s => s.resume
}