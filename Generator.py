"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension:
-Dictionary Comprehension:
-Set Comprehension:

Não Vismos
-Tuple Comprehensiom.... porque elas se chamam Generetors

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristana', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

#Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristana', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

#List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

#Qual a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória de elemento passado como parâmetro
from sys import getsizeof 

#Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto Maior a string, mais espaço ocupa
print(getsizeof('Geek'))
"""
from sys import getsizeof

#Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

#Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

#Gerando uma lista de números com Generator
gen_comp = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension {list_comp}')
print(f'Set Comprehension {set_comp}')
print(f'Dictionary Comprehension {dic_comp}')
print(f'Generator {gen_comp}')