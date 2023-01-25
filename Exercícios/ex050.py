# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 50 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;34m', ' SOMA PARES ', '\033[m'))

soma = 0

for i in range(1, 7):
    num = int(input('Digite o {}º número: '.format(i)))
    if num % 2 == 0:
        soma += num

print('\nTotal pares: {}'.format(soma))
