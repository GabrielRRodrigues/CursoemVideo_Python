'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

print('{} EX 40 {}\n'.format('>'*15, '<'*15))
print('{} {} MÉDIA SITUAÇÃO {} {}\n'.format('\033[7;38m', '→'*7, '←'*7, '\033[m'))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2

print('\n{}{}{}\n'.format('\033[7;38m', '↔'*28, '\033[m'))

if media < 5:
    print('Média: {:.1f} \nSituação: {}REPROVADO{}'.format(media, '\033[4;31m', '\033[m'))
elif media >= 7:
    print('Média: {:.1f} \nSituação: {}APROVADO{}'.format(media, '\033[4;32m', '\033[m'))
else:
    print('Média: {:.1f} \nSituação: {}RECUPERAÇÃO{}'.format(media, '\033[4;33m', '\033[m'))
