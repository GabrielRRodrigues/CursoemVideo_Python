# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('{} EX 47 {}\n'.format('>'*15, '<'*15))
print('{}{:↔^40}{}\n'.format('\033[7;33m', ' NÚMEROS PARES ', '\033[m'))

for i in range(2, 51, 2):
    print(i)
