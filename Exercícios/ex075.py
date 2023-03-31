# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

from colorama import Fore, Back, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 75 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' Análise de dados - Tupla ', Fore.RESET, Back.RESET))

numeros = ()
for i in range(0,4):
    num = int(input('Digite um número: '))
    numeros = numeros + (num,)
    par = tuple(num for num in numeros if num % 2 == 0)

print(f'\nA) Quantas vezes apareceu o valor 9: {numeros.count(9)} vez(es)'
      f'\nB) Em que posição foi digitado o primeiro valor 3: '
      f'{str(numeros.index(3)+1) + "ª posição" if 3 in numeros else "não digitado"}'
      f'\nC) Quais foram os números pares: {par}')
