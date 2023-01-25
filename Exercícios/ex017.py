'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimentp da hipotenusa.'''

from math import hypot

print('{} EX 17 {}'.format('>'*10, '<'*10))
print('\n{} TEOREMA DE PITÁGORAS {}\n'.format('>'*3, '<'*3))

cop = float(input('Cateto Oposto: '))
cad = float(input('Cateto Adjacente: '))

print('{} \nHipotenusa: {:.2f}'.format('='*22, hypot(cop, cad)))
