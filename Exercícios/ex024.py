#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print('{} EX 24 {}'.format('>'*10, '<'*10))
print('\n{} CIDADE SANTO {}\n'.format('='*6, '='*6))

cidade = input('Digite o nome da cidade: ').title()

print(cidade.split()[0][:5] == 'Santo')