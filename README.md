Этот проект — REST API сервис, реализованный в качестве вступительного испытания
в школу бэкенд-разработки Яндекса. Сервис сохраняет переданные ему наборы данных, позволяет их
просматривать и редактировать, а также производить анализ этих данных. Подробное техническое задание находится [здесь](https://docviewer.yandex.ru/view/522289777/?page=1&*=d3yu5DTbRdU%2BmWq676JUZ0iLDLd7InVybCI6InlhLWRpc2stcHVibGljOi8vOHhSS3l5bXZVL0VsUGJCY3k1M3V1T043VEQzSEdrRU1TbGtEN0pXRWFweVFybTNadjhwVTRNMWJHL3RDRzlMSnEvSjZicG1SeU9Kb25UM1ZvWG5EYWc9PSIsInRpdGxlIjoiVEFTSy5wZGYiLCJub2lmcmFtZSI6ZmFsc2UsInVpZCI6IjUyMjI4OTc3NyIsInRzIjoxNTY4NzIxNDk0Mzc4LCJ5dSI6IjQ3NTcxNzcxOTE1NjgyNjY1MDgifQ%3D%3D).


# Установка

Чтобы установить проект, выполните следующие действия:
1. Создайте папку, в которую вы клонируете проект;
2. Перейдите в папку и клонируйте проект командой ```git clone https://github.com/vpershukov/backend_school_assignment.git```;
3. Установите зависимости, описанные ниже.


### Зависимости

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
