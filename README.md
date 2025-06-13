# Blog

## О проекте

Это **бэкенд часть** простого блога, написанная на FastAPI с использованием асинхронного SQLAlchemy и SQLite.
В проекте реализованы базовые CRUD операции для пользователей, постов и комментариев.

---

## Установка и запуск (Linux)

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/KnightParzivalll/OOP-project-blog.git
   cd OOP-project-blog
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Запустите сервер разработки:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Откройте в браузере:
   [http://127.0.0.1:8000](http://127.0.0.1:8000) — главная страница сразу перенаправляет на документацию API (`/docs`).
