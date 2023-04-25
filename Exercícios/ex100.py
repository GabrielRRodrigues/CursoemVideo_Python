# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.

from colorama import init, Fore, Back
from random import randint
from time import sleep

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 100 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' FUNÇÃO PARA SORTEAR E SOMAR ', Fore.RESET, Back.RESET))

numeros = []


def sorteia():
    print(f'Valores sorteados: ', end = '')
    for i in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[len(numeros)-1], end=', ' if i < 4 else '.')
        sleep(0.4)
    print()



def somaPar(num):
    soma = 0
    pares = []
    for i in num:
        if i % 2 == 0:
            soma += i
            pares.append(str(i))
    print(f'Soma dos pares ({", ".join(pares)}): {soma}')


sorteia()
somaPar(numeros)
