'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random
#from random import shuffle
print('{} EX 20 {}'.format('>'*10, '<'*10))
print('\n{} ORDEM APRESENTAÇÃO {}\n'.format('>'*4, '<'*4))

alunos = []
for i in range(4):
    aluno = input('Aluno: ')
    alunos.append(aluno)

random.shuffle(alunos)

print('{} \nOrdem do sorteio: {}'.format('='*28, ', '.join(alunos)))

