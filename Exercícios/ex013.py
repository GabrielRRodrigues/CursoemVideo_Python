'''Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.'''

print('{} EX13 {}\n'.format('>' * 10, '<' * 10))
print('{} AUMENTO DE SALÁRIO {}\n'.format('$' * 3, '$' * 3))

sal = float(input('Salário: R$ '))
up = float(input('Aumento(%): '))

print('{}\nSalário com aumento de {:.2f} %: R$ {:.2f}'.format('=' * 28, up, sal * (1 + up / 100)))