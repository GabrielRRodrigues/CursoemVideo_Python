'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('{} EX 36 {}'.format('>'*15, '<'*15))
print('\n\033[7;30;44m{} EMPRÉSTIMO BANCÁRIO {}\033[m\n'.format('='*7, '='*7))

sal = float(input('Salário do comprador: R$ '))
valor = float(input('Valor da casa: R$ '))
anos = int(input('Tempo para pagamento (anos): '))
prest = valor / (anos * 12)

print('\n' + '='*28 + '\n')
if prest > sal * 0.3:
    print('\033[7;31mEmpréstimo negado!!\033[m')
else:
    print('\033[7;32mEmpréstimo aprovado!!\033[m \nParcelas: {} \nValor: R$ {:.2f}'.format(anos*12, prest))
