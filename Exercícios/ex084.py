# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 84 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.RED, Fore.BLACK, ' LISTA COMPOSTA E ANÁLISE DE DADOS ', Fore.RESET, Back.RESET))

pessoas = []
pessoa = []
pesos = []

while True:
    while True:
        nome = str(input('Digite um nome: ')).title()
        peso = float(input('Digite o peso(Kg): '))
        pessoa.append(nome)
        pessoa.append(peso)
        pessoas.append(pessoa[:])
        pesos.append(peso)
        pessoa.clear()

        resp = str(input('Deseja inserir outra pessoa? [S/N] →'))[0]
        print('-'*40)
        if resp in 'SsNn':
            break

    if resp in 'Nn':
        break

pesos = sorted(pesos)
print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'Pessoa(s) mais pesada(s) ({max(pesos)} Kg): ', end='')
for i in pessoas:
    if i[1] == max(pesos):
        print(f'[{i[0]}]', end=' ')

print(f'\nPessoa(s) mais leve(s) ({min(pesos)} Kg): ', end='')
for i in pessoas:
    if i[1] == min(pesos):
        print(f'[{i[0]}]', end=' ')
