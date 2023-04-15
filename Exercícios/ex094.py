# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

from colorama import init, Fore, Back

init()
print('{}{}{:↔^40}{}{}\n'.format(Back.WHITE, Fore.BLACK, ' EX 94 ', Fore.RESET, Back.RESET))
print('{}{}{:×^40}{}{}\n'.format(Back.RED, Fore.BLACK, ' UNINDO DICIONÁRIOS E LISTAS ', Fore.RESET, Back.RESET))

dados = {}
pessoas = []
mulheres = []
idosos = []
media = 0

while True:
    dados['nome'] = str(input('Nome: ')).title()

    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).title()[0]
        if dados['sexo'] in 'FM':
            break
        print('ERRO!! Por favor, responda M ou F.')

    dados['idade'] = int(input('Idade: '))

    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    media += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()

    while True:
        resp = str(input('Mais alguém? [S/N] → ')).title()[0]
        if resp in 'SsNn':
            print('-' * 35)
            break
        print('ERRO!! Por favor, digite S ou N.')
    if resp in 'Nn':
        break

media = media/len(pessoas)

print(f'Foram cadastradas: {len(pessoas)} pessoas'
      f'\nMédia de idades: {media:.2f} anos'
      f'\nMulheres: {", ".join(mulheres)}'
      f'\nPessoas acima da média: {", ".join([pessoa["nome"] for pessoa in pessoas if pessoa["idade"] > media])}')
