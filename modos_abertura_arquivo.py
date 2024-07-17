"""
Modo de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exita, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo
+ -> Abre o modo de atualizaç: Leitura e Escrita

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
sera adicionado SEMPRE ao final

https://docs.python.org/3/library/functions/html#open

# Exemplo X
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe') 

#Exemplo A
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Infome uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""