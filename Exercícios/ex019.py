'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''

from random import randint
print('{} EX 19 {}'.format('>'*10, '<'*10))
print('\n{} SORTEIO ALUNOS {}\n'.format('>'*6, '<'*6))
alunos = []

for i in range(4):
    a = input('Aluno: ')
    alunos.append(a)
print('{} \nAluno sorteado: \033[4;35m{}\033[m'.format('=' * 22, (alunos[randint(0, 3)])))
