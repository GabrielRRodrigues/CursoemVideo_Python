#  Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e 
# o programa vai informar quantas cédulas de cada valor serão entregues.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 71 ', '\033[m'))
print('{} {:$^40} {}\n'.format('\033[7;1;32m', ' SIMULADOR DE CAIXA ELETRÔNICO ', '\033[m'))
 
while True:
    resto = 0
    valores = [200, 100, 50, 20, 10, 5, 2, 1]
    valores1 = []

    while True:
        valor = int(input('Valor do saque: R$ '))
        if valor > 0:
            break

    resto = valor

    for i in range(0, 8):
        valores1.append(resto // valores[i])
        resto = resto % valores[i]

        if valores1[i] != 0:
            print(f'Cédulas de R$ {valores[i]:3}: {valores1[i]:3}')

    #2, 5, 10, 20, 50, 100, 200
    while True:
        op = str(input('{} \nDeseja realizar outra transação? [S/N] \n→ '.format('-'*25))).strip()[0]

        if op in 'SsNn':
            break

    if op in 'Nn':
        break

    print('{}'.format('-'*25))
print('\n{}{:$^40}{}'.format('\033[7;32m', ' BANCO GSR AGRADECE ', '\033[m'))