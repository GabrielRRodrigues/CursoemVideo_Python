# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 93 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.GREEN, Fore.BLACK, ' CADASTRO DE JOGADOR DE FUTEBOL ', Fore.RESET, Back.RESET))

jogador = {'Nome': str(input('Nome: ')).title(),
           'Gols': []}

partidas = int(input('Partidas jogadas: '))
for i in range(1, partidas + 1):
    jogador['Gols'].append(int(input(f'   Gols no {i}ºjogo: ')))

total = 0
for a in range(0, partidas):
    total += jogador['Gols'][a]

jogador['total'] = total

print('-' * 30)
print(jogador)


print('-' * 30)
for k, v in jogador.items():
    print(f'O campo "{k}" tem o valor "{v}"')


print('-' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas:')
for pos, c in enumerate(jogador['Gols']):
    print(f'  → Na {pos+1}ª partida: {c:2} gol(s)')
print(f'Foi um total de {jogador["total"]} gols.')
