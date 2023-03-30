# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

from colorama import init, Back, Fore

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 73 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' Brasileirão ', Fore.RESET, Back.RESET))

classificacao = ('Palmeiras', 'Atlético Mineiro', 'Fortaleza', 'Red Bull Bragantino', 'Flamengo',
                 'Athletico Paranaense', 'Ceará', 'Corinthians', 'Internacional', 'Juventude', 'Santos',
                 'Bahia', 'São Paulo', 'Fluminense', 'América Mineiro', 'Sport Recife', 'Cuiabá', 'Grêmio',
                 'Chapecoense', 'América de Natal')

print('A) TOP 5: ')
for time in range(0,5):
    print(f'{time+1}º {Fore.GREEN}{classificacao[time]}{Fore.RESET}')

print('\nB) Últimos 4:')
for time in range(16, 20):
    print(f'{time+1}º {Fore.RED}{classificacao[time]}{Fore.RESET}')

print('\nC) Ordem alfabética: ')
for pos, time in enumerate(sorted(classificacao)):
    print(f'{pos+1:2} {time} ')

print(f'\nD) Chapecoense: {Fore.BLUE}{classificacao.index("Chapecoense")+1}º{Fore.RESET}')
