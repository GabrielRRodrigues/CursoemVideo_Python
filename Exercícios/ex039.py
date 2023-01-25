'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se
alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
print('{} EX 39 {}\n'.format('>'*15, '<'*15))
print('{} {} ALISTAMENTO {} {}\n'.format('\033[7;33m', '→'*7, '←'*7, '\033[m'))

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('\n{}{}{}\n'.format('\033[7;33m', '↔'*25, '\033[m'))

if idade == 18:
    print('Chegou o ano de seu alistamento. \nSe apresente {}até 31 de Dezembro de {}{}'.format('\033[7;33m', atual, '\033[m'))
elif idade > 18:
    print('Alistamento pendente desde {}. \nSeu alistamento está {}atrasado em {} anos{}.'.format(atual - (idade - 18), '\033[7;31m', atual -(atual - (idade - 18)), '\033[m'))
else:
    print('Alistamento fora do prazo. \nAlistamento previsto para {}daqui {} {}{}.'.format('\033[7;32m', (nasc + 18) - atual, 'ano' if nasc + 18 - atual == 1 else 'anos', '\033[m'))
