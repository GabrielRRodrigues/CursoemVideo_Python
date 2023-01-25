'''Faça um programa que leia um ângulo qualquer e mostre na
tela o valor do seno, cosseno e tangente desse ângulo.'''

import math
print('{} EX 18 {}'.format('>'*10, '<'*10))
print('\n{} SEN COS TG {}\n'.format('>'*7, '<'*7))

ang = float(input('Ângulo: '))

print('{} \nSeno: {:.3f} \nCosseno: {:.3f} \nTangente: {:.3f}'.format('='*22, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))
