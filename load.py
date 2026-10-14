import os
import psycopg
from dotenv import load_dotenv

from extract import extract_all_pokemons

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
}

def load_pokemons(pokemons):

    if not pokemons:
        print('Нет данных для загрузки.')
        return

    rows = [
        (
            p['id'],
            p['name'],
            p['height'],
            p['weight'],
            p['base_experience'],
            p['types'],
        ) 
        for p in pokemons
    ]

    sql = '''
        INSERT INTO pokemons (id, name, height, weight, base_experience, types)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            name = EXCLUDED.name,
            height = EXCLUDED.height,
            weight = EXCLUDED.weight,
            base_experience = EXCLUDED.base_experience,
            types = EXCLUDED.types,
            loaded_at = NOW();
    '''

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, rows)
            conn.commit()
            print(f'Загружено записей: {cur.rowcount}')


def main():

    print('Извлечение...')
    pokemons = extract_all_pokemons()         

    print('Загрузка...')
    load_pokemons(pokemons)

    print('Проверка...')
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as curr:
            curr.execute('SELECT COUNT(*) FROM pokemons;')
            count = curr.fetchone()[0]
            print(f'Всего строк в таблице: {count}')

if __name__ == '__main__':
    main()

    

            