# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 90 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.CYAN, Fore.BLACK, ' DICIONÁRIO EM PYTHON ', Fore.RESET, Back.RESET))

aluno = {}
nome = str(input('Nome: ')).title()
media = float(input('Média: '))

aluno['Nome'] = nome
aluno['Média'] = media
aluno['Situação'] = ('Aprovado' if aluno['Média'] >= 5 else 'Reprovado')

print('-'*30)
for k, v in aluno.items():
    print(f'{k}: {v}')
print()


