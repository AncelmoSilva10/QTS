import requests #Essa biblioteca permite realizar requisições remotas



cep =input('Digite o CEP desejado: ')

link = f"http://viacep.com.br/ws/{cep}/json/"

requisicao = requests.get(link)
dicRequisicao = requisicao.json()
print(dicRequisicao) #Um print para a gente ver o que veio de lá...



#Agora, basta separar o que queremos e transferira para variáveis

estadobuscador = dicRequisicao['uf']

logradourobuscador = dicRequisicao['logradouro']

bairrobuscador = dicRequisicao['bairro']

cidadebuscador = dicRequisicao['localidade']


#Finalmente, só imprimir !

print(estadobuscador)

print(logradourobuscador)

print(bairrobuscador)

print(cidadebuscador)
