"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista

from csv import writer

with open('filmes.csv', 'a') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])

"""

#DictWriter

from csv import DictWriter

with open('filmes1.csv', 'a') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duracao": duracao})