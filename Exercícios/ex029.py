#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.


print('{} EX 29 {}'.format('>'*10, '<'*10))
print('\n{} RADAR {}\n'.format('='*10, '='*10))

vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    print('{} \nVocê foi multado por excesso de velocidade! \nValor da multa: R$ {:.2f}'.format('='*25, (vel-80)*7))
