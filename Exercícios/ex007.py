
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print('{} {} {}\n'.format('>' * 10, 'EX 07', '<' * 10))
print('\033[7;34;40m{} MÉDIA DE NOTA {}\033[m\n'.format('%'*6, '%'*6))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1+ nota2) / 2

print('{}\nMédia: {}{:.1f}{}'.format('='*28,'\033[1;31m' if media <5 else '\033[1;34m' ,media, '\033[m'))
