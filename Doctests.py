"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python


def soma(a, b):
    '''somam os números a e b
    
    >>> soma(1, 2)
    3 

    >> soma(4, 6)
    10
    '''
    
    return a + b


Para rodar um test do doctest

python -m doctest -v nome_do_modulo.py

#Saída

1 items had no tests:
    Doctests
0 tests in 1 items.
0 passed and 0 failed.
Test passed.

def duplicar(valores):
    '''duplica os valores em uma lista
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplica(['a' , 'b', 'c'])
    ['aa', 'bb', 'cc']
    
    >>> duplicar([True, None])
    Traceback (most recenta call last):
    
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    '''
    return [2 * elemento for elemento in valores]

    Obs: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples
"""

