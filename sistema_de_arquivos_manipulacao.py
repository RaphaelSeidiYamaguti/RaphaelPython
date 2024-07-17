"""
Sistema de Arquivos - Manipulação

#Descobrindo se um arquivo ou diretório existe

print(os.path.exists('arquivo.txt')) #False
print(os.path.exists('frutas.txt')) #True

#Diretório

#Paths relativos
print(os.path.exists('geek')) #True
print(os.path.exists('geek/univetsity'))#True
print(os.path.exists('outro')) #False

#Paths absolutos

print(os.path.exists('/home/geek/univetsity'))#True
print(os.path.exists('/home/geek/Imagens'))#True

#Criando Arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

#Forma 2
open('arquivo-teste2.txt', 'a').close()

#Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass
    

os.mknod('arquivo-teste4.txt')

os.mknod('/home/geek/university.txt')

#Criando Arquivos

os.mknod('arquivo-teste4.txt')

os.mknod('/home/geek/university.txt')

# Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError

#Obs: Se criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

os.mkdir('templates')

#Obs: A gunção mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

# OBS: Se não tivermos permissão para criar um diretório teremos um PermissionError
"""
import os



