# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 96 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.MAGENTA, Fore.BLACK, ' FUNÇÃO QUE CALCULA ÁREA ', Fore.RESET, Back.RESET))


def area(a, b):
    print(f'{"-" * 20}'
          f'\nA área de um terreno de {a} x {b} é {a * b:.2f} m².')


print('Controle de terrenos'
      f'\n{"-" * 20}')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)
