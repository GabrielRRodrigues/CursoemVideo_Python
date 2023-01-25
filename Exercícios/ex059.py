# # Crie um programa qie leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 59 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;36m', ' MENU DE OPÇÕES ', '\033[m'))

num1 = int(input('1º número: '))
num2 = int(input('2º número: '))
op = 0

while op != 5:
    op = int(input('\n\033[7;32m{:↔^25}\033[m \n\n1 ) somar \n2 ) multiplicar \n3 ) maior \n4 ) novos números \n5 ) sair do programa \n\nInsira o número da opção desejada: '.format(' MENU ')))

    if op == 1:
        print('\n{} + {} = {}'.format(num1, num2, num1 + num2))
    elif op == 2:
        print('\n{} × {} = {}'.format(num1, num2, num1 * num2))

    elif op == 3:
        print('\n{} é maior que {}'.format(num1 if num1 > num2 else num2, num2 if num1 > num2 else num1))

    elif op == 4:
        num1 = int(input('\n1º número: '))
        num2 = int(input('2º número: '))

    else:
        print('\n\033[7;31mOpção inválida!\033[m Tente novamente.')

print('\n >>> Saindo', end='')
for i in range(0, 3):
    sleep(0.3)
    print('.', end='')
    sleep(0.4)
