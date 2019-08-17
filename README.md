Этот проект — это REST API сервис, реализованный в качестве вступительного испытания
в школу бэкэнд-разработки Яндекса.

# Установка

Здесь подробная информация по тому, как запустить проект.

# Документация

Последняя версия технического задания находится здесь: (ссылка на файл).

# Примеры использования

Основние примеры находятся в описании техничекого задания. Например, первый из
них:
```python
POST http://localhost:5000/imports

{
     "citizens": [
       {
           "citizen_id": 1,
           "town": "Москва",
           "street": "Льва Толстого",
           "building": "16",
           "apartment": 1,
           "name": "Иванов Иван Иванович",
           "birth_date": "23.09.1997",
           "gender": "male",
           "relatives": [2]
       }
    ]
}
```
При успешном запросе приходит следующий ответ:
```python
HTTP 201
{
    "data": {
        "import_id": 1
    }
}
```
