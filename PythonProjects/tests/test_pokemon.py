import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6888f3ee36b0bcc9516e6971c64c176d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '8362'
TRAINER_NAME = 'Arisha'



def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID } )
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID , 'trainer_name' : TRAINER_NAME} )
    assert response_get.json()["data"][0]["trainer_name"] == 'Arisha'

