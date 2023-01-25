# Melhore o DESAFIO 061, perguntando se ele querr mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 61 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;35m', ' PROGRESSÃO ARITMÉTICA v3.0 ', '\033[m'))

termo = int(input('1º termo: '))
razao = int(input('Razão: '))
op = 'S'
cont = 2
c = 2

while op == 'S':
    if c != 2:
        quant = int(input('Quantos termos? '))
        i = 0
        print('{}'.format('↔' * 28))

        while i < quant:
            print('{}º termo: {:2}'.format(cont, termo + razao))
            termo += razao
            cont += 1
            i += 1

    if c == 2:
        print('{}'.format('↔' * 28))

        while c < 11:
            print('{:2}º termo: {:2}'.format(cont, termo+razao))
            termo += razao
            c += 1
            cont += 1

    op = input('\nQuer mais alguns termos? [S/N] ').strip().upper()

