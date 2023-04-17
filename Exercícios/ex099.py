# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from colorama import init, Fore, Back
from time import sleep

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 99 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.YELLOW, Fore.BLACK, ' FUNÇÃO QUE DESCOBRE O MAIOR ', Fore.RESET, Back.RESET))


def maior(* num):
    print('=-' * 25)
    if not num:
        print('Nenhum valor informado!')
    else:
        print(f'Analisando o(s) valore(s) passado(s)...', end=' ')
        for i in num:
            print(i, end=' ')
            # sleep(0.3)
        print(f'\n{"0" if not num else len(num)} valor(es) informado(s) ao todo.'
              f'\nO maior valor informado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
