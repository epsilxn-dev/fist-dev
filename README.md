ФИСТ
---
### Навигация
* [Стек технологий]()
* [Запуск проекта]()
  * [Back-end]()
  * [Front-end]()
* [Документация]()
* [Работа в системе / Контрибьютинг]()
---
### Стек технологий
* Front-end
  * ![JavaScript](https://img.shields.io/badge/JavaScript-000000?style=for-the-badge&logo=JavaScript&logoColor=#F7DF1E)
  * ![Vue](https://img.shields.io/badge/Vue-000000?style=for-the-badge&logo=Vue.js&logoColor=#61DAFB)
  * ![Vuetify](https://img.shields.io/badge/Vuetify-000000?style=for-the-badge&logo=Vuetify&logoColor=#61DAFB)
* Back-end
  * ![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=Python&logoColor=#3776AB)
  * ![Django](https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=Django&logoColor=#009688)
* Базы данных
  * ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-000000?style=for-the-badge&logo=PostgreSQL&logoColor=#4169E1)
* Автоматизация
  * ![Docker](https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=Docker&logoColor=#2496ED)
---
### Запуск проекта
> При ручной настройке проекта (не через docker) **необходимо** править Dockerfile/docker-compose таким образом, чтобы ваш проект мог запускаться через docker/docker-compose
#### Back-end
1. Установите [python v3.10+](https://www.python.org/downloads/)
   * **НЕОБХОДИМО** добавить python в переменную Path
2. Установите [postgresql v13+](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
    * **НЕОБХОДИМО** добавить postgresql в переменную Path
3. Установите зависимости
```
pip install -r requirements.txt
```
4. Создайте БД в postgresql
5. Создайте .env файл в корне проекта (на одном уровне с client, server, docker-compose.yml) со следующим содержимым
```dotenv
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""
DJANGO_SECRET="123456qwezxc"
DJANGO_SUPERUSER_USERNAME="root"
DJANGO_SUPERUSER_PASSWORD="1234"
DJANGO_SUPERUSER_EMAIL="qwe@qwe.qwe"
NORTH_VALLEY_SHEET_NAME="API Table"
EMAIL_HOST="smtp.yandex.ru"
EMAIL_PORT=465
EMAIL_HOST_USER="" #Создаём тестовую почту яндекс
EMAIL_HOST_PASSWORD="" #Создаём тестовую почту яндекс
NUXT_ENV_BASE_URL=""
MODE=""
ALLOWED_HOSTS="" # отделяется ; каждый новый хост
HOSTING_HOST=""
HOSTING_PROTOCOL=""
```
6. Подготовьте и примените миграции
```
python manage.py makemigrations
```
```
python manage.py migrate
```
7. Создайте суперюзера
```
python manage.py createsuperuser
```
8. Запустите проект
```
python manage.py runserver
```
9. *Для теста курсов северной долины необходимо также добавить [service_account.json](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) в директорию server, которая лежит на уровне с client
#### Front-end
* Установите node.js версии 16.8.0-16.14.2 (любую из них)
* В директории client установите все пакеты
```
npm i
```
* Запустите проект
```
npm run dev
```
---
### Документация
* [Back-end](https://github.com/ulstu/fist-portal/blob/main/server/README.md)
* [Front-end](https://github.com/ulstu/fist-portal/blob/main/client/README.md)
### Работа в системе / Контрибьютинг
> Если необходимо внести какие-то изменения, добавить фичи и так далее, то необходимо перейти в ветку dev, от неё создать ветку со своим псевдонимом и через "/" указать модуль или фичу, которую реализуете
1. Переключаемся на (и вместе с этим создаём от ветки dev) ветку rst-news (название ветки является примером)
```git
git checkout -b rst/news dev
```
2. Вносим какие-то изменения, создаём файлы, удаляем файлы
3. Добавляем файлы в индекс
```git
git add *
```
4. Коммитим (возможно, пушим в свою ветку)
```git
git commit -m "Commit"
```
5. Повторяем шаги 2-4, пока не будет закончена работа
6. Переключаемся на ветку dev, с ранее созданной вашей ветки
```git
git checkout dev
```
7. Сливаем ветку "branch_name" в dev
```git
git merge --no-ff branch_name
```
8. Удаляем ветку (ветку dev даже после мерджей не удаляем)
```git
git branch -d branch_name
```
9. Пушим изменения на сервер
```git
git push origin dev
```

