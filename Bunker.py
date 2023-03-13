from os import system
import random
system('cls')

with open('profesion.txt', 'r') as f:
    lista_profesion = f.readlines()
with open('boli.txt', 'r') as f:
    lista_sickness = f.readlines()
with open('fobii.txt', 'r') as f:
    lista_fobii = f.readlines()
with open('tr_caracter.txt', 'r') as f:
    lista_tr_caracter = f.readlines()
with open('bagaj.txt', 'r') as f:
    lista_bagaj = f.readlines()

lista_profesion = [line.strip() for line in lista_profesion]
lista_sickness  = [line.strip() for line in lista_sickness]
lista_fobii     = [line.strip() for line in lista_fobii]
lista_tr_caracter  = [line.strip() for line in lista_tr_caracter]
lista_bagaj     = [line.strip() for line in lista_bagaj]



profesii_random = random.choice(lista_profesion)
sickness_random = random.choice(lista_sickness)
fobii_random    = random.choice(lista_fobii)
bagaj_random    = random.choice(lista_bagaj)
tr_caracter_random = random.sample(lista_tr_caracter,2)

with open('Player_card.txt', 'w') as f:
    f.write(f'Player card:\nProfesie: {profesii_random},\nBoala: \\\
 {sickness_random},\nFobie: {fobii_random},\nBagaj: {bagaj_random},\nCaracter: \\\
{tr_caracter_random}\n')
