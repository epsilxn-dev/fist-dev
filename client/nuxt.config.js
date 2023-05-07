
export default {
    ssr: true,
    head: {
        script: [{
            src: 'https://vk.com/js/api/openapi.js?169',
            type: 'text/javascript',
            defer: true
        }],
        title: 'ФИСТ',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
        ]
    },

    css: [
        '~/assets/styles/main.scss',
        "~/node_modules/vue-wysiwyg/dist/vueWysiwyg.css",
        '~/node_modules/sweetalert2/dist/sweetalert2.min.css'
    ],

    plugins: [
        '~/plugins/wysiwyg.js',
        '~/plugins/nuxtClientInit.client.js',
        '~/plugins/directives.js',
        '~/plugins/showMsg.js',
        "~/plugins/toFormData.js"
    ],

    components: true,

    buildModules: [
        '@nuxtjs/vuetify',
    ],

    modules: [
        ['vue-scrollto/nuxt', {
            duration: 1000,
            easing: 'easy-in-out'
        }],
        ['cookie-universal-nuxt', { alias: 'cookiz' }],
        '@nuxtjs/axios',
        'vue-sweetalert2/nuxt',

    ],
    
    pwa: { icon: { source: '~/static/favicon.ico' } },
    axios: {
        baseURL: process.env.NUXT_ENV_BASE_URL || "http://127.0.0.1:8000/",
    },
    sweetalert: {
        confirmButtonColor: '#41b882',
        cancelButtonColor: '#ff7674'
    },

    build: {}
}