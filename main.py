import requests
from pprint import pprint

class Superhero:
    '''
    класс героя
    '''
    base_url = 'https://akabab.github.io/superhero-api/api/'

    def get_all_superhero(self):
        uri = '/all.json'
        request_url = self.base_url + uri
        response = requests.get(request_url)
        return response.json()

    def get_id_superhero(self, id):
        uri = '/id/' + str(id) + '.json'
        request_url = self.base_url + uri
        response = requests.get(request_url)
        return response.json()

    def get_powerstars_superhero(self, id):
        uri = '/powerstars/' + str(id) + '.json'
        request_url = self.base_url + uri
        response = requests.get(request_url)
        return response.json()

    def get_appearance_superhero(self, id):
        uri = '/appearance/' + str(id) + '.json'
        request_url = self.base_url + uri
        response = requests.get(request_url).json()
        return response.json()

    def get_biography_superhero(self, id):
        uri = '/biography/' + str(id) + '.json'
        request_url = self.base_url + uri
        response = requests.get(request_url)
        return response.json()


compare_heroes = ['Halk', 'Capitan America', 'Thanos']
# compare_heroes = ['A-Bomb', 'Abe Sapien', 'Abin Sur'] # alternative heroes

if __name__ == '__main__':
    hero = Superhero()
    info_heroes = hero.get_all_superhero()
    ids_heroes = {}
    for info in info_heroes:
        if info['name'] in compare_heroes:
            ids_heroes[info['name']] = info['powerstats']['intelligence']

    max = 0
    for name in ids_heroes.keys():
        if ids_heroes[name] > max:
            Name = name
            max = ids_heroes[name]

    pprint(Name)
