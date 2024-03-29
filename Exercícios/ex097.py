# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 97 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.MAGENTA, Fore.BLACK, ' UM PRINT ESPECIAL ', Fore.RESET, Back.RESET))


def escreva(txt):
    print(f'\n{"=" * (len(txt)+5)}'
          f'\n{txt.center(len(txt)+4)}'
          f'\n{"=" * (len(txt)+5)}')


texto = str(input("Texto: "))
escreva(texto)