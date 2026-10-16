# PokeAPI ETL Pipeline

ETL-пайплайн для загрузки данных о покемонах из PokeAPI (https://pokeapi.co) в PostgreSQL.

## Что делает

1. **Extract** - обходит все страницы PokeAPI (1351 покемон), забирает детали по каждому.
2. **Load** - загружает данные в PostgreSQL батчами (`executemany`) с идемпотентным upsert (`ON CONFLICT DO UPDATE`).
3. **Analytics** — набор SQL-запросов для аналитики: агрегации, оконные функции, работа с массивами.

