<template>
    <v-stepper v-model="el" vertical>
        <v-stepper-step :complete="el > 1" step="1">
            Сдайте ЕГЭ
            <small>на необходимые баллы</small>
        </v-stepper-step>
        <v-stepper-content step="1">
            <div class="mb-5">
                <div class="text-center">
                    В обязательном порядке необходимо сдать ЕГЭ по
                    <b>Русскому языку</b>, <b>Математике (профиль)</b> и на
                    выбор Информатика/Физика/Химия
                </div>
                <div class="text-center d-flex align-start justify-center">
                    <div>
                        <v-divider class="mt-2" />
                        <p class="mt-2">
                            Изчучить проходные баллы прошлого года можно по
                            <a
                                href="https://vk.com/away.php?to=https%3A%2F%2Fulstu.ru%2Fabitur%2Fbak-spec-mag%2Fdocuments%2Fedd%2Fbak_zach.pdf&cc_key="
                                >ссылке</a
                            >
                        </p>
                    </div>
                </div>
            </div>
            <v-btn color="primary" @click="el = 2"> Далее </v-btn>
        </v-stepper-content>

        <v-stepper-step :complete="el > 2" step="2">
            Отнесите документы
            <small>по данному адресу</small>
        </v-stepper-step>

        <v-stepper-content step="2">
            <iframe
                src="https://yandex.ru/map-widget/v1/?um=constructor%3A6f69539c6db460c9c76d48546f37624cbb6d818e11fc4c40ff939e4fd671d4df&amp;source=constructor"
                width="100%"
                height="400"
                frameborder="0"
            ></iframe>
            <v-btn color="primary" @click="el = 3"> Далее </v-btn>
        </v-stepper-content>

        <v-stepper-step :complete="el > 3" step="3">
            Следите за списками
        </v-stepper-step>

        <v-stepper-content step="3">
            <div class="mb-5">
                <div class="text-center flex-md-row d-flex justify-center">
                    Наблюдайте за своей кандидатурой в списке на сайте
                    <a class="ml-2" href="https://ulstu.ru/"> УлГТУ</a>
                </div>
                <v-divider class="mt-4" />
            </div>
            <v-btn color="primary" @click="el = 1"> Сначала </v-btn>
        </v-stepper-content>
    </v-stepper>
</template>

<script>
export default {
    data() {
        return {
            el: 1,
        };
    },
};
</script>
