import requests
from pprint import pprint   # Transformar o arquivo JSON em uma árvore facilitando a leitura 

API_Key = '595d39bc8c5681fba199b98966a1da1d'

city = input("Enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city   # Resposta da API com os dados
weather_data = requests.get(base_url).json()    # Transforma a resposta em um formato JSON

pprint(weather_data)
