# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 80 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.MAGENTA, Fore.BLACK, ' Lista Ordenada s/ rep ', Fore.RESET, Back.RESET))

valores = []
for i in range(0, 5):
    num = int(input('Digite um número: '))

    if i == 0 or num > valores[-1]:
        valores.append(num)
    else:
        for pos in range(len(valores)):
            if num < valores[pos]:
                valores.insert(pos, num)
                break

print(f'Valores digitados (em ordem): {", ".join(str(x) for x in valores)}')

