""" Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m²."""

print('{} EX 11 {}\n'.format('>' * 10, '<' * 10))

print('{} ÁREA E TINTA {}\n\nEntre com os dados da parede, \nem metros:\n'.format('=' * 7, '=' * 7))
larg = float(input('Largura: '))
alt = float(input('Altura: '))

print('{}\nÁrea: {:.3f} m²\nTinta necessária: {:.1f} L'.format('=' * 18, larg * alt, larg * alt / 2))

