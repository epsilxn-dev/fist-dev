export const state = () => ({
    resumes: [],
    vacancies: []
})

export const actions = {

    setResumes({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/resumes').then(res => {
                commit('setResumes', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения резюмов', err)
            })
        })
    },
    setVacancies({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/vacancies').then(res => {
                commit('setVacancies', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения вакансий', err)
            })
        })
    }
}

export const mutations = {
    setResumes(state, resumes) {
        state.resumes = resumes
    },

    setVacancies(state, vacancies) {
        state.vacancies = vacancies
    }
}

export const getters = {
    getResumes: s => s.resumes,
    getVacancies: s => s.vacancies
}