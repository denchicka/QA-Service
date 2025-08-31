# QA Service

API‑сервис «Вопрос–Ответ» на Django 5 и DRF 3.15.

---

## Функционал

| Метод    | URL                            | Описание                                 |
| -------- | ------------------------------ | ---------------------------------------- |
| `GET`    | `/api/questions/`              | Список всех вопросов                     |
| `POST`   | `/api/questions/`              | Создать новый вопрос                     |
| `GET`    | `/api/questions/{id}/`         | Получить вопрос и все его ответы         |
| `DELETE` | `/api/questions/{id}/`         | Удалить вопрос (каскадно удаляет ответы) |
| `POST`   | `/api/questions/{id}/answers/` | Добавить ответ к вопросу                 |
| `GET`    | `/api/answers/{id}/`           | Получить конкретный ответ                |
| `DELETE` | `/api/answers/{id}/`           | Удалить ответ                            |

Полная схема OpenAPI доступна по `/api/schema/`, Swagger UI — `/api/docs/`.

---

## Стек

* **Python 3.12** / Django 5.0
* **Django REST Framework 3.15**
* **PostgreSQL 16**
* **Docker / docker‑compose**
* Тесты - **pytest‑django**

---

## Быстрый старт (Docker)

```bash
# 1. Клонируем репозиторий
$ git clone https://github.com/your‑org/qa_service.git
$ cd qa_service

# 2. Запускаем сервис
$ docker compose up --build
# или в фоне
$ docker compose up -d
```

Доступы:

* API: [http://localhost:8000/api/](http://localhost:8000/api/)
* Админка: [http://localhost:8000/admin/](http://localhost:8000/admin/) 

---

## Локальная разработка (SQLite)

```bash
# создать виртуальное окружение
$ python -m venv venv && source venv/bin/activate
$ pip install -r requirements.txt

# SQLite база по умолчанию
$ python manage.py migrate
$ python manage.py runserver
```

Чтобы переключиться на PostgreSQL локально, пропишите переменные окружения.

---

## Тесты

```bash
# в контейнере
$ docker compose run --rm web pytest -q

# локально
$ pytest -q
```

---

## Создание суперпользователя

```bash
$ docker compose run --rm web python manage.py createsuperuser
```

---

## Структура проекта

```
qa_service/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── qa/                # root‑пакет Django‑проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── questions/         # основное приложение
    ├── migrations/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── tests/
```

---

## Лицензия

MIT

---

