# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os numeros pares
# e os numeros ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 82 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.MAGENTA, Fore.BLACK, ' DIVIDINDO numeros ', Fore.RESET, Back.RESET))

numeros = []
par = []
impar = []

while True:
    numeros.append(int(input('Digite um número: ')))
    if numeros[len(numeros)-1] % 2 == 0:
        par.append(numeros[len(numeros)-1])
    else:
        impar.append(numeros[len(numeros)-1])
    while True:
        resp = str(input('Deseja inserir mais algum número? [S/N]→ '))[0]
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break
    print('-'*40)

print(f'\nNúmeros digitados: {", ".join(str(x) for x in numeros)} '
      f'\nPares: {", ".join(str(x) for x in par)}'
      f'\nÍmpares: {", ".join(str(x) for x in impar)}')