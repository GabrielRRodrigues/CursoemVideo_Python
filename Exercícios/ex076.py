# Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

from colorama import Fore, Back, init

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 76 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' Lista de Preços ', Fore.RESET, Back.RESET))


print('{}{}{:×^50}{}{}'.format(Back.CYAN,Fore.BLACK, '', Fore.RESET, Back.RESET),
      '\n{}{}{:^50}{}{}'.format(Back.BLACK, Fore.CYAN, 'LOJINHA', Fore.RESET, Back.RESET),
      '\n{}{}{:×^50}{}{}'.format(Back.CYAN,Fore.BLACK, '', Fore.RESET, Back.RESET))

dados = ('Mouse', 25.0,
         'Mouse Gamer', 78.0,
         'Teclado', 29.99,
         'Teclado Gamer', 92.99,
         'Pen Drive 16 GB', 22.0,
         'Pen Drive 32 GB', 38.2,
         'Pen Drive 64 GB', 71.49,
         'Fone de ouvido', 12.99,
         'Head Gamer', 71.91,
         'Fone Bluetooth 5.3', 114.99,
         'Smartwatch', 274.59,
         'Carregador Micro USB', 14.99,
         'Carregador USB C', 19.99,
         'Carregador Lightning', 29.99)

for i in range(0, len(dados), 2):
    print(f'{dados[i]:_<38} {Fore.GREEN}R${Fore.CYAN} {float(dados[i+1]):7.2f}{Fore.RESET}')
    # .format(dados[i], Fore.GREEN, Fore.CYAN, float(dados[i+1]), Fore.RESET))

print('{}{}{:×^50}{}{}'.format(Back.CYAN,Fore.BLACK, '', Fore.RESET, Back.RESET))

