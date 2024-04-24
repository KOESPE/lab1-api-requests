import time

import requests as r
import os


BASE_URL = 'https://ftapi.pythonanywhere.com/translate'

HEADER = """Онлайн переводчик на Python (англ\рус) c TTS

Выберите язык ввода (введите цифру):
1. Русский язык
2. Английский язык"""


def main():
    print(HEADER)

    source_language = 'ru' if int(input('Выбор: ')) == 1 else 'en'
    destination_language = 'ru' if source_language == 'en' else 'en'

    destination_text = input('Введите текст для перевода: ')

    resp = r.get(url=BASE_URL,
                 params={
                     'sl': source_language,
                     'dl': destination_language,
                     'text': destination_text
                 })
    if resp.status_code == 200:
        resp_data = resp.json()
        print(f'Перевод: {resp_data["destination-text"]}')

        filename = 'tts.mp3'
        response = r.get(resp_data['pronunciation']['destination-text-audio'])
        with open(filename, 'wb') as f:
            f.write(response.content)
        os.startfile(filename)

        time.sleep(2)
        os.remove(filename)
    else:
        print('Не удалось выполнить запрос.')


if __name__ == '__main__':
    main()
