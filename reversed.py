"""
Reversed

Obs: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável

Sua função é inverter o iterável

A função reversed() retorna um iterável chamado List Reverse Iterator
"""
#Exemplos

listas = [1, 2, 3, 4, 5]

res = reversed(listas)

print(res)
print(type(res))

#Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

#Lista 
print(list(reversed(listas)))

#Tupla
print(tuple(reversed(listas)))

#OBS: Em conjuntos não definimos a ordem dos elementos
#Conjunto (Set) 
print(set(reversed(listas)))
#Podemos iterar sobre o reversed
for letra in reversed('Raphael Seidi'):
    print(letra, end='')

#Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Raphael Seidi'))))

#Já vimos como fazer isso mais facil com o slice de stringes
print('Raphael Seidi'[::-1])

#Podemos também utilizar o reversed() para fazer um loop reverso
for n in reversed(range(0, 10)):
    print(n)

#Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)