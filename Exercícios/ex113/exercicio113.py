# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from ex113.utilidades import dado

print('{} {} {}\n'.format(('>'*10), 'EX 113', ('<'*10)))

inteiro = dado.leiaInt('Digite um número Inteiro: ')
real = dado.leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
