<template>
  <div>
    <v-simple-table>
        <thead>
            <tr>
                <th scope="col">Модуль</th>
                <th scope="col">#</th>
                <th scope="col">Наименование раздела</th>
                <th scope="col">Количество часов общее</th>
                <th scope="col">Лекции</th>
                <th scope="col">Практики</th>
                <th scope="col">Самостоятельная работа</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th class="td-white" rowspan="6" valign="center">1</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Основы цифровых технологий. Введение в профессию</td>
                <td>20</td>
                <td>6</td>
                <td>6</td>
                <td>8</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Основы веб-дизайна</td>
                <td>18</td>
                <td>6</td>
                <td>6</td>
                <td>6</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Введение в веб-разработку на HTML и CSS</td>
                <td>18</td>
                <td>4</td>
                <td>6</td>
                <td>8</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Основы графического дизайна</td>
                <td>20</td>
                <td>6</td>
                <td>6</td>
                <td>8</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td><b>Итого за модуль 1</b></td>
                <td>76</td>
                <td>22</td>
                <td>24</td>
                <td>30</td>
            </tr>
            <tr>
                <th class="td-white" rowspan="5">2</th>
            </tr>
            <tr>
                <td>5</td>
                <td>Введение в алгоритмизацию и программирование на языке C</td>
                <td>62</td>
                <td>18</td>
                <td>20</td>
                <td>24</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Основы языка программирования на языке JavaScript</td>
                <td>26</td>
                <td>8</td>
                <td>8</td>
                <td>10</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Система контроля версий git</td>
                <td>14</td>
                <td>4</td>
                <td>4</td>
                <td>6</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td><b>Итого за модуль 2</b></td>
                <td>102</td>
                <td>30</td>
                <td>32</td>
                <td>40</td>
            </tr>
            <tr>
                <th scope="row" class="td-white" rowspan="6" valign="center">3</th>
            </tr>
            <tr>
                <td>8</td>
                <td>Введение в базы данных PostgreSQL</td>
                <td>28</td>
                <td>8</td>
                <td>8</td>
                <td>12</td>
            </tr>
            <tr>
                <td>9</td>
                <td>Основы сетевых технологий и операционных систем</td>
                <td>26</td>
                <td>8</td>
                <td>8</td>
                <td>10</td>
            </tr>
            <tr>
                <td>10</td>
                <td>Введение в технологии веб-программирования с использованием NodeJS</td>
                <td>28</td>
                <td>8</td>
                <td>8</td>
                <td>12</td>
            </tr>
            <tr>
                <td>11</td>
                <td>Итоговая аттестационная работа работа</td>
                <td>40</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td><b>Итого за модуль 3</b></td>
                <td>122</td>
                <td>24</td>
                <td>24</td>
                <td>74</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td><b>Итого за весь курс</b></td>
                <td>300</td>
                <td>76</td>
                <td>80</td>
                <td>144</td>
            </tr>
        </tbody>
                    
    </v-simple-table>
  </div>
</template>

<style>
    th.td-white{
        background-color: transparent !important
    }
    tr{
        margin: 100px !important;
        
    }
    th,td{
        padding: 20px 10px !important;
    }
</style>
