"""
Entendendo Iterators e iterables

Iterator -> 
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable ->
    - Um objeto que irá retornar um iterador quando a função iter() for chamada.

nome = 'Geek' # É um iterable mas não é um iterator
lista = [1, 2, 3, 4, 5, 6] # É um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(lista)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
#print(next(it1)) -> Erro de StopIteraction 

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
#print(next(it2)) -> Erro de StopIteraction 
"""

nome = 'Geek'

for letra in nome:
    print(f'{letra}')