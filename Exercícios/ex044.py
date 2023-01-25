'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''

print('{} EX 44 {}\n'.format('>'*15, '<'*15))
print('{} {} GERENCIADOR DE PAGAMENTOS {} {}\n'.format('\033[7;31m', '→'*7, '←'*7, '\033[m'))

preco = float(input('Total dos produtos: R$ '))
parcela = int(2)

print('\n{}{:=^40}{}\n'.format('\033[7;31m', ' FORMA DE PAGAMENTO ', '\033[m'))
print('1 ) À vista dinheiro/cheque \n2 ) À vista no cartão \n3 ) Em até 2x no cartão \n4 ) 3x ou mais no cartão\n')
print('{}{}{}'.format('\033[7;31m', '='*40, '\033[m'))

op = int(input('Digite o número da opção desejada: '))

if op == 1:
    preco = preco * 0.9
elif op == 2:
    preco = preco * 0.95
elif op ==4:
    preco = preco * 1.2
    parcela = int(input('Quantas parcelas: '))

print('{}{}{}'.format('\033[7;31m', '='*40, '\033[m'))

if 0 < op < 5:
    if 2 < op <= 4:
        print('\n{} parcelas de: R$ {:.2f} \nTotal à pagar: R$ {:.2f}'.format(parcela, preco/parcela, preco))
    else:
        print('\nTotal à pagar: R$ {:.2f}'.format(preco))
else:
    print('{}{:^40}{}'.format('\n\033[1;31m', 'Opção inválida!!', '\033[m'))


