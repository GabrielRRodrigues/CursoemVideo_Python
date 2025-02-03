# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

from colorama import Back, Fore, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 103 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' FICHA DO JOGADOR ', Fore.RESET, Back.RESET))


def ficha(nome = '<Desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


n = str(input(f'{"-"*25}\nNome do Jogador: ')).title()
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)
