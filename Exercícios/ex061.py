# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos usando a estrurura while.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 61 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;35m', ' PROGRESSÃO ARITMÉTICA v2.0 ', '\033[m'))

termo = int(input('1º termo: '))
razao = int(input('Razão: '))
c = 2

print('{}'.format('↔'*28))
while c < 11:
    print('{:2}º termo: {:2}'.format(c, termo+razao))
    termo += razao
    c += 1