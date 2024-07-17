"""
O bloco With


Passos para se trabalhar com arquivos

#1 - Abrimos o arquivo
#2 - Manipulamos o arquivo
#3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechado após o bloco with

arquivo = open('texto.txt')

"""

# O bloco with - Foma Pythônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


print(arquivo.closed)