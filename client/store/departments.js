export const state = () => ({
    departments: [{
            id: 0,
            name: 'ВТ'
        },
        {
            id: 1,
            name: 'ИС'
        },
        {
            id: 2,
            name: 'ИВК'
        },
    ],
})
export const actions = {
  setDepartments({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios.get('api/v1/departments/').then(res => {
        commit('setDepartments', res.data.data.results)
        resolve(res.data.data.results)
      }).catch((err) => {
        reject('Ошибка получения направлений')
      })
    })
  }
}

export const mutations = {
  setDepartments(state, departments) {
    state.departments = departments
  }
}

export const getters = {
    getDepartments: s => s.departments
}
