"""
Sistemas de Arquivos - Navegação

Um arquivo possue duas partes

Nome- Exemplo: SistemaDeArquivos_Navegacao
Extensão- Exemplo:.py -> É um arquivo Python pois é associado ao Python pelo .py

Root Directory

Windows: C:/
Posix: /

PAra fazer o uso de manipulação de arquivos do sistema operacional, precisamos importar 
e fazer uso do módulo os.

os -> OPerating System - Sistema Operacional

#Fazer o Import
import os

#getcwd() -> pego o current work directory - diretório de trabalho corrente
#Retorna o path (caminho absoluto)
print(os.getcwd())

#Para mudar o diretório, podemos utilizar o chdir

os.chdir('..')

print(os.getcwd())
"""

#Fazer o Import
import os