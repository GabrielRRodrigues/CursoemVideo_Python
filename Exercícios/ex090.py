# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 90 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.CYAN, Fore.BLACK, ' DICIONÁRIO EM PYTHON ', Fore.RESET, Back.RESET))

aluno = {'Nome': str(input('Nome: ')).title(), 'Média': float(input('Média: '))}

aluno['Situação'] = ('Aprovado' if aluno['Média'] >= 7 else ('Recuperação' if aluno['Média'] >= 5 else 'Reprovado'))

print('-'*30)
for k, v in aluno.items():
    print(f'{k}: {v}')
print()


