# tests_yandex
Запуск UI тестов c генерацией отчетов:  
pytest -v ui_yandex/tests/ --alluredir=results
* тест с загрузкой файла выполняется только локально (нужна смена абсолютного пути к файлу для загрузки)

Запуск отчета после прогона тестов:  
allure serve results

Запуск API тестов с генерацией отчетов:  
pytest -v api_yandex/tests/ --alluredir=results_api

Запуск отчета после прогона тестов:  
allure serve results_api