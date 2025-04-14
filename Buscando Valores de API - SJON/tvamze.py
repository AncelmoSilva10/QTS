import requests

tema = input('Qual tema deseja pesquisar? ')

tvamze = requests.get(f'https://api.tvmaze.com/search/shows?q={tema}')

print(tvamze.json())