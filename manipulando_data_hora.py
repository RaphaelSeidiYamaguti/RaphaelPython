"""
Manipulando Data e Hora

Python tem um módulo built-in (integrada) para se trabalhar com data e hora
chamado datetime

2024-02-05 10:33:27.596830 

2024-02-21 15:41:38.056382

import datetime

#print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

#Retorna a data e hora corrente
print(datetime.datetime.now()) # 2024-02-05 10:33:27.596830 -> Us format


#datetime.datetime.now(year, month, day, hour, minute, second, milisecond) 
print(repr(datetime.datetime.now())) 

#replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

#Alterar o horario para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

#Recebendo dados do usuario e convertendo para data

print(type(evento))

print(type('31/12/2018'))

print(evento)

nascimento = input('Informe sua data de nascimento  (dd/mm/yyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

import datetime

evento = datetime.datetime.now()


#Acessa individual dos elementos de data e hora

print(evento.year) #ano
print(evento.month) #mes
print(evento.day) #dia
print(evento.hour) #hora
print(evento.minute) #minuto
print(evento.second) #segundo
print(evento.microsecond) #microsegundo

print(dir(evento))