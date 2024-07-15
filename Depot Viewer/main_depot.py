import requests
import os
import json

# Вставьте ваш Client ID и Secret Key здесь
client_id = '226bbcdddec8450f826913efc3bf857f'
secret_key = 'IAc2oOYmmu2GfWrO19DobZ6Jku0Il9P8REN1IvWi'

# Ссылки для OAuth 2.0
auth_url = 'https://login.eveonline.com/oauth/authorize'
token_url = 'https://login.eveonline.com/oauth/token'
callback_url = 'http://localhost:8000/callback'  # URL-адрес перенаправления

# Укажите необходимые scopes
scopes = 'esi-universe.read_systems.v1 esi-universe.read_structures.v1 esi-characters.read_loyalty.v1 esi-wallet.read_character_wallet.v1'
#

# Файл для хранения токена
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

def authenticate():
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

# Базовый URL для ESI API
esi_base_url = 'https://esi.evetech.net/latest'

# Список систем с их ID
systems = {
    'Jita': 30000142,
    'Oicx': 30003838
}

def get_structures_in_system(system_id, access_token):
    """Получает информацию о системе и её структурах."""
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'datasource': 'tranquility'  # Указываем источник данных (в данном случае, tranquility)
    }
    response = requests.get(f'{esi_base_url}/universe/systems/{system_id}/', headers=headers, params=params)
    print(f"Structures in System {system_id} - Response Status Code: {response.status_code}")
    try:
        system_info = response.json()
    except json.JSONDecodeError:
        system_info = response.text  # Если JSON не удалось декодировать, выводим как текст

    print(f"Structures in System {system_id} - Response Content: {system_info}")
    if response.status_code == 200:
        # Вывод основной информации о системе
        print(f"\nИнформация о системе {system_info['name']} (ID: {system_info['system_id']})")
        print(f"Класс безопасности: {system_info['security_class']}")
        print(f"Статус безопасности: {system_info['security_status']}")
        print(f"Позиция: X={system_info['position']['x']}, Y={system_info['position']['y']}, Z={system_info['position']['z']}")

        # Вывод структур в системе, если они есть
        if 'stations' in system_info:
            print("\nСтанции:")
            for station_id in system_info['stations']:
                print(f"- ID станции: {station_id}")

        if 'stargates' in system_info:
            print("\nСтаргейты:")
            for stargate_id in system_info['stargates']:
                print(f"- ID старгейта: {stargate_id}")

        if 'planets' in system_info:
            print("\nПланеты и их луны:")
            for planet in system_info['planets']:
                planet_id = planet['planet_id']
                moons = planet.get('moons', [])
                if moons:
                    moon_ids = ', '.join(str(moon_id) for moon_id in moons)
                    print(f"- Планета ID {planet_id} с лунами: {moon_ids}")
                else:
                    print(f"- Планета ID {planet_id}")

    else:
        print(f"Ошибка при получении информации о системе: {system_info}")
        return None

def get_character_balance(access_token, character_id):
    """Получает баланс персонажа в ISK."""
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f'{esi_base_url}/characters/{character_id}/wallet/', headers=headers)
    print(f"Balance Response Status Code: {response.status_code}")
    if response.status_code == 200:
        try:
            balance_info = response.json()
            balance = int(balance_info)
            return balance
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Некорректный формат данных: {response.text}")
            return None
    else:
        print(f"Не удалось получить баланс персонажа.")
        return None

def get_character_loyalty(access_token, character_id):
    """Получает Loyalty Points персонажа."""
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f'{esi_base_url}/characters/{character_id}/loyalty/points/', headers=headers)
    print(f"\nLoyalty Points Response Status Code: {response.status_code}")
    if response.status_code == 200:
        loyalty_info = response.json()
        return loyalty_info
    return None

def main():
    access_token = authenticate()

    # Проверяем баланс персонажа
    character_id = 2117970187  # Убедитесь, что это правильный ID вашего персонажа
    character_balance = get_character_balance(access_token, character_id)
    if character_balance is not None:
        print(f"Баланс персонажа: {character_balance:,.0f} ISK")
    else:
        print("Не удалось получить баланс персонажа.")

    # Получаем Loyalty Points персонажа
    loyalty_points = get_character_loyalty(access_token, character_id)
    if loyalty_points is not None:
        for lp_info in loyalty_points:
            corporation_id = lp_info['corporation_id']
            loyalty_points_value = lp_info['loyalty_points']
            if corporation_id == 1000180:
                print(f"- State Protectorate: {loyalty_points_value:,.0f} LP")
    else:
        print("Не удалось получить Loyalty Points персонажа.")

    # Получаем информацию о структурах в каждой системе
    for system_name, system_id in systems.items():
        print(f'\nСистема: {system_name} (ID: {system_id})')
        structures = get_structures_in_system(system_id, access_token)
        if structures:
            print('Объекты в системе:')
            for structure in structures:
                # Выводим информацию о каждой структуре
                print(f"- Название: {structure.get('name', 'Unknown')}")
                print(f"  ID структуры: {structure.get('structure_id', 'Unknown')}")
                print(f"  Тип структуры: {structure.get('type_id', 'Unknown')}")
                # Пример фильтрации по типу (замените на свой тип)
                if structure.get('type_id') == 35832:  # Пример типа станции
                    print("    Это станция!")
        else:
            print('Нет объектов в системе.')

if __name__ == '__main__':
    main()
