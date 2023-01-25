#Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import floor
print('{} EX 16 {}'.format('>'*10, '<'*10))
print('\n{} ARREDONDAR ↓ {}\n'.format('>'*6, '<'*6))

num = float(input('Digite um número: '))
print('{} \nPorção inteira: {}'.format('='*25, floor(num)))