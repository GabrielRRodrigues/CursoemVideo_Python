#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

from colorama import Back, Fore, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 104 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' VALIDANDO ENTRADA DE DADOS ', Fore.RESET, Back.RESET))

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('{}{}{:!^40}{}{}\n'.format(Back.RED, Fore.BLACK, ' Digite um número válido ', Fore.RESET, Back.RESET))
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')

print(f'Número digitado → {n} ←')