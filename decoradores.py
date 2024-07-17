"""
Decoradores (Decorators)

Oque são Decorators?

- Decorators são funções;
- Decorator envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe prórpia, usando "@" (Syntact Sugar / Açúcar Sintático)

|------------------------------------------|
|       Function Decorator                 |
--------------------------------------------

---------------------------------------------
||------------------------------------------||
||       Função decorada                    ||
||-------------------------------------------|
|---------------------------------------------



#Decorator como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você! ')
        funcao()
        print('Tenha um ótimo dia! ')
    return sendo()

def saudacao():
    print('Seja bem-vindo(a) à Geek University')

#Testando 1
    
#saudacao()
    
teste = seja_educado(saudacao)

teste()

#Testando 2 

def raiva():
    print('Eu te odeio')

raiva_educada = seja_educado(raiva)

raiva_educada()

#Decorators com Systax Sugar

def seja_educado_mesmo(funcao):
    def sendo_educado():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo_educado

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

#Testando
    
apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()

|------------------------------------------------
|home   |serviçoes  |Produtos   |Administrativos|
|------------------------------------------------

https://www.suaempresa.com.br/home
https://www.suaempresa.com.br/servicos
https://www.suaempresa.com.br/produtos
https://www.suaempresa.com.br/admin

#Não é codigo funcional (Que funcione) é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect(https://www.suaempresa.com.br)

def home(request):
    return "Pode acessar home"

@checa_login
def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    
"""