#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('{} EX 10 {}\n'.format('>' * 10, '<' * 10))
print('{} COMPRA DE DÓLARES {}\n'.format('$' * 5, '$' * 5))
real = float(input('Digite quanto você tem na carteira: R$ '))

print('{}\nCompra: US$ {:.2f}\nTroco: R$ {:.2f}'.format('='*28, real // 3.27, real % 3.27))