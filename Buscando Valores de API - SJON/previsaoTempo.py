
import requests

clima = requests.get('http://api.tempo.com/index.php?api_lang=br&localidad=12996&affiliate_id=tk99un15usak&v=3.0')
print(clima.json())
