# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

from colorama import Fore, Back, init
from unidecode import unidecode

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 77 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.YELLOW, Fore.BLACK, ' Contador de Vogais ', Fore.RESET, Back.RESET))

palavras = ('gato', 'cachorro', 'elefante', 'leão', 'tigre',
            'girafa', 'macaco', 'panda', 'rinoceronte', 'hipopótamo')

for palavra in palavras:
    palavraA = unidecode(palavra)
    print(f'{palavra.capitalize()}: ', end='')
    for letra in palavraA:
        if letra in 'aeiou':
            print(f'{letra.upper()}', end=' ')
    print()
