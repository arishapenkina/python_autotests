import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6888f3ee36b0bcc9516e6971c64c176d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body = {
    "pokemon_id": "121200",
    "name": "mimimamomuuu",
    "photo_id": 3
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)
print (response.json())
'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body)
print (response.json())
'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body)
print (response.json())