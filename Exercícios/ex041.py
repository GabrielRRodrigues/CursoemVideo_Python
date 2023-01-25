'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date
print('{} EX 41 {}\n'.format('>'*15, '<'*15))
print('{} {} CLASSIFICAÇÃO NATAÇÃO {} {}\n'.format('\033[7;34m', '→'*7, '←'*7, '\033[m'))

ano = int(input('Anos de Nascimento: '))
idade = date.today().year - ano

print('\n{}{}{}\n'.format('\033[7;34m', '↔'*28, '\033[m'))
if idade <= 9:
    print('Idade: {} \nCategoria: {}MIRIM{}'.format(idade, '\033[4;32m', '\033[m'))
elif idade <= 14:
    print('Idade: {} \nCategoria: {}INFANTIL{}'.format(idade, '\033[4;32m', '\033[m'))
elif idade <= 19:
    print('Idade: {} \nCategoria: {}JÚNIOR{}'.format(idade, '\033[4;32m', '\033[m'))
elif idade <=25:
    print('Idade: {} \nCategoria: {}SÊNIOR{}'.format(idade, '\033[4;32m', '\033[m'))
else:
    print('Idade: {} \nCategoria: {}MASTER{}'.format(idade, '\033[4;32m', '\033[m'))
