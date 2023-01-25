#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

print('{} EX 25 {}'.format('>'*10, '<'*10))
print('\n{} NOME SILVA {}\n'.format('='*8, '='*8))

nome = input('Nome completo: ').title()

print('{} \nPossui Silva no nome: {}'.format('=' * 28, 'Silva' in nome))

'''if nome.count('Silva') > 0:
    print('{} \nPossui Silva no nome!!'.format('='*28))
else:
    print('{} \nNão possui Silva no nome!!'.format('='*28))'''
