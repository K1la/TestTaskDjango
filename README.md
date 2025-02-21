# Установите виртуальное окружение в проекте

python -m venv venv

venv\Scripts\activate

# Установка зависимостей

pip install django==4.2.19 djangorestframework==3.15.2 django-filter

# Настройка IDE

Перейдите в IDE в папку ~/TestTaskDjango/app

Выберите интерпретатор в своем IDE по пути ~/TestTaskDjango/.venv/Scripts/python.exe

# Запуск программы:

python manage.py runserver

# Использование:

GET: ~/api/task/ - получить список всех задач

GET: ~/api/task/id/ - получить конкретную задачу по id

DELETE: ~/api/task/id/ - удалить выбранную задачу

POST: ~/api/task/ - создать новую задачу (снизу будут поля)

PUT: ~/api/task/id/ - редактировать выбранную задачу по id (снизу будут поля)

GET: ~/api/task/?status=pending - фильтрация по статусам задач (фильтрация по pending)


Список статусов: 

pending, in_progress, completed