"""
Função de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma Linguagem de Programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funçoes 
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
no nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen

#Exemplos - Definindo as Funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

#Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

#Nested Functions - Funções Alinhadas

'''
Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Intertas)
'''

#Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

#Testando

print(cumprimento('Angelica'))

print(cumprimento('Felicity'))

#Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahaha ', 'kkkkkkkkkkkkkk', 'yayayayayaya '))
    return rir

#Teste
rindo = faz_me_rir()
print(rindo())
"""

#Inner Functions(Funções Internas/ Nested Fucntions) podem acessar o escopo de funções mais externas

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahaha ', 'kkkkkkkkkkkkkk ', 'yayayayayayaya '))
        return f'{risada} {pessoa}'
    return dando_risada

#Testando

rindo = faz_me_rir_novamente('Fernanda')


print(rindo())
print(rindo())
print(rindo())


