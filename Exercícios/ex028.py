'''Escreva um programa que faça 0 computador "pensar" em um número interiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O rpograma deverá escrever na tela se o usuário vendeu ou perdeu.'''

from random import randint

print('{} EX 28 {}'.format('>'*10, '<'*10))
print('\n{} ADIVINHAÇÃO {}\n'.format('='*8, '='*8))

num = randint(0, 5)
num1 = int(input('Vou pensar em um número entre 0 e 5, tente adivinhar: '))

print('{} \nVocê ganhou!! :\')'.format('='*25) if num1 == num else '{} \nVocê perdeu!! :\'('.format('='*25))
