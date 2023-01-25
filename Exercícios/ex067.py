# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 67 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;36m', ' TABUADA v3.0 ', '\033[m'))

i = 1

while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print('↔'*25)

    while True:
        if i > 10:
            i = 1
            print('↔'*25)
            break
        print(f'{num:2} × {i:2} = {num*i:2}')
        i += 1