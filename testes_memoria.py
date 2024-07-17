"""
Teste de Memória com Generators

#Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13... 

# Test 1 
for n in fib_lista(100000):
    print(n)
"""
#Função usando listas 449Mb

def fib_gen(max):
    nums = []
    a, b = 0, 1
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

#Teste 2 Geradores 

for n in fib_gen(100000):
    print(n)

