#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

print('{} EX 32 {}'.format('>'*10, '<'*10))
print('\n{} ANO BISSEXTO {}\n'.format('='*7, '='*7))

ano = int(input('Ano: '))

if ano == 0:
    ano = date.today().year

print('='*25 + '\n{} {} Bissexto'.format(ano, 'é' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'não é'))