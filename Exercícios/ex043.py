'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

print('{} EX 43 {}\n'.format('>'*15, '<'*15))
print('{} {} IMC {} {}\n'.format('\033[7;33;40m', '→'*7, '←'*7, '\033[m'))

peso = float(input('Peso(Kg): '))
altura = float(input('Altura(m): '))
imc = peso / (altura ** 2)

print('\n{}{}{}\n'.format('\033[7;33;40m', '↔'*25, '\033[m'))
if imc < 18.5:
    print('IMC: {:.1f} \nStatus: {}ABAIXO DO PESO{}'.format(imc, '\033[4m', '\033[m'))
elif 18.5 <= imc < 25:
    print('IMC: {:.1f} \nStatus: {}PESO IDEAL{}'.format(imc, '\033[4m', '\033[m'))
elif 25 <= imc < 30:
    print('IMC: {:.1f} \nStatus: {}SOBREPESO{}'.format(imc, '\033[4m', '\033[m'))
elif 30 <= imc < 40:
    print('IMC: {:.1f} \nStatus: {}OBESIDADE{}'.format(imc, '\033[4m', '\033[m'))
else:
    print('IMC: {:.1f} \nStatus: {}OBESIDADE MÓRBIDA{}'.format(imc, '\033[4m', '\033[m'))
