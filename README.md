Этот проект — REST API сервис, реализованный в качестве вступительного испытания
в школу бэкенд-разработки Яндекса.


# Установка

Чтобы установить проект, выполните следующие действия:
1. Создайте папку, в которую вы клонируете проект;
2. Перейдите в папку и клонируйте проект командой ```git clone https://github.com/vpershukov/backend_school_assignment.git```;
3. Установите зависимости, описанные ниже.


# Зависимости

```python3
Package     Version

Flask       1.1.1
mongo       0.2.0
pymongo     3.8.0
numpy       1.17.0
pytest      2.9.1
requests    2.22.0
```


# Запуск

Чтобы запустить проект, перейдите в созданную вами папку и отправте команду ```python3 app.py```.


# Тестирование

Для запуска автотестов выполните следующие действия:
1. После запуска кода откройте новую вкладку в консоли и перейдите в папку проекта;
2. Запустите автотесты командой ```py.test``` (или ```py.test -v``` для большей наглядности).

Результаты тестирования:
1. Если результатом будет сообщение вида ```38 passed in 0.45 seconds``` — тесты пройдены;
2. Если не все тесты завершатся успехом, появится сообщение вида ```1 failed, 37 passed in 0.52 seconds```.
