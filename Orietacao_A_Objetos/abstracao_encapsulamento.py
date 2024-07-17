"""
POO - Abstracao e Encapsulamento

O grande objetivo de POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> cápsula


            classe
_________________________________
|                               |
|           Atributos e métodos |
|_______________________________|

#Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado __nome e um método privado chamado
__falar(self)

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__fala()

Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular) #Name Mangling

conta1._Conta__titular = 'Angelina'

print(conta1.__dict__)

print(conta1.__dict__)

conta1.deposita(1200.00)

conta1.sacar(300.00)
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def deposita(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
            
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor precisa ser positivo')
    def tranferir(self, valor, conta_destino):
        # 1 - remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 #Taxa de tranferencia

        #2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

#Testando
        
conta1 = Conta('Geek', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Raphael', 300, 2000)
conta2.extrato()

conta1.tranferir(50.00, conta2)

conta1.extrato()
conta2.extrato()