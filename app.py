from dadata import Dadata
import db

db.create_table()
token = input('Введите API-ключ: ')
secret = input('Введите секретный ключ: ')
language = input('Введите язык(ru - русский, en - английский): ')
if language != 'ru' and language != 'en':
    language = 'ru'

db.add_record('https://dadata.ru/', token, secret, language)

with Dadata(token, secret) as dadata:
    while True:
        query = input('Введите адрес, либо exit для выхода: ')
        if query == 'exit':
            exit()

        # получаем список возможных адресов и выводим на экран
        response = dadata.suggest(name='address', query=query, language=language)
        address_list = [adr['value'] for adr in response]
        for n, adr in enumerate(address_list):
            print(f'{n + 1} - {adr}')
        try:
            # получаем ответ от пользователя
            query = int(input('Выберите один из выведенных адресов, если нет подходящих, то введите E и уточните '
                              'адрес: '))

            target = address_list[query - 1]
            res = dadata.clean(name='address', source=target)
            lat, lon = res['geo_lat'], res['geo_lon']
            print(f'Широта {lat}, долгота {lon}')
        except:
            pass
