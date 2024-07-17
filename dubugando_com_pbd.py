"""
Debungando com PDB

PDB -> Python Debugger

BUg -> Inseto
  
#OBS: A utilização do print() para debuggar é uma pratica ruim.

def dividir(a , b):
    print(f'a= {a}, b= {b}')
    try:
         return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
         return f'Ocorreu um problema: {err}'
    
print(dividir(4, 7))

#Existem formas mais proficionais de se fazer este 'debug', utlizando o debugger
#Em Python podemos fazer isso em diferentes IDEs, com o Pycharm ou utilizando o 
#PDB - Python Debugger

#Exemplo com o PBD - Python Debugger

#Para utilizar o Python Debugger precisamos importa a biblioteca pbd entao utilizar a função set_trace()

#Comandos básicos do PDB
# l (listar onde estamos no código)
#n (próxima linha)
#p (imprime variável)
#c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelica'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)

#Exemplo com o PBD - Python Debugger - Exemplo 2

#Para utilizar o Python Debugger precisamos importa a biblioteca pbd entao utilizar a função set_trace()

#Comandos básicos do PDB
#l (listar onde estamos no código)
#n (próxima linha)
#p (imprime variável)
#c (continua a execução - finaliza o debugging)

nome = 'Angelica'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)

#Porque utilizar este formato?
#O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas
#no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo.
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção

#Exemplo com o PBD - Python Debugger - Exemplo 3

#Para utilizar o Python Debugger precisamos importa a biblioteca pbd entao utilizar a função set_trace()

# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando debug foi incorporado
# como função built-in (integrada) chamada breakpoint()

#Comandos básicos do PDB
#l (listar onde estamos no código)
#n (próxima linha)
#p (imprime variável)
#c (continua a execução - finaliza o debugging)

nome = 'Angelica'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)

#OBS: CUidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

#Como os nomes das variáveis são o mesmos dos comandos pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variável

#Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos

def soma(num1, num2, num3, num4)
    breakpoint()
    return num1 + num2+ num3 + num4
"""

