# Rest-API Django
Технологии: Python, Django, GitHub Actions

#### 1) Делаем REST API CRUD  с использованием библиотеки rest framework

   Приложение должно реализовать API:
      
    GET /persons/{personId} – информация о человеке;
    GET /persons – информация по всем людям;
    POST /person – создание новой записи о человеке;
    PATCH /person/{personId} – обновление существующей записи о человеке;
    DELETE /person/{personId} – удаление записи о человеке.

###### Подробнее: <https://rsoi-person-service.herokuapp.com/swagger-ui.html>
#### 2) Делаем небольшую страничку CRUD.
#### 3) Написание 5-и unit-тестов на реализованные функции
#### 4) Для проведения тестов и деплоя используется GitHub Actions
## Подробнее
##### API
1) Запросы/ответы в в формате JSON
2) Если запись по id не найдена, тогда возвращается HTTP статус 404 Not Found
3) При создании новой записи о человека (метод POST /person) возвращается HTTP статус 201 Created с пустым телом и Header "Location: https://rsoi-person-service.herokuapp.com/person/{personId}", где personId – id созданной записи.
##### GitHub Actions
1) Деплой на Heroku
2) Полная автоматизация процесса тестирования и деплоя 

