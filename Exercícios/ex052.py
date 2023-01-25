# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 52 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;36m', ' NÚMERO PRIMO ', '\033[m'))

num = int(input('Número: '))
primo = 0
cont = 0

# for i in range(1, num + 1):
#     primo = 0
#     if i % 2 != 0 and i != 1 and i % 5 != 0 and i % 3 != 0 or i == 5 or i == 3 or i == 2:
#         primo = 1
#         if i == num:
#             cont = 1

for i in range(1, num + 1):
    primo = 0
    if num % i == 0:
        primo = 1
        cont += 1

    print('{}{}'.format('\033[1;31m' if primo == 0 else '\033[1;32m', i), end=' ')
print('\n\n→ \033[m{} {} primo'.format(num, 'é' if cont == 2 else 'não é'))
