import requests
from pprint import pprint   # Transformar o arquivo JSON em uma árvore facilitando a leitura 

API_Key = '595d39bc8c5681fba199b98966a1da1d'

city = input("Enter a city: ")
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&lang=pt_br" # Resposta da API com os dados
weather_data = requests.get(base_url).json()    # Transforma a resposta em um formato JSON
temp = weather_data['main']['temp'] - 273.15

print(f'{temp:.2f} °C')
