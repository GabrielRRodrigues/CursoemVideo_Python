# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 86 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLACK, Fore.WHITE, ' MATRIZ EM PYTHON ', Fore.RESET, Back.RESET))

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{linha},{coluna}]: '))
        matriz[linha].append(num)

print('-'*40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print('')
