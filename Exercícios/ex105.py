#   Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#   e vai retornar um dicionário com as seguintes informações:
#   – Quantidade de notas
#       – A maior nota
#           – A menor nota
#               – A média da turma
#                   – A situação (opcional)

from colorama import Back, Fore, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 105 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.YELLOW, Fore.BLACK, ' ANÁLISE/ CRIAÇÃO DE DICIONÁRIOS ', Fore.RESET, Back.RESET))


def notas(*num, sit=False):
    r = dict()

    r['Quantidade'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num) / len(num)

    if sit:
        r['Situação'] = 'BOA' if r['Média'] >= 7 else 'RAZOÁVEL' if r['Média'] >=5  else 'RUIM'

    return r


valores = list(map(float, input('Digite as notas (separadas por espaço): ').split()))

sit = input('Exibir Situação? (S/N) → ').strip().upper() == 'S'

resp = notas(*valores, sit=sit)
print(resp)
