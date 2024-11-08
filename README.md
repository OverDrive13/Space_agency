## Тестовое задание yеобходимо сверстать с помощью bootstrap 5 и запустить новую страницу по макету

## Запуск проекта 

1. ``Клонировать репозиторий https://github.com/OverDrive13/Space_agency``
2. ``cd space_agency/``
3. ``python -m venv venv``
4. ``source venv/Scripts/activate``
5. ``pip install -r requirements.txt``
6. ``python manage.py makemigrations``
7. ``manage.py migrate``

### База Данных
В репозитории уже есть db.sqlite3

``cd space_agency``
``python manage.py runserver``
```

Проект доступен: ``localhost:8000``

***
``http://127.0.0.0:8000/`` - главная страница проекта

``http://127.0.0.1:8000/admin`` - административная панель с возможностью редактирования 

Для входа в админ панель воспользуйтесь логином admin и паролем admin
