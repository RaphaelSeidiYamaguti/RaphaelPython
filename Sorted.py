"""
Sorted

OBS: Não confunda apesar do nome, com a gunção sort() que já estudamos em listas. O sort()
só funciona em lista;

Podemos utlizar o sorted() com qualquer interavel

Como o próprio nome diz: sorted() serve para ordenar.

OBS: O sorted, sempre retorna uma Lista com os elementos do iterável ordenados

numeros = [6, 1, 8, 2]

print(numeros)

print(sorted(numeros))

#Adicionando parãmetros ao sorted()
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True)) # Ordena do Maior para o menor
"""
musica = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]
#Ordena da menos tocada para a mais tocada

print(sorted(musica, key=lambda musica: musica['tocou']))

print(sorted(musica, key=lambda musica: musica['tocou'], reverse= True))
