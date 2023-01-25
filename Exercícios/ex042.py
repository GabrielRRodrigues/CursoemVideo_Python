'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''

print('{} EX 42 {}\n'.format('>'*15, '<'*15))
print('{} {} ANALISADOR DE TRIÂNGULOS 2 {} {}\n'.format('\033[7;35m', '→'*7, '←'*7, '\033[m'))

r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))

print('\n{}{}{} \n'.format('\033[7;35m', '↔'*28, '\033[m'))

if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    if r1 == r2 and r2 == r3: # r1 == r2 == r3
        print('Triângulo: {}EQUILÁTERO{}'.format('\033[4;35m', '\033[m'))
    elif r1 != r2 and r2 != r3 and r1 != r3: # r1 != r2 != r3 != r1
        print('Triângulo: {}ESCALENO{}'.format('\033[4;35m', '\033[m'))
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Triângulo: {}ISÓCELES{}'.format('\033[4;35m', '\033[m'))
else:
    print('\033[31mNão forma um triângulo!')