export const globalMenu = [
    //Список иконок можно найти на сайте https://materialdesignicons.com/
    {
        ico: "mdi-home",
        title: "Главная",
        to: "/"
    },
    {
        ico: "mdi-newspaper-variant",
        title: "Новости",
        to: "/news"
    },
    {
        ico: "mdi-account",
        title: "Абитуриентам",
        submenu: [
            {
                ico: "mdi-ballot",
                title: "Направления",
                to: "/#directions"
            },
            {
                ico: "mdi-archive",
                title: "Правила приёма",
                to: "/abiturients#rules"
            },
            {
                ico: "mdi-monitor-star",
                title: "Компьютерная школа",
                to: "/computer_school"
            },
            {
                ico: "mdi-file-document-multiple",
                title: "Подача документов",
                href: "http://pk.ulstu.ru/index.php?nav=rules2021"
            },
            {
                ico: "mdi-file-sign",
                title: "Проходные баллы",
                href: "http://pk.ulstu.ru/Documents/2020/PB.pdf"
            },
           
        ]
    },
    {
        ico: "mdi-account-tie",
        title: "Студентам",
        submenu: [
            {
                ico: "mdi-flask",
                title: "Лаборатории",
                to: "/labs"
            },
            {
                ico: "mdi-lightbulb-variant",
                title: "Идеи",
                to: "/ideas"
            },
            {
                ico: "mdi-file-document-multiple",
                title: "Проекты",
                to: "/projects"
            }
        ]
    },
    {
        ico: "mdi-layers",
        title: "Курсы",
        submenu: [
            {
                ico: "mdi-stairs-up",
                title: "Проф. переподготовка",
                to: "/northvalley"
            },
            {
                ico: "mdi-monitor-star",
                title: "Компьютерная школа",
                to: "/computer_school"
            },
            {
                ico: "mdi-account-arrow-up",
                title: "Курсы Simbirsoft",
                href: "https://vk.com/it.place_simbirsoft"
            },
            {
                ico: "mdi-domain",
                title: "Курсы Mediasoft",
                href: "https://academy.mediasoft.team/"
            },
            {
                ico: "mdi-translate-variant",
                title: "Иностранный язык",
                href: "http://ling.ulstu.ru/linguistics/students/professional-interpreter/"
            }
        ]
    },
    {
        ico: "mdi-message-question",
        title: "FAQ",
        to: "/faq"
    },
    {
        ico: "mdi-layers",
        title: "Люди",
        submenu: [
            {
                ico: "mdi-human-male-board-poll",
                title: "Преподаватели",
                to: "/teachers"
            },
            {
                ico: "mdi-human-greeting-variant",
                title: "Выпускники",
                to: "/graduates"
            }
        ]
    },
    {
        ico: "mdi-handshake",
        title: "Трудоустройство",
        submenu: [
            {
                ico: "mdi-account-cash",
                title: "Резюме",
                to: "/job"
            },
            {
                ico: "mdi-card-search",
                title: "Вакансии",
                to: "/job/vacancies"
            }
        ]
    },
    {
        ico: "mdi-information-outline",
        title: "О факультете",
        submenu: [
            {
                ico: "mdi-chair-school",
                title: "Бакалавриат",
                href: "https://ulstu.ru/education/directions-specialty/"
            },
            {
                ico: "mdi-school",
                title: "Магистратура",
                href: "https://ulstu.ru/education/directions-specialty/"
            },
            {
                ico: "mdi-human-male-board-poll",
                title: "Аспирантура",
                href: "https://old.ulstu.ru/main/view/article/16964"
            },
            {
                ico: "mdi-human-male-board",
                title: "Докторантура",
                href: "https://www.ulstu.ru/main/view/article/17620"
            },
        ]
    },
]