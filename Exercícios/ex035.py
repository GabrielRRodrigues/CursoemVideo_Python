#Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo.

print('{} EX 36 {}'.format('>'*10, '<'*10))
print('\n{} ANALISADOR TRIÂNGULO {}\n'.format('='*2, '='*2))

r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))

if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print('='*28 + '\n\033[32mForma um triângulo!')
else:
    print('='*28 + '\n\033[31mNão forma um triângulo!')