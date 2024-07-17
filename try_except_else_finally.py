"""
Try/ Except/ Else/ Finally

Dica de quando e onde tratar código:

Toda entrada do Usuário deve ser Tratada!

#Else -> é executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

    
# Finally 

try:
    num = int(input("Informe um numero: ")) 
except ValueError:
    print("Você não digitou um valor válido. ")
else:
    print(f"Você digitou o número {num}")
finally:
    print("Executando o finally")

#Obs: O bloco finally é sempre executado. Idependete se houve exceção ou não

# O finally, geralmente é utilizado para fechar ou desalocar recursos

#Exemplo mais complexo ERRADO

def dividir(a , b):
    return a / b
try:
    num1 = int(input("Informe o primeiro numero: "))
    num2 = int(input("Informe o segundo numero: "))
except ValueError:
    print('O valor precisar númerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valro incorreto')

#Exemplo mais complexo Correto
#OBS Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a , b):
    try:
         return int(a) / int(b)
    except ValueError:
         print("Valor incorreto!!")
    except NameError:
         print("Valor incorreto!!")
    except ZeroDivisionError:
         return 'Não é possivel realizar uma divisão por zero'

num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))

#Exemplo mais complexo Genérico
#OBS Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a , b):
    try:
         return int(a) / int(b)
    except:
         print("Ocorreu um problema")

num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))

#Exemplo mais complexo Semi-Genérico
#OBS Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a , b):
    try:
         return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
         return f'Ocorreu um problema: {err}'

num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))
"""
