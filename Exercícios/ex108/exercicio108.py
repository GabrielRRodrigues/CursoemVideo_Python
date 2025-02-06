# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado. (00,00)

import moeda

print('{} EX 108 {}'.format('>'*14, '<'*14))
print('\n{} FORMATANDO MOEDAS {}\n'.format('='*8, '='*8))

preco = float(input('Digite o preço: → R$ '))
print(f'A metade de R$ {moeda.moeda(preco)}, é R$ {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de R$ {moeda.moeda(preco)} é R$ {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 25%, temos R$ {moeda.moeda(moeda.aumentar(preco, 25))}')
print(f'Diminuindo 20%, temos R$ {moeda.moeda(moeda.diminuir(preco, 20))}')