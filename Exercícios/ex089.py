# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 89 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' BOLETIM COM LISTAS COMPOSTAS ', Fore.RESET, Back.RESET))

boletim = []
aluno = []

while True:
    nome = str(input('Aluno: ')).title()
    aluno.append(nome)
    for i in range(1, 3):
        nota = float(input(f'Nota {i}: '))
        aluno.append(nota)
    aluno.append((aluno[1]+aluno[2])/2)

    boletim.append(aluno[:])
    aluno.clear()
    while True:
        resp = str(input('Falta algum aluno? [S/N] → '))[0]
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break
    print('-' * 35)

print('\n{:-^30}'.format('BOLETIM'))
for num, i in enumerate(boletim):
    print(f'Nº {num+1:^2}'
          f'\nAluno(a): {i[0]}'
          f'\nMédia: {i[3]:.2f}')
    print('-'*30)

# resp = 'S'
while True:
    while True:
        resp = str(input('Deseja ver a nota de algum? [S/N] → '))[0]
        if resp in 'SsNn':
            break

    if resp in 'Nn':
        break
    notas_aluno = int(input('Qual o número do aluno(a)? → '))

    print('-'*30)
    print(f'Aluno(a): {boletim[notas_aluno-1][0]}')
    for i in range(1, 3):
        print(f'Nota {i}: {boletim[notas_aluno-1][i]:.2f}')
    print(f'Média: {boletim[notas_aluno-1][3]:.2f}')
    print('-'*30)
