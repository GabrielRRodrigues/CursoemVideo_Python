# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final  mostre quantos números foram digitados e qual a soma entre eles

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 64 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;33m', ' TRATANDO VÁRIOS VALORES ', '\033[m'))

soma = c = 0
num = int(input('Digite um número: '))

while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um número: '))

print('{} \nNúmeros digitados: {} \nTotal da soma: {}'.format('↔'*25, c, soma))
