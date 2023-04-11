# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 85 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.YELLOW, Fore.BLACK, ' LISTA COM PARES E ÍMPARES ', Fore.RESET, Back.RESET))

numeros = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'\n{"-"*30}\nNúmeros Pares: {sorted(numeros[0])} \nNúmeros Ímpares: {sorted(numeros[1])}')


