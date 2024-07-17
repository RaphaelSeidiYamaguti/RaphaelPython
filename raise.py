"""
Levantando os próprios erros com raise

raise -> Lança execeções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Pra simplificar, pense no raise como sendo util para que possamos criar nossa próprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipodeErro('Mensagem de erro')


#Exemplo Real

def colere(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    print(f'O texto {texto} será impresso na cor {cor} ')

colere('Geek', 'Azul')

#Exemplo Real

def colere(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor} ')

colere('Geek', 'preto')

Obs: O raise, assim como o return(), finaliza a função. Ou seja, nada após o raise é executado.
"""

#Exemplo Refatorado

def colere(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor} ')

colere('Geek', 'preto')