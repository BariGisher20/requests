from pprint import pprint
import requests


def response_get():
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    heroes_name = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
    for hero in heroes_name:
        response = requests.get(url=url + hero['name'])
        hero['intelligence'] = int(response.json()['results'][0]['powerstats']['intelligence'])
    a = max(heroes_name, key=lambda hero: hero['intelligence'])['name']
    return a


if __name__ == '__main__':
    pprint(response_get())