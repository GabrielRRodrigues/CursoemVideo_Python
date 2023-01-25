# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# - a média de idade do grupo,
# - qual é o nome do homem mais velho
# - quantas mulheres têm menos de 20 anos.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 52 ', '\033[m'))
print('{}{:↔^40}{}'.format('\033[7;1;36m', ' ANALISADOR COMPLETO ', '\033[m'))

media = float(0)
hidade = 0
hnome = ''
contMulher = 0

for i in range(1, 5):
    print('\nDados da {}ª pessoa:'.format(i))
    nome = input('Nome: ').title().strip()
    idade = int(input('Idade: '))
    media += idade
    sexo = input('Sexo (m/f): ').lower()

    if sexo == 'm':
        if i == 1:
            hidade = idade
            hnome = nome
        if idade > hidade:
            hidade = idade
            hnome = nome

    if sexo == 'f' and idade < 20:
        contMulher += 1

print('\nMédia das idades: {:.1f} anos'.format(media / 4))
print('Homem mais velho: {} \nMulheres com menos 20 anos: {}'.format((hnome + ' com {} anos'.format(hidade)) if hnome != '' else '--', contMulher))
