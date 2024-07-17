"""
Decorators com diferentes assinaturas

#Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olám eu gostaria de {principal}, acompnhando de {acompanhamento}, por favor. '


#Testando

print(saudacao('Angelica'))

print(ordenar('Picanha', 'Batata Frita'))

#Resolver, utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parâmentros de entrada

#Refatorando com a decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f' Olá, eu sou o/a {nome}'

@gritar
def ordernar(principal, acompanhamento)
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

print(saudacao('Felicity'))

@gritar
def lol():
    return 'lol'

print(lol())

#OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordernar(acompanhamento='Batata Frita', principal='Picanha'))
"""

#Decorator com Argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favoria(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

#Testando

print(soma_dez(10, 12))

print(soma_dez(1, 21))

print(comida_favoria('pizza', 'churrasco'))

print(comida_favoria('sanduiche', 'pizza'))