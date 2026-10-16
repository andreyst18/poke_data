# PokeAPI ETL Pipeline

ETL-пайплайн для загрузки данных о покемонах из PokeAPI (https://pokeapi.co) в PostgreSQL.

## Что делает

1. **Extract** - обходит все страницы PokeAPI (1351 покемон), забирает детали по каждому.
2. **Load** - загружает данные в PostgreSQL батчами (`executemany`) с идемпотентным upsert (`ON CONFLICT DO UPDATE`).
3. **Analytics** — набор SQL-запросов для аналитики: агрегации, оконные функции, работа с массивами.

## Стек

- Python 3.14 (requests, psycopg3, python-dotenv)
- PostgreSQL 18
- SQL (оконные функции, CTE, unnest, CASE)
- Git, Linux (WSL)

## Как запустить

1. Клонировать репозиторий.
2. Создать venv: `python3 -m venv venv && source venv/bin/activate`
3. Установить зависимости: `pip install -r requirements.txt`
4. Создать `.env` с параметрами БД (см. `.env.example`).
5. Создать таблицу: `psql -h localhost -U andrey_data -d poke_db -f sql/01_create_tables.sql`
6. Запустить пайплайн: `python load.py`
