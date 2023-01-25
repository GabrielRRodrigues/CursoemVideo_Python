'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome completo com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome'''

print('{} EX 22 {}'.format('>'*10, '<'*10))
print('\n{} LENDO STRING {}\n'.format('='*6, '='*6))

nome = input('Digite seu nome completo: ')

print('{} \nNOME: {}'.format('='*28, nome.upper()))
print('nome: {}'.format(nome.lower()))
print('Letras: {}'.format(len(''.join(nome.split()))))
print('Letras Nome: {}'.format(len(nome.split()[0])))
