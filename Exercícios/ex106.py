#   Faça um mini-sistema que utilize o Interactive Help do Python.
#   O usuário vai digitar o comando e o manual vai aparecer.
#   Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from colorama import Back, Fore, init, Style

init()

print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 106 ', Fore.RESET, Back.RESET))
# print('{}{}{:×^40}{}{}\n'.format(Back.RED, Fore.BLACK, ' INTERACTIVE HELPING SYSTEM IN PYTHON ', Fore.RESET, Back.RESET))

def assistente(comando):
    cabecalho(f'→ Acessando o manual do comando {comando.upper()} ←', 'BLUE')
    print(f'{Back.LIGHTWHITE_EX}{Fore.BLACK}', end='')
    help(comando)
    print(f'{Style.RESET_ALL}')


def cabecalho(txt, cor_f = ''):
    cor_fundo = getattr(Back, cor_f.upper(), '')
    tam = len(txt) + 15
    print('{}{}{:=^{}}{}'.format(cor_fundo, Fore.LIGHTWHITE_EX, '', tam, Back.RESET))
    print('{}{:^{}}{}'.format(cor_fundo, txt, tam, Back.RESET))
    print('{}{:=^{}}{}'.format(cor_fundo, '', tam, Style.RESET_ALL))


comando = ''
while True:
    cabecalho('→ SISTEMA DE AJUDA PyHELP ←', 'RED')
    comando = str(input('\nFunção ou Biblioteca → ')).strip().lower()
    if comando == 'fim':
        break
    else:
        assistente(comando)


cabecalho('    ATÉ LOGO! ^^ ', 'LIGHTGREEN_EX')
