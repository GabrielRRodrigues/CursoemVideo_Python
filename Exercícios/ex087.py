# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 87 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLACK, Fore.WHITE, ' MAIS SOBRE MATRIZ EM PYTHON ', Fore.RESET, Back.RESET))

matriz = [[], [], []]
pares = []
soma = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um número para a posição [{linha},{coluna}]: '))
        matriz[linha].append(num)
        if num % 2 == 0:
            pares.append(num)
        if coluna == 2:
            soma += num
print('-'*40)
for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end=' ')
    print('')

print(f'{"-"*40}'
      f'\nA soma de todos os valores pares digitados é: {sum(pares)}'
      f'\nA soma dos valores da terceira coluna é: {soma}'
      f'\nO maior valor da segunda linha é: {max(matriz[1])}')
