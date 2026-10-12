import requests
import time

def get_pokemon_list(limit=20):
    
    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset=0'
    all_results = []

    while url:
        print(f'Загружается страница: {url}')
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        all_results.extend(data['results'])
        url = data['next']

        time.sleep(0.1)

    print(f'Всего покемонов в списке: {len(all_results)}')
    return all_results


def get_pokemon_details(url):
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'base_experience': data['base_experience'],
        'types': [t['type']['name'] for t in data['types']],
    }

def extract_all_pokemons():
    pokemon_list = get_pokemon_list(20)

    pokemons = []
    for i, item in enumerate(pokemon_list, start=1):
        details = get_pokemon_details(item['url'])
        pokemons.append(details)

        if i % 50 == 0:
            print(f'Обработано: {i} / {len(pokemon_list)}')

    return pokemons

extract_all_pokemons()
