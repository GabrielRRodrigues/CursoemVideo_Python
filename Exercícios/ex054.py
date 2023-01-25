# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 53 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;36m', ' GRUPO DA MAIORIDADE ', '\033[m'))

atual = date.today().year
contMaior = 0
contMenor = 0
cores = {'limpa': '\033[m',
         'verde': '\033[4;32m',
         'vermelho': '\033[4;31m'}

for i in range(1, 8):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(i)))
    if atual - nasc >= 21:
        contMaior += 1
    else:
        contMenor += 1

print('\n{}{}{} {}'.format(cores['verde'], contMaior, cores['limpa'], 'é maior' if contMaior == 1 else 'são maiores'), end='')
print(' {}{}{} {}'.format(cores['vermelho'], contMenor, cores['limpa'], 'é menor' if contMenor == 1 else 'são menores'))


