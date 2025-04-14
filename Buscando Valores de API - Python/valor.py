import requests

valor = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,ARS-BRL,ETH-BRL')

nomeDolar = valor.json() ['USDBRL']['name']
nomePeso = valor.json()['ARSBRL']['name']
nomeEtherum = valor.json()['ETHBRL']['name']

valorDolar = valor.json() ['USDBRL']['bid']
valorPeso = valor.json()['ARSBRL']['bid']
valorEtherum = valor.json()['ETHBRL']['bid']

print(nomeDolar,valorDolar)
print(nomePeso,valorPeso)
print(nomeEtherum,valorEtherum)