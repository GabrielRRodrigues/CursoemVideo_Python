# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 51 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;32m', ' PROGRESSÃO ARITMÉTICA ', '\033[m'))

termo = int(input('1º termo da PA: '))
razao = int(input('Razão: '))

print('\n{}'.format('='*25))
for i in range(1, 10):
    print('{:2}º termo: {}'.format(i+1, termo+razao))
    termo += razao