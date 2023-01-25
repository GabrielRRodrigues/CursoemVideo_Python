#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('{} EX 09 {}\n'.format('>' * 10, '<' * 10))
num = int(input('Digite um número: '))
print('\n\033[7;34m{} Tabuada do {} {}\033[m'.format('×'*3, num, '×'*3))
i = 1
j = 0
while j <= 2:
    if j % 2 == 0:
        print('='*20
              )
    while i <= 10:
        if i < 10:
            print('{} X  {} = {}'.format(num, i, num*i))
        else:
            print('{} X {} = {}'.format(num, i, num*i))
        i += 1
    j += 1






