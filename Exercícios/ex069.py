# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres têm menos de 20 anos

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 69 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;34m', ' ANÁLISE DE DADOS DO GRUPO ', '\033[m'))

mulhermenor20 = homens = pessoamais18 = 0
while True:
    idade = int(input('{} \nCadastro \n{} \nIdade: '.format('-'*15, '-'*15)))

    while True:
        sexo = str(input('Sexo [M/F]: ')).strip()
        if sexo in 'FfMm':
            break
    if idade > 18:
        pessoamais18 += 1

    if sexo in 'Ff':
        if idade < 20:
            mulhermenor20 += 1
    else:
        homens += 1
    print('-' * 15)

    while True:
        op = str(input('Deseja continuar? [S/N] \n→ ')).strip()
        if op in 'SsNn':
            break

    if op in 'Nn':
        break

print('{}'.format('-'*20), f'\nPessoas maiores de 18 anos: {pessoamais18} \nHomens cadastrados: {homens} \nMulheres com menos de 20: {mulhermenor20}')



