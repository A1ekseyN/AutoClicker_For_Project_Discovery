import requests
import json

# Ваши данные авторизации и параметры
client_id = '226bbcdddec8450f826913efc3bf857f'
secret_key = 'IAc2oOYmmu2GfWrO19DobZ6Jku0Il9P8REN1IvWi'
callback_url = 'http://localhost:8000/callback'
scopes = 'esi-search.search_structures.v1'

# Базовый URL для ESI API
esi_base_url = 'https://esi.evetech.net/latest'

# ID персонажа EVE Online
character_id = 2117970187  # Замените на ваш ID персонажа

# Определим переменную systems только для Jita (30000142)
systems = {
    'Jita': 30000142
}


# Функция для аутентификации и получения токена
def authenticate(client_id, secret_key, callback_url, scopes):
    auth_url = 'https://login.eveonline.com/oauth/authorize'
    token_url = 'https://login.eveonline.com/oauth/token'
    token_file = 'eve_access_token.json'

    def save_token(token):
        with open(token_file, 'w') as f:
            json.dump(token, f)

    def load_token():
        try:
            with open(token_file, 'r') as f:
                token = json.load(f)
                return token
        except FileNotFoundError:
            return None

    token = load_token()
    if token:
        return token['access_token']
    else:
        print(
            f'Перейдите по следующей ссылке и авторизуйтесь: {auth_url}?response_type=code&redirect_uri={callback_url}&client_id={client_id}&scope={scopes}')
        authorization_code = input('Введите код авторизации: ')

        response = requests.post(token_url, data={
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': callback_url,
        }, auth=(client_id, secret_key))

        response_data = response.json()
        access_token = response_data['access_token']
        save_token(response_data)
        return access_token


def search_entities_in_system(access_token, character_id, system_id, search_string):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'categories': ['solar_system'],
        'search': search_string,
        'datasource': 'tranquility'
    }
    response = requests.get(f'{esi_base_url}/characters/{character_id}/search/', headers=headers, params=params)
    print(f"response: {response}")
    if response.status_code == 200:
        results = response.json()
        solar_systems = results.get('solar_system', [])
        if system_id in solar_systems:
            print(f"Найдена информация о системе {system_id} по запросу '{search_string}'")
        else:
            print(f"Система {system_id} не содержит информации по запросу '{search_string}'")
    else:
        print(f"Ошибка при выполнении поиска: {response.status_code}")


def main():
    access_token = authenticate(client_id, secret_key, callback_url, scopes)

    for system_name, system_id in systems.items():
        print(f"Ищем данные в системе: {system_name} (ID: {system_id})")
        search_string = 'аномалия'  # Замените на ваш поисковый запрос
        search_entities_in_system(access_token, character_id, system_id, search_string)


if __name__ == '__main__':
    main()
