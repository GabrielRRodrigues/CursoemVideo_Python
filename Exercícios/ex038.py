'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

print('{} EX 38 {}\n'.format('>'*15, '<'*15))
print('{} {} COMPARANDO NÚMEROS {} {}\n'.format('\033[7;34m', '→'*7, '←'*7, '\033[m'))

n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))

print('\n{}{}{}\n'.format('\033[7;34m', '='*20, '\033[m'))
if n1 == n2:
    print('Não existe valor maior, os dois são iguais')
elif n1 > n2:
    print('O {}primeiro{} valor é maior'.format('\033[4;33m', '\033[m'))
else:
    print('O {}segundo{} valor é maior'.format('\033[4;33m', '\033[m'))