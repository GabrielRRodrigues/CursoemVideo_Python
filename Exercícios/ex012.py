#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('{} EX 12 {}\n'.format('>' * 10, '<' * 10))
print('{} PREÇO C/ DESCONTO {}'.format('$' * 5, '$' * 5))

preco = float(input('\nPreço atual: R$ '))
desc = float(input('Desconto(%): '))
print('{}\nCom desconto de {} %: R$ {:.2f}'.format('=' * 30, desc,preco * (1 - desc / 100)))
