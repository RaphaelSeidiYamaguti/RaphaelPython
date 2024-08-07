"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

#Biblioteca para trabalhar com dados estatisticos
import statistics

#Dados coletados de algum sensor
dados = [1.3 , 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função mean
media = statistics.mean(dados)

#OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e interável

res = filter(lambda x: x > media, dados)
res = filter(lambda x: x < media, dados)
print(list(res))

#OBS: Assim com na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# A diferença entre map() e filter() é:

#map() -> Recebe doi parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

#filter() -> Recebe dois parâmetrosm uma função e um iterável e retorna um objeto filtrando apenas os elementos de acroco com a função

# Exemplo mais complexo

usuarios = [
    {"username" : "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username" : "carla", "tweets": ["Eu gosto de cachorros"]},
    {"username" : "raphael", "tweets": [""]},
    {"username" : "yudi", "tweets": [""]},
    {"username" : "Igor", "tweets": ["Eu adoro comer"]}    
]

#Filtrar os usuários que estão inativos no Twitter

res = list(filter(lambda tweet: len(tweet['tweets']) == 0, usuarios))
print(res)
"""
#Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

#Devemos criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)