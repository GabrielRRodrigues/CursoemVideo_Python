# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), # diminuir(), dobro() e metade().
# Faça também um programa que importe ess módulo e use algumas dessa funções.

import moeda

preco = float(input('Digite o preço: → R$ '))
print(f'A metade de R$ {preco}, é R$ {moeda.metade(preco)}')
print(f'O dobro de R$ {preco} é R$ {moeda.dobro(preco)}')
print(f'Aumentando 25%, temos R$ {moeda.aumentar(preco, 25)}')
print(f'Diminuindo 20%, temos R$ {moeda.diminuir(preco, 20)}')