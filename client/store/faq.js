export const state = () => ({
    questions: [{
            theme: 'стипухи',
            question: 'Почему мы такие молодцы',
            answer: 'Потому что делаем много',
            tags: [
                { name: "default" },
                { name: 'second' }
            ]
        },
        {
            theme: 'Ёжики',
            question: 'И причём тут ёжики?',
            answer: 'Морковь',
            tags: [
                { name: "default" },
                { name: 'second' }
            ]
        },
        {
            theme: 'Ёжики',
            question: 'И зачем тут ёжики?',
            answer: 'Морковь',
            tags: [
                { name: "default" },
                { name: 'second' }
            ]

        },
        {
            theme: 'Поступление',
            question: 'А как поступать?',
            answer: 'Через круги бюрократического ада',
            tags: [
                "default",
                'second'
            ]
        },
        {
            theme: 'Поступление',
            question: 'А зачем поступать?',
            answer: 'пока сам не понял',
            tags: [
                "default",
                'second'
            ]
        }
    ]
})

export const actions = {
    setQuestions({ commit }) {
        return new Promise((resolve, reject) => {
            this.$axios.get('api/v1/questions').then(res => {
                commit('setQuestions', res.data.data.results)
                resolve(res.data.data.results)
            }).catch((err) => {
                reject('Ошибка получения вопросов', err)
            })
        })
    }
}

export const mutations = {
    setQuestions(state, questions) {
        state.questions = questions
    }
}

export const getters = {
    getQuestions: s => s.questions
}