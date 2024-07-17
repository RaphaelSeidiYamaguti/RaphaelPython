"""
POO - Herança (Inheritance)

A Ideia de herança é a de reaproveitar código. Também estender nossas classes.

OBS: Com a herança a partir de uma classe existente nós extendemos outa classe que passa
a herdar atributos e métodos da classe herdada.


Cliente
    -Nome;
    -Sobrenome;
    -CPF;
    -Renda;

Funcionario
    -Nome;
    -Sobrenome;
    -CPF;
    -Matricula

Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidade:

class Clientes:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
cliente1 = Cliente('Angelina', 'Jolie','123.456.789-99', 3000)

funcionario1 = Funcionario('Raphael','Seidi', '061,598,759-14', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por
    -Super Classe;
    -Classe Mãe;
    -Classe Pai;
    -Classe Base;
    -Classe Genérica;

Quando uma Classe herda de outra classe, ela é chamada:
    [Cliente, Funcionário]
    - Sub Classe;
    - Classe filha;
    - Classe específica;

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa):
    '''Cliente herda pessoa'''
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) #Forma não comum de acessar dados da super classe
        self.__renda = renda
    
class Funcionario(Pessoa):
    '''Funcionario herda Pessoa'''
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

cliente1 = Cliente('Angelina', 'Jolie','123.456.789-99', 3000)

funcionario1 = Funcionario('Raphael','Seidi', '061,598,759-14', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)
 
#Sobrescrita de Métodos (Overriding)       

Sobrescrita de Método ocorre quando reescrevemos/reimplementamos um método presente na super classe
em classes filhas.

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa):
    """Cliente herda pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) #Forma não comum de acessar dados da super classe
        self.__renda = renda
    
class Funcionario(Pessoa):
    """Funcionario herda Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


#Sobrescrita de Métodos (Overriding)
        
cliente1 = Cliente('Angelina', 'Jolie','123.456.789-99', 3000)

funcionario1 = Funcionario('Raphael','Seidi', '061.598.759-14', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())