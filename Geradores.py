"""
Geradores

- Geradores (Generators) são iterators (Iteradores);
OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras Informações:
-Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra resevada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções geradoras)

---------------------------------------------------------------------------------------
| Funções                                   | Generator Funcions                      |
---------------------------------------------------------------------------------------
| Utilizam return                           | Utilizam yield                          |
---------------------------------------------------------------------------------------
| Retorna uma vez                           | Podem utilizar yield multipla vezes     |
---------------------------------------------------------------------------------------
| Quando executada, retorna um valor        |Quando executada, retorna um generator   |
---------------------------------------------------------------------------------------

# Obs: Uma generator Function não é um Generator. Ela gera um generator

gen = conta_ate(5)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

#Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(10)

for num in gen:
    print(num)
