#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
print('{} {} {}\n'.format('>' * 10, 'EX 05', '<' * 10))
print('{} ANTECESSOR - SUCESSOR {}\n'.format('+'*2, '+'*2))

cores= {'limpa':'\033[m',
        'verde':'\033[1;32m',
        'vermelho':'\033[1;31m'}

num = int(input('Digite um número: '))
print('{}\n{}Antecessor:{} {}\nNúmero: {} \n{}Sucessor:{} {}'.format('='*28, cores['vermelho'], cores['limpa'], num-1, num, cores['verde'], cores['limpa'], num+1))
