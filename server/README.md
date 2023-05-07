Сервер ФИСТ
---
### Навигация
* [Документация по фреймворкам и библиотекам](#framedocs)
* [Полезные ссылки](#links)
* [Структура проекта](#project-structure)
  * [ViewSet поля/аттрибуты](#project-viewset-fields)
  * [Система идентификации](#identifier)
---
### Документация по фреймворкам и библиотекам <a name="framedocs"></a>
* [Django](https://docs.djangoproject.com/en/4.0/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Django filters](https://django-filter.readthedocs.io/en/stable/guide/usage.html)
* [Django SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
---
### Полезные ссылки <a name="links"></a>
* [JWT Encoder/Decoder](https://jwt.io/)
* [Sourcetree](https://www.sourcetreeapp.com/ "Программа для работы с VCS(git)")
---
### Структура проекта <a name="project-structure"></a>
#### CBV поля/аттрибуты <a name="project-viewset-fields"></a>
> В проекте предпочтительнее всего использовать классы (даже если логика заключается в использовании 1 функции на create или подобное).
> Это связано с тем, что многие поля, которые существуют в drf+filters, оптимизированы именно под классы. Также, в конфигураторе написан класс для swagger (поле swagger_tags=[""] ниже)
* `queryset` - поле с информацией из бд
  * **Пример**: `queryset = Course.objects.filter(is_deleted=False)`
* `serializer_class` - поле с сериализатором, который будет использоваться по умолчанию
  * **Пример**: `serializer_class = CourseSerializer`
* `authentication_classes` - класс, который будет в `request.user` и `request.auth` класть информацию (опознавать юзера)
  * **Почти во всех случаях**: `authentication_classes = [AuthenticationSystem]`
  * Если поле `authentication_classes = []`, то к ресурсу может получить доступ любой человек (если не стоят проверки уровня `request.user.id = ...`)
* `swagger_tags` - не обязательное поле, которое нужно для группировки методов в Swagger (127.0.0.1/swagger)
  * **Пример**: `swagger_tags = ["Course"]`
* `filterset_fields` - поля, по которым будет идти фильтрация
  * **Пример:** `filterset_fields = ["name", "rst"]`
* `search_fields` - поля, по которым будет выполнен поиск
  * Поведение поиска можно контролировать
    * ^ - starts-with search
    * = - exact matches
    * @ - full-text search
    * $ - regex search
  * **Пример:** `search_fields = ["name", "=rst"]`
    * При `?q=asd` поиск будет выполнен по правилу exact match (полное совпадение в поле name или rst)
* `ordering_fields` - поля, по которым будет сортироваться выдача
  * **Пример:** `ordering_fields = ["-id", "price", "name"]`
#### Система идентификации <a name="identifier"></a>
> В системе используется собственная система аутентификации (в плане логики) jwt, основанная на библиотеке simplejwt.
* Регистрация
  * Пользователь вводит email, password, login, отправляет на сервер и получает ответ
* Авторизация
  * Пользователь вводит login и password
  * Пользователь получает HttpOnly cookie в которой хранится refresh token, а также получается отдельно access token
    * Access token - короткоживущий токен, который можно использовать неограниченное количество раз, пока срок действия не подошёл к концу
    * Refresh token - долгоживущий токен, нужен для замены пары access и refresh токенов
* Аутентификация
  * Пользователь делает любой запрос и отправляет вместе с ним в заголовке Authorization свой access токен
    * Если токен подошёл к концу (в плане expire time), то выдаст 40х ошибку
    * Если токен действителен и не соотносится с текущим токеном клиента (токен был украден), то тоже выдаст ошибку
    * Если токен действителен и совпадает с токеном, записанным в бд, то вернётся положительный ответ
