#Desenvolva um programa que pergunte a distâncoa de uma viagem em KM.
#Calcule o proço da passagem, cobrando R$ 0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

print('{} EX 31 {}'.format('>'*10, '<'*10))
print('\n{} PREÇO VIAGEM {}\n'.format('='*7, '='*7))

dist = float(input('Distância em Km: '))

print('='*25 + '\nPassagem: R$ {:.2f}'.format(dist * 0.5 if dist <= 200 else dist * 0.45))