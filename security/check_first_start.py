import requests
import json


def first_start(url):
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.text
        print(response_json)

first_start('https://xchess.webnet.kz/check-code?code=thisIsCode')
