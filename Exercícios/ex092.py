# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from colorama import init, Fore, Back
from datetime import datetime

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 92 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' CADASTRO DE TRABALHADOR EM PYTHON ', Fore.RESET, Back.RESET))

trabalhador = {'Nome': str(input('Nome: ')).title(),
               'Idade': datetime.today().year - int(input('Ano de nascimento: ')),
               'CTPS': int(input('CTPS (0 se não possuir): '))}

if trabalhador['CTPS'] != 0:
    trabalhador['Ano_Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Idade_Aposentadoria'] = trabalhador['Ano_Contratação']+35-(datetime.now().year-trabalhador['Idade'])

print('-' * 35)

for k, v in trabalhador.items():
    print(f'→ {k}: {v}')
