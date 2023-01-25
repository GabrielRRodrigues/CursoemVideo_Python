# Faça um programa que leia um número qualquer e mostre o seu fatorial
# Ex: 5! = 5 * 4 * 3 * 2 * 1

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 52 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;31m', ' FATORIAL ', '\033[m'))

num = int(input('Número: '))
num1 = fat = num
i = 0

print('\n{}! = {} ×'.format(num, num), end=' ')

while num1 != 1:
    fat = fat * (num1 - 1)

    print('{}'.format(num1 - 1), end='')
    print(' ×' if num1 > 2 else ' =', end=' ')
    num1 -= 1

print('{}'.format(fat))