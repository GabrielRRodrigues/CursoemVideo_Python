# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from colorama import init, Fore, Back
from random import randint
from operator import itemgetter

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 91 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.YELLOW, Fore.BLACK, ' JOGO DE DADOS EM PYTHON ', Fore.RESET, Back.RESET))

jogo = {}

print('Valores sorteados: ')
for i in range(1, 5):
    jogo[f'Jogador {i}'] = randint(1, 6)
    print(f'Jogador {i} tirou {jogo[f"Jogador {i}"]} no dado.')

# print('\n'+'-'*40)
print(f'\n{" RANKING " :=^30}\n')

for pos, i in enumerate(sorted(jogo.items(), key=itemgetter(1), reverse=True)):
    print(f'{f"{pos+1}º lugar: {i[0]} com {i[1]}":^30}')


