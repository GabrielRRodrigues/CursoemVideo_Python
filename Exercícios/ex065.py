# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos e o maior e o menor valores lidos.
# O programa deve perguntar se ele quer ou não a digitar valores.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 66 ', '\033[m'))
print('{}{:↔^40}{}'.format('\033[7;1;36m', ' VÁRIOS NÚMEROS FLAG ', '\033[m'))

cont = i = soma = 0
op = 'S'
# num = int(input('Digite um número: '))
numeros = []

while op not in 'SsNn':
    op = str(input('\nOpção inválida! \nDeseja continuar? [S/N] ')).upper().strip()

while op in 'Ss':
    num = int(input('\nDigite um número: '))
    numeros.append(num)
    cont += 1
    soma += num
    op = str(input('Continuar? [S/N] ')).upper().strip()

print('\n{}\n'.format('↔'*25))
print(sorted(numeros))
print('Média: {:.2f} \nMaior: {} \nMenor: {}'.format(soma/cont, sorted(numeros)[len(numeros)-1], sorted(numeros)[0]))