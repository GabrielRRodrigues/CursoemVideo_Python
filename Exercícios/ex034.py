#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Paea salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

print('{} EX 34 {}'.format('>'*10, '<'*10))
print('\n{} AUMENTO SALÁRIO {}\n'.format('='*7, '='*7))

sal = float(input('Salário: R$ '))

print('='*28 + '\nAumento: R$ {:.2f}'.format(sal*0.15 if sal <= 1250 else sal*0.1))
print('Novo Salário: R$ {:.2f}'.format(sal*1.15 if sal <= 1250 else sal*1.1))
