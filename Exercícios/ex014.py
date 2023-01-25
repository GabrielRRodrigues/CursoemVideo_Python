#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

print('{} EX 14 {}\n'.format('>'*10, '<'*10))
print('{} CONVERSOR TEMPERATURA {}\n'.format('§'*2, '§'*2))

cel = float(input('Temperatura em Celsius: '))
print('{}\nTemperatura em Fahrenheit: {:.2f} ºF'.format('='*28, cel * 1.8 + 32))
