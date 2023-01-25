#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

print('{} EX 23 {}'.format('>'*10, '<'*10))
print('\n{} SEPARADOR NÚMEROS {}\n'.format('='*4, '='*4))

num = input('Digite um número de 0 a 9999: ')
num1 = []
num2 = int(num)

while num2 < 0 or num2 > 9999:
    print('\n{} Número inválido!! {} \n'.format('>'*7, '<'*7))
    num2 = int(input('Digite um número de 0 a 9999: '))

for i in str(num2):
    num1.append(i)

if num2 < 1000:
    if num2 < 100:
        if num2 < 10:
            num1.insert(0, 0)
        num1.insert(0, 0)
    num1.insert(0, 0)

print('{} \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format('='*28, num1[3], num1[2], num1[1], num1[0]))
