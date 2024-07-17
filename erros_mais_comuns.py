"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso
código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que 
o Python não reconhece como parte da Linguagem.

#Exemplos SyntaxError

a)
def funcao: #Na função precisa utilizar o () no final da função
    print('Geek University')

b)#Não pode atribuir um valor para uma palavra reservada, que no caso é o NONE
None = 1

c)#Precisa ser colocada dentro de uma função
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida

#Exemplos NameError

a)
print(geek)

b)#Função que não existe
geek()

c)
a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)

3 - TypeError ocorre quand uma função/operação/ação aplicada a um tipo errado

Exemplos TypeError

a)objeto int não tem len()
print(len(5))

b) Não tem catetenar uma String e uma lista 
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um 
índice invalido

#Exemplos de IndexError:

a) Não Existe o elemento 2 na lista
lista = ['Geek']
print(lista[2])

b) #Não existe a posição 10 nessa String
lista = ['Geek']
print(lista[0][10])

c)#Mesma coisa que na lista
tupla = ('Geek')
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função/operação buint-in (integrada) recebe um argumento com tipo correto mas valor 
inapropriado

#Exemplos ValueError

a) #Não é possivel trocar esse valor para um int
print(int('Geek'))

b)#Mesma coisa que no primeiro caso
print(float('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

#Exemplos KeyError

a) #Não existe a chave com o valor no dic
dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função

#Exemplos AttributeError

a)#Não tem essa função para o tuple()
tupla = (11 , 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

#Exemplos IndentationError

a)#Não foi utilizado os 4 espaços na função
def nova():
print('Geek')

b)#Mesma ocasião do primeiro exemplo
for i in range(10):
i + 1

OBS: Exception e Errors são sinônimos na programação

OBS: Importante ler e prestar atenção na saída de erro
"""

#Exemplos IndentationError



