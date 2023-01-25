# Crie um algoritmo que leia um número e mostre o seu dobro,triplo e a raiz quadrada.
print('{} {} {}\n'.format('>' * 10, 'EX 06', '<' * 10))
print('{}{} 2x, 3x, √ {}{}\n'.format('\033[7;31;40m', '+'*8, '+'*8, '\033[m'))

num = int(input('Digite um número: '))
print('{}\nDobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format('='*15, num * 2, num * 3, num ** (1 / 2)))
