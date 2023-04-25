# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from colorama import init, Fore, Back
from random import randint
from datetime import datetime

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 101 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' FUNÇÕES PARA VOTAÇÃO ', Fore.RESET, Back.RESET))


def voto(ano):
    idade = datetime.now().year - ano
    print(f'Uma pessoa nascida em {ano}, possui {idade} anos.')
    if idade < 16:
        return f'{Fore.RED}NEGADO{Fore.RESET}'
    elif idade < 18 or idade >= 65:
        return f'{Fore.GREEN}OPCIONAL{Fore.RESET}'
    else:
        return f'{Fore.YELLOW}OBRIGATÓRIO{Fore.RESET}'


ano = randint(datetime.now().year - 100, datetime.now().year-1)
print(f'Situação do voto: {voto(ano)}')
