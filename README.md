# 👨‍💻 Онлайн-курсы 
## _HardQode test project_

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Проект представляет собой площадку для размещения онлайн-курсов с набором уроков. Доступ к урокам предоставляется после покупки курса (подписки). Внутри курса студенты автоматически распределяются по группам.

### __Установка на локальном компьютере__
1. Клонируйте репозиторий:
    ```
    git clone git@github.com:Lozhkin-pa/hardqode-test-project.git
    ```
2. Установите и активируйте виртуальное окружение:
    ```
    python -m venv venv
    venv/Scripts/activate  - для Windows
    source venv/bin/activate - для Linux
    ```
3. Установите зависимости:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Перейдите в папку product и выполните миграции:
    ```
    cd product
    python manage.py migrate
    ```
5. Создайте суперпользователя:
    ```
    python manage.py createsuperuser
    ```
6. Запустите проект:
    ```
    python manage.py runserver
    ```

### __OpenAPI документация__
* Swagger: http://127.0.0.1:8000/api/v1/swagger/
* ReDoc: http://127.0.0.1:8000/api/v1/redoc/

### __Примеры запросов__

<details><summary> GET: http://127.0.0.1:8000/api/v1/courses/  - показать список всех курсов.</summary>

    200 OK:
    ```
    [
        {
            "id": 3,
            "author": "Михаил Иванов",
            "title": "Backend developer",
            "start_date": "2024-03-03T12:00:00Z",
            "price": "15000",
            "lessons_count": 0,
            "lessons": [],
            "demand_course_percent": 0,
            "students_count": 0,
            "groups_filled_percent": 0
        },
        {
            "id": 2,
            "author": "Михаил Иванов",
            "title": "Python developer",
            "start_date": "2024-03-03T12:00:00Z",
            "price": "10000",
            "lessons_count": 3,
            "lessons": [
                {
                    "title": "Урок №1"
                },
                {
                    "title": "Урок №2"
                },
                {
                    "title": "Урок №3"
                }
            ],
            "demand_course_percent": 84,
            "students_count": 10,
            "groups_filled_percent": 83
        },
        {
            "id": 1,
            "author": "Иван Масков",
            "title": "Онлайн курс",
            "start_date": "2024-03-03T12:00:00Z",
            "price": "5000",
            "lessons_count": 3,
            "lessons": [
                {
                    "title": "Урок №1"
                },
                {
                    "title": "Урок №2"
                },
                {
                    "title": "Урок №3"
                }
            ],
            "demand_course_percent": 7,
            "students_count": 1,
            "groups_filled_percent": 10
        }
    ]
    ```
</details>

<details><summary> GET: http://127.0.0.1:8000/api/v1/courses/2/lessons/  - показать список уроков определенного курса.</summary>

    200 OK:
    ```
    [
        {
            "title": "Урок №1",
            "link": "http://www.example.com/video/",
            "course": "Python developer"
        },
        {
            "title": "Урок №2",
            "link": "http://www.example.com/video/",
            "course": "Python developer"
        },
        {
            "title": "Урок №3",
            "link": "http://www.example.com/video/",
            "course": "Python developer"
        }
    ]
    ```
</details>



### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)
* [Djoser  2.2.0](https://djoser.readthedocs.io/en/latest/getting_started.html)

### __Автор__
[Дмитрий Хубулашвили](https://github.com/DmitriyDecadenz)
