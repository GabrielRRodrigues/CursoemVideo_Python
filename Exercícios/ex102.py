# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

from colorama import Back, Fore, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 102 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' FUNÇÕES PARA FATORIAL ', Fore.RESET, Back.RESET))


def fatorial(num, show=False):
    fat = 1
    calc = ''
    for i in range(num, 0, -1):
        fat *= i
        if i != 1:
            calc += str(i) + ' × '
        else:
            calc += '1 = ' + str(fat)

    if show is True:
        return calc
    else:
        return fat


num = int(input('Digite um número: '))

while True:
    opcao = str(input('Exibir os cálculos? [S/N/I] ')).upper()[0]
    if opcao in 'SNI':
        if opcao == 'S':
            show = True
        else:
            show = ''
        break
    print('Opção inválida!! Digite S = SIM, N = NÃO ou I = INDIFERENTE.')


print(f'\n{num}! = {fatorial(num, show)}')


