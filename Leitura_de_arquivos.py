"""
Leitura de arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente diguinifca 'abrir'

open() -> Na forma mais simpler de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para o aruivo a ser lido. Essa função retorna um _io.TextIoWrapper e 
é com ele que trabalhamos então

https://docs.python.org/3/library/functions.html#open

#Obs: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então termemos o erro FileNotFoundError

<_io.TextIOWrapper name='texto,txt' mode='r' enconidrg='UTF=8'

mode r -> MOdo de Leitura. r -> read() -> ler
"""
#Exemplo

arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

#para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())

#Obs: O python, utiliza um recurso para trabalhar com arquivos chamados cursor. Esse cursor,
#Funciona como o cursor quando estamos escrevendo

#Obs: afunção read() lê todo o conteúdo do arquivo
