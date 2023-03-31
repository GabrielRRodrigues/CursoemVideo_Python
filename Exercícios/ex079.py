# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 79 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.YELLOW, Fore.BLACK, ' Valores únicos - LISTA ', Fore.RESET, Back.RESET))

resp = 'S'
valores = []
while True:
    print('×'*40)
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
    else:
        print(f'Valor {Fore.RED}duplicado{Fore.RESET}')

    while True:
        resp = str(input('Deseja digitar mais algum número? (S/N) ')).upper()[0]
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break

valores.sort()
print(f'\nOs valores únicos digitados foram: {", ".join(str(x) for x in valores)}')