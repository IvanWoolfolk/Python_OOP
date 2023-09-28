import requests              # requiere  instalar modulo con : pip install requests

respuesta = requests.get("https://www.thesportsdb.com/api/v1/json/3/all_leagues.php")

print(respuesta)