# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada
# a) de 1 até 10, de 1 em
# b) de 10 até 0, de 2 em
# c) uma contagem personalizada

from colorama import init, Fore, Back
from time import sleep

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 98 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' FUNÇÃO DE CONTADOR ', Fore.RESET, Back.RESET))


def contador(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i > f:
        if p > 0:
            p = p * -1
        f = f - 2

    for j in range(i, f + 1, p):
        print(j, end=' ')
        # sleep(0.3)
    print('FIM!!')
    print(f'{"=" * 35}')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)
