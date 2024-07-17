"""
Escrevendo em arquivos

# Obs: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler,
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escreve nele.

# Obs: Ao abrir um arquivo para escritam o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo após abrir o arquivo utilizamos a função write().
Esta função recebe um string como parâmetro.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido

#Exemplo de escrita - modo 'W' - write (escrita)

#Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linas quisermos.\n')
    arquivo.write('Está é a ultima linha')

#Forma tradicional de escrita em arquivo(Não Pythonica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek\n '  * 1000)
"""

while True:
    with open('frutas.txt', 'w') as arquivo:
        while True:
            fruta = input("Informe uma fruta ou digite sair: ")
            if fruta != 'sair':
                arquivo.write(fruta)
            else:
                break