# Faça um programa que leia o sexo de uma pesso, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça digitação novamente até ter um valor correto.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 57 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;36m', ' VALIDAÇÃO DE DADOS ', '\033[m'))

sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('\nResposta inválida, tente novamente. \nDigite o sexo (M/F): ')).strip().upper()[0]

print('\nResposta arquivada!')
