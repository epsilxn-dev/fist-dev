export const state = () => ({
    subjects: [{
            name: 'Математика',
            balls: '54 балла'
        },
        {
            name: 'Русский язык',
            balls: '52 балла'
        },
        {
            name: 'Информатика',
            balls: '64 балла'
        },
        {
            name: 'Итог',
            balls: '200 баллов'
        }
    ],
    links: [{
            href: 'https://ulstu.ru/abitur/bak-spec-mag/',
            text: 'Приёмная комиссия'
        },
        {
            href: 'https://ulstu.ru/school/prepare-for-admission/',
            text: 'Подготовка к поступлению'
        },
        {
            href: 'http://akademia.ulstu.ru/',
            text: 'Инженерная академия'
        },
        {
            href: 'https://ulstu.ru/abitur/it-litsey/',
            text: 'IT-лицей'
        },
        {
            href: 'https://old.ulstu.ru/main/view/article/21952',
            text: 'Среднее профессиональное образование'
        },
        {
            href: 'https://old.ulstu.ru/main/view/article/17959',
            text: 'Аспирантура'
        }
    ]
})
export const getters = {
    getSubjects: s => s.subjects,
    getLinks: s => s.links
}