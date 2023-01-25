# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from emoji import emojize
from time import sleep

print('{} EX 46 {}\n'.format('>'*15, '<'*15))
print('{}{:↔^40}{}\n'.format('\033[7;31m', ' FOGOS DE ARTIFÍCIO ', '\033[m'))

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print(emojize('\n{}'.format(':tada:'*5), language='alias'))


