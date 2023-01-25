'''Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
por Km rodado. '''

print('{} EX 15 {}'.format('>'*10, '<'*10))
print('\n{} ALUGUEL CARRO {}\n'.format('>'*6, '<'*6))

dias = int(input('Dias alugados: '))
km = float(input('Km rodados: '))

total = 60 * dias + km * 0.15
print('{} \nCarro: R$ {:.2f} \nPor KM: R$ {:.2f} \n{} \nTOTAL: R$ {:.2f}'.format('='*20, 60*dias, km*0.15, '='*15, total))
