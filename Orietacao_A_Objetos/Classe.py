"""
POO - Classes

Em POO Classes nada mais são do que modelos dos objetos do mundo real sendo representados 
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
    -Atributos -> Representam as caracteristicas do objeto. ou se seja, pelos atributos conseguimos
    reprsentar computacionalmente os estados de um obejto. No caso da lampada, possivelmnete
    iríamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou
    outra cor, qual é luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este obejto 
    pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamentos comum que muito
    provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

    
Em Python, para definir um classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'passa' em Python quando temos um bloco de código que ainda não está 
implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em
maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, 
todas juntas.

Dica Geek: Em computação não utilizamos: Acentuação, caracters especiais ou similares
para nomes de classes, atributos, métodos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistemas, chamamos
estes objetos que serão mapeados para classes de entidade
"""

class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass


valor = int('42') # cast

print(help(int))

inteiro = int()