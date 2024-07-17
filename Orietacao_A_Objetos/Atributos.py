"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;


# Atributos de instância: São atributos declarados dentro do método construtor.

# Obs: Método construtor é um método especial utilizado para a contrução do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor
    }

    public int getVoltagem(){
        return this.voltagem;
    }

}

Em Python, por convenção, ficou estabelecido que todo, atributo de uma classe é publico
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado deve ser tratado como privado, ou seja, 
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido como Name Mangling.

#OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso ao atributos sinalizados como privados fora de classe.

#Exemplo
        
user = Acesso('user@gmail.com', '123456')

print(user.email)

#print(user.__senha) #AttributeError

print(user._Acesso__senha) #Temos acesso. Mas não deveríamos fazer esse acesso; (Name Mangling)

#Oque siginifca atributos de instância?

#Siginifca, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
#terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

#Atributos de Classe

# Atributos de classe. são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do contrutor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seu próprios
# valores como é o cado dos atributos de instância, co os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) #Acesso possível, mas incorreto de um atributo de classe
print(p2.valor) #Acesso possível, mas incorreto de um atributo de classe

#Obs: Não precisamos criar um intância de uma classe para fazer um acesso a um atributo de classe

print(Produto.imposto)# Acesso correto de um atríbuto de classe

print(p1.id)
print(p2.id)

#Obs: Em linguagem como o Java, os atributos conhecidos como atributos de classe aqui em Python
# São chamados de atributos estáticos;

"""
# Classes com Atributo de Instância Público
class Lampada:
    
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha 


#Atributos Públicos e Atributos Privados
        
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha 

    def mostra_senha(self):
        print(self.__senha)
    
    def mostra_email(self):
        print(self.email)



#Refatorar a classe Produto

class Produto:

    # Atributo de Classe
    imposto = 1.05 #0.05 de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

#Atributos Dinâmicos -> Um atributos de intância que pode ser cirado em tempo de excução.
        
#OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', ' Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' #Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
        
#print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}') # AttributeError

#Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

#print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)