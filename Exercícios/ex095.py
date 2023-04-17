# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

from colorama import init, Fore, Back
from time import sleep

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 95 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' APRIMORANDO OS DICIONÁRIOS ', Fore.RESET, Back.RESET))

jogadores = []

while True:
    dados = {'Nome': str(input('Nome: ')).title(),
             'Gols': []}

    partidas = int(input('Partidas jogadas: '))
    for i in range(1, partidas + 1):
        dados['Gols'].append(int(input(f'   → Gols no {i}ºjogo: ')))

    dados['total'] = sum(dados['Gols'])

    jogadores.append(dados.copy())
    dados.clear()

    print('-' * 30)
    while True:
        resp = str(input('Outro jogador? [S/N] → ')).upper()[0]
        if resp in 'SN':
            if resp == 'S':
                print('-' * 30)
            break
        print(f'{Fore.RED}ERRO!!{Fore.RESET} Responda "S" para SIM ou "N" para NÃO!')
    if resp in 'Nn':
        print(f'\n{"-" * 50}')
        break
print(f'{Fore.GREEN}|{"cod":^5}|{"Nome":^18}|{"Gols":^14}|{"total":^8}|{Fore.RESET}')
print('-' * 50)
for pos, jogador in enumerate(jogadores, 1):
    print(f'|{pos:^5}|{jogador["Nome"]:<18}|{", ".join(map(str, jogador["Gols"])):^14}|{jogador["total"]:^8}|')
print(f'{"-" * 50}\n')

while True:
    while True:
        resp = int(input('Mostrar detalhes de qual jogador? (0 para parar) → '))
        if resp < 0 or resp > len(jogadores):
            print(f'ERRO!! Não existe jogador {Fore.RED}{resp}{Fore.RESET}!')
        else:
            break
    if resp == 0:
        print(f'{"-" * 30}\nEncerrando...')
        sleep(2)
        break

    print('-' * 30)
    print(f'Dados do jogador {Fore.GREEN}{jogadores[resp-1]["Nome"]}{Fore.RESET}:')
    for pos, jogo in enumerate(jogadores[resp-1]['Gols'], 1):
        print(f'    → No {pos}º jogo fez {jogo} gol(s)')
    print('-' * 30)
