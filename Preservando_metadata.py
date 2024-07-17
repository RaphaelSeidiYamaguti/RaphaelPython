"""
Preservando Metadatas com Wraps

Metadados -> São dados intrísepos em arquivos.

Wraps -> São funções que envolvem elementos com diversas finalidades.

# Problema 

def ver_log(funcao):
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra '''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    '''Soma dois números.'''
    return a + b

print(soma.__name__)
print(soma.__doc__)
"""

# Resolução Problema 

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra '''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    '''Soma dois números.'''
    return a + b

print(soma.__name__)
print(soma.__doc__)
