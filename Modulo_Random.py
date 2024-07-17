"""
Módulo Ramdom

- Em Python, módulos nada mais são do que outros arquivos Python.

MOdulo Random -> Possui várias funções para geração de números pseudo-aleatório.

#Obs: Existem duas formas de se utilizar um módulo ou função deste

#Forma 1


# random() -> Gera um número pseudo-aleatório entre 0 e 1

#OBS: Ao realizar o import de todo o módulo, todas funções, atributos, classes e propriedades que estiverem
#Dentro do módulo ficarão disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma idela de utilazação. Nós veremos uma forma melhor na Forma 2.

print(random.random())
# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da fução,
# separados por ponto

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# aprenas uma função dentro do módulo random

# Forma 2 - importando uma função específica do módulo
from random import random

#No módulo acima, estamos falando: Do Módulo random, importe a função random

for i in range(10):
    print(random())

# Uniform() -> Gerar um número pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(0, 10)) #7 não é incluido
    
# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint
#Gerador de apostas para a mega-sena

for i in range(6):
    print(randint(1,61), end=', ')    

# choice() -> Mostra um valor aleatório entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
"""
# shuffle() -> Tem a função de embaralhar dados

from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5' ,'6', '7']

shuffle(cartas)

print(cartas)