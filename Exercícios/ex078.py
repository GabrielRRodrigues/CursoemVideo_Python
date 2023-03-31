# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e
# as suas respectivas posições na lista.

from colorama import Fore, Back, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 78 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' Maior - Menor (LISTA) ', Fore.RESET, Back.RESET))

valores = []
for i in range(0,5):
    valores.append(int(input('Digite um número: ')))

print(f'\nMaior {Fore.GREEN}↑{Fore.RESET}: {max(valores)} na(s) posição(ões) ', end='')
for pos, num in enumerate(valores):
    if num == max(valores):
        print(pos+1, end =' ')

print(f'\nMenor {Fore.RED}↓{Fore.RESET}: {min(valores)} na(s) posição(ões) ', end='')
for pos, num in enumerate(valores):
    if num == min(valores):
        print(pos+1, end=' ')