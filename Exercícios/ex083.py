    # Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
    # Seu aplicativo deverá analisar se a expressão passada está com os
    # parênteses abertos e fechados na ordem correta.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 83 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.BLUE, Fore.BLACK, ' VALIDANDO EXPRESSÕES MATEMÁTICAS ', Fore.RESET, Back.RESET))

expressao = input('Digite uma expressão com parênteses: ')
pilha = []

for c in expressao:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print(f'Expressão {Back.GREEN}{Fore.BLACK}válida!!{Back.RESET}')
else:
    print(f'Expressão {Back.RED}{Fore.BLACK}inválida!!{Back.RESET}')

