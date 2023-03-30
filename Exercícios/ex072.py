#  Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
#  de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

from num2words import num2words as nw
from colorama import init, Fore, Back

init()

print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 72 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.RED, Fore.BLACK, ' NÚMERO POR EXTENSO ', Fore.RESET, Back.RESET))
# print('{}{:×^40} {}\n'.format('\033[7;1;32m', ' NÚMERO POR EXTENSO ', '\033[m'))

while True:
    num = int(input('Digite um número (0-20): '))

    if num <= 0 or num <= 20:
        break

# print(f'Você digitou o número{Fore.BLUE} {nw(num, lang="pt_BR")} {Fore.RESET}')

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print(f'Você digitou o número{Fore.BLUE} {numeros[num]} {Fore.RESET}')
