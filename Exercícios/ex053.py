# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#
# Exemplos de palíndromos:
#
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA.

import unidecode

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 53 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;33m', ' PALÍNDROMO ', '\033[m'))

frase = input('Digite uma frase: ').strip().upper()

frase1 = unidecode.unidecode(frase.replace(" ", ''))
frase2 = frase1[::-1]

print('\"{}\" → {} um palíndromo!'.format(frase, '\033[32mÉ\033[m' if frase1 == frase2 else '\033[31mnão é\033[m'))
