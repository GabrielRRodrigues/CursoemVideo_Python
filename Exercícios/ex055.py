# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 55 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;32m', ' MAOR E MENOR ', '\033[m'))

lista = []

for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    lista.append(peso)

print('\nMaior peso: {:.2f} Kg \nMenor peso: {:.2f} Kg'.format(sorted(lista)[len(lista)-1], sorted(lista)[0]))
