'''Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal
3 para hexadecimal.'''

print('{} EX 37 {}\n'.format('>'*15, '<'*15))
print('{} {} CONVERSÃO BASE {} {}\n'.format('\033[7;35m', '→'*7, '←'*7, '\033[m'))

num = int(input('Digite um número inteiro: '))

print('\n{}{}{}\n\n1) Binário \n2) Octal \n3) Hexadecimal \n\n{}{}{}'.format('\033[7;35m', '='*20, '\033[m', '\033[7;35m', '='*20, '\033[m'))
op = int(input('Digite o número da opção desejada: '))
print('{}{}{}\n'.format('\033[7;35m', '='*20, "\033[m"))

if op == 1:
    print('Em Binário: \n{} = {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('Em Octal: \n{} = {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('Em Hexadecimal: \n{} = {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!!')