# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 68 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;33m', ' PAR OU ÍMPAR ', '\033[m'))

from random import randint

vitorias = 0

while True:
    while True:
        op = int(input('\n1) Ímpar \n2) Par \n\n{} \nNúmero da opção desejada: '.format('=' * 15)))
        if op == 1 or op == 2:
            break
        print('\n\033[7;31m>> Opcão inválida!!\033[m')
    pc = randint(0, 11)
    # print(pc)

    while True:
        jogador = int(input('\nDigite um número de 0 a 10: '))
        if 0 <= jogador <= 10:
            break
        print('\n\033[7;31mNúmero inválido!!\033[m')

    soma = pc + jogador

    if op == 1:
        if soma % 2 == 0:
            print('\n{} \n{}Você perdeu!!{} \nComputador jogou {} e você {}'.format('=' * 20, '\033[7;31m', '\033[m', pc, jogador))
            print('{} + {} = {} (PAR) \n{} \nVitórias: {}'.format(pc, jogador, pc + jogador, '=' * 20, vitorias))
            break
        else:
            print('\n{} \n{}Você ganhou!!{} \nComputador jogou {} e você {}'.format('=' * 20, '\033[7;32m','\033[m', pc, jogador, pc))
            print('{} + {} = {} (ÍMPAR) \n{}'.format(pc, jogador, pc + jogador, '=' * 20))
            vitorias += 1
    else:
        if soma % 2 == 0:
            print('\n{} \n{}Você ganhou!!{} \nComputador jogou {} e você {}'.format('=' * 20, '\033[7;32m', '\033[m', pc, jogador, pc))
            print('{} + {} = {} (PAR) \n{}'.format(pc, jogador, pc + jogador, '=' * 20))
            vitorias += 1
        else:
            print('\n{} \n{}Você perdeu!!{} \nComputador jogou {} e você {}'.format('=' * 20, '\033[7;31m', '\033[m', pc, jogador))
            print('{} + {} = {} (ÍMPAR) \n{} \nVitórias: {}'.format(pc, jogador, pc + jogador, '=' * 20, vitorias))
            break
print('\nFim de jogo...')