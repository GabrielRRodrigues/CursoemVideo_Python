# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 81', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.MAGENTA, Fore.BLACK, ' Exraindo dadods - Lista ', Fore.RESET, Back.RESET))

resp = 'S'

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Deseja informar mais algum número: [S/N]→ '))[0]
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break
    print('×'*40)
valores.sort(reverse=True)
print(f'\nForam digitados {Fore.GREEN}{len(valores)+1}{Fore.RESET} número(s)'
      f'\nA lista em ordem decrescente: {", ".join(str(x) for x in valores)}'
      f'\nNº5 foi digitado? '
      f'{f"{Fore.GREEN}Sim" if 5 in valores else f"{Fore.RED}Não"}')