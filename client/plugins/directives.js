import Vue from 'vue'
import directives from '@/directives/index.js';

directives.forEach(d => {
    Vue.directive(d.name, d)
})