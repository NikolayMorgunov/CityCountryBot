import requests
from setup import *
from time import sleep
from get_chat_id_fl import *
from last_update_fl import *
from get_updates_json_fl import *
from send_mess_fl import *


def main():
    update_id = last_update(get_updates_json(url))['update_id']
    update_id += 1
    while True:
        incomming = last_update(get_updates_json(url))
        if update_id == incomming['update_id']:
            if incomming['message']['text'] == '/start':
                send_mess(get_chat_id(incomming),
                          'Привет! Я бот, который может определить к какой стране принадлежит город. Просто отправь мне название города и я отвечу в какой стране он находится', url)
            else:
                city = incomming['message']['text']
                geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format(
                    '+'.join(city.split()))
                response_geo = requests.get(geocoder_request)
                json_response = response_geo.json()
                toponym = json_response["response"]["GeoObjectCollection"]["featureMember"]
                if toponym:
                    city_ans = toponym[0]['GeoObject']['name']
                    answer = toponym[0]['GeoObject']['description']
                    send_mess(get_chat_id(incomming), 'Город {} находится в стране {}'.format(city_ans, answer), url)
                else:
                    send_mess(get_chat_id(incomming), 'Что-то я не знаю такого города', url)

            update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()
