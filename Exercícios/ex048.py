# Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

print('{:↔^40}\n'.format(' EX 48 '))
print('{}{:↔^40}{}\n'.format('\033[7;35m', ' SOMA MÚLTIPLOS DE 3 (0-500) ', '\033[m'))

soma = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma += i

print('Total: {}'.format(soma))