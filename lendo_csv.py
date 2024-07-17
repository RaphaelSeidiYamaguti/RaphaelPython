"""
Lendo arquivos CSV

CSV - COmma Separeted Values - Valores separados por vírgula

#Separador por vírgula
1, 2, 3, 4, 5, 6

"geek", "university", "python", "ciência", "dados"

#Separados por ponto e virugula
1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; "ciência"; "dados"

# Separador por espaço

1 2 3 4 5 6

"geek" "university" "python" "ciência" "dados"

#Possível de trabalhar mas não é o ideal (trabalhoso)
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split('.')
    print(dados)

    
A linguagem Python possue duas formas diferente para ler dados em arquivos CSV:
    -reader -> Permite que iteremos sobre as linhas do arquivo como listas:
    -DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts:

#Reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f'{linha [0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')

# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f'{linha ['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} centímetros')
"""
