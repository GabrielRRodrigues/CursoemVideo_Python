# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from colorama import init, Fore, Back
from random import randint

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 88 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' PALPITES MEGA SENA ', Fore.RESET, Back.RESET))

palpites = []
jogo = []

quant_jogos = int(input('Quantos jogos deseja realizar? → '))

for i in range(0, quant_jogos):
    while True:
        num = randint(1, 60)
        jogo.append(num)
        jogo = list(set(jogo))
        if len(jogo) == 6:
            palpites.append(jogo[:])
            jogo.clear()
            break
print('\n{:-^35}'.format(' Palpitando... '))
for i in range(1, len(palpites)+1):
    print(f'Jogo {i}: {sorted(palpites[i-1])}')
print('{:-^35}'.format(' Bons Jogos! '))