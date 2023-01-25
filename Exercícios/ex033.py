# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('{} EX 33 {}\n'.format('>' * 10, '<' * 10))
print('{} MAIOR MENOR {}\n'.format('×' * 7, 'x' * 7))

n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
n3 = int(input('Terceiro: '))
maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('=' * 25 + '\nMaior: {} \nMenor: {}'.format(maior, menor))

'''num = []

for i in range(3):
    num.append(int(input('Digite um número: ')))

num.sort()
print('='*25 + '\nMaior: {} \nMenor: {}'.format(num[2], num[0]))'''