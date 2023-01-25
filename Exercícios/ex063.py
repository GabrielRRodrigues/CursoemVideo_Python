# Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros
# elementos de uma Sequência de Fibonacci.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 61 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;35m', ' FIBONACCI ', '\033[m'))

n = int(input('Informe um número: '))
n1 = n2 = i = 1
f = [n1]

while i <= n-1:
    n2 += n1
    f.append(n1)
    n1 += n2
    f.append(n2)
    i += 1

print(*f[:n])





