# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 66 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;35m', ' VÁRIOS NÚMEROS COM FLAG ', '\033[m'))

cont = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'\nNúmeros digitados: {cont} \nSoma: {soma}')
