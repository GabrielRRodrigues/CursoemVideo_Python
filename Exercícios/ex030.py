#Crie um programa que leia um número inteiro e mostre na tela se ele é ÍMPAR ou PAR.


print('{} EX 30 {}'.format('>'*10, '<'*10))
print('\n\033[7;31m{} ÍMPAR ou PAR {}\033[m\n'.format('='*7, '='*7))

num = int(input('Digite um número: '))

print(('{}→ PAR ←{}' if num % 2 == 0 else '{}→ ÍMPAR ←{}').format('\033[7;36m', '\033[m'))

