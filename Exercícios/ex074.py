# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.

from colorama import Fore, Back, init
from random import randint

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 74 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' Maior - Menor ', Fore.RESET, Back.RESET))

valores = ()
for i in range(0, 5):
    num = randint(0, 100)  # Gera um número aleatório entre 1 e 10
    valores = valores + (num,)

print(f'Valores gerados: {valores}'
      f'\nMenor ↓: {Fore.RED}{sorted(valores)[0]}{Fore.RESET}' 
      f'\nMaior ↑: {Fore.GREEN}{sorted(valores)[-1]}{Fore.RESET}')

# print(f'Valores gerados: {valores}'
#       f'\nMenor ↓: {Fore.RED}{min(valores)}{Fore.RESET}'
#       f'\nMaior ↑: {Fore.GREEN}{max(valores)}{Fore.RESET}')