#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímitros.

print('{} {} {}\n'.format('>' * 10, 'EX 08', '<' * 10))
print('\033[7;33m{} CONVERSOR DE MEDIDAS {}\033[m\n'.format('='*2, '='*2))
metros = int(input('Digite um valor: '))

print('\033[7;33m{}\033[m\nMetros: {} m\nCentímetros: {} cm\nMilímitros: {} mm'.format('='*27, metros, metros * 100, metros * 1000))
