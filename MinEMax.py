"""
Min e Max

max() -> Retorna o maior valor em um iterável ou maior de dois ou mais elementos.
#Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(max(dicionario.values()))

print(max(3, 34))

#Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))

print(max(val1,val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'abc','c', 'g'))

print(max(3.145, 5.784) )

print(max('Raphael Seidi Yamaguti'))

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(min(dicionario.values()))

print(min(3, 34))

#Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))

print(min(val1,val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'abc','c', 'g'))

print(min(3.145, 5.784) )

print(min('Raphael Seidi Yamaguti'))

#Outros exemplos

nomes = ['Arya', 'Samson','Dora', 'Tim', 'Ollivander']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""
musica = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(max(musica, key=lambda musicas: musicas['tocou']))
print(min(musica, key=lambda musicas: musicas['tocou']))

#Desafio
print(max(musica, key=lambda musicas: musicas['tocou'])['titulo'])
print(min(musica, key=lambda musicas: musicas['tocou'])['titulo'])
