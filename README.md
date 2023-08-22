# Каталог исполнителей
### Задача
Собрать с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:
- Исполнитель
    - Название
- Альбом
    - Исполнитель
    - Год выпуска
- Песня
    - Название
    - Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.
### Технологии
Python 3.10
Django 4.2
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
### Авторы
Разработал Зюзин Андрей в качестве тестового задания.
