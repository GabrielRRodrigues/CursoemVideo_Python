#Crie um programa que faça o computador jogar Jokenpô com você.

import emoji
from random import randint
import playsound

print('{} EX 45 {}\n'.format('>'*15, '<'*15))
print('{}{:↔^40}{}\n'.format('\033[7;33m', ' JOKEMPÔ ', '\033[m'))

jogadas = [':fist:', ':hand:', ':v:']
pc = randint(0, 2)


input('Vamos jogar!! \n\nPressione \033[4;32mENTER\033[m para começar. \n')

playsound.playsound('jokenpo.mp3')

print(emoji.emojize((jogadas[pc]), language='alias'))

# print('Vamos \033[4;32mJogar\033[m \n\n{}{}{}'.format('\033[7;33m', '↔'*25, '\033[m'))
# player = int(input('Faça sua jogada: \n\n1) Pedra \n2) Papel \n3) Tesoura \n\nJogada: '))
# campeao = -1
#
# if player == 1:
#     print('\n{}{}{}\n'.format('\033[7;33m', '↔'*25, '\033[m'))
#     if pc == 0:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 0
#     elif pc == 1:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 1 #pc
#     else:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 2 #player
# elif player == 2:
#     print('\n{}{}{}\n'.format('\033[7;33m', '↔'*25, '\033[m'))
#     if pc == 0:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 2
#     elif pc == 1:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 0
#     else:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 1
# elif player == 3:
#     print('\n{}{}{}\n'.format('\033[7;33m', '↔'*25, '\033[m'))
#     if pc == 0:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 1
#     elif pc == 1:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 2
#     else:
#         print('Computador jogou {}'.format(emoji.emojize(jogadas[pc], language='alias')))
#         print('Você jogou {}'.format(emoji.emojize(jogadas[player-1], language='alias')))
#         campeao = 0
# else:
#     print('\n{}{}{}\n'.format('\033[7;33m', '↔' * 25, '\033[m'))
#     print('{}JOGADA INVÁLIDA!!{}'.format('\033[7;31m', '\033[m'))
#
# if campeao == 0:
#     print('Campeão: {}{}{}'.format('\033[4;33m', ' EMPATE ', '\033[m'))
# elif campeao == 1:
#     print('Campeão: {}{}{}'.format('\033[4;31m', ' PC ', '\033[m'))
# elif campeao == 2:
#     print('Campeão: {}{}{}'.format('\033[4;32m', ' JOGADOR ', '\033[m'))
