"""
Trabalhando com Módulos Built-in (Módulos integradosm que já vem instalados no Python)
________________________
|Python|Módulos builtin|
------------------------

#Utilizando alias (apelidos) para módulos/funções
import random as rdm


print(rdm.random())

#POdemos importar todas as funções de um módulo utilizando o *
from random import *

print(random())

#Importando todo o módulo

import random

print(random.random())

#utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

#utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))
"""
#Costumamos utilzar tuple ppara colocar multiplos imports de um emsmo módulo

from random import(
    random,
    randint,
    shuffle,
    choice
)

