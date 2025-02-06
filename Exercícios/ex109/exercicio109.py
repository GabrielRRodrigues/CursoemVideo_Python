# Modifique as funções que foram criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
# pela função moeda(), desenvolvida no desafio 108.

import moeda

print('{} EX 109 {}'.format('>'*14, '<'*14))
print('\n{} FORMATANDO MOEDAS {}\n'.format('='*8, '='*8))

preco = float(input('Digite o preço: → R$ '))

print(f'A metade de R$ {moeda.moeda(preco)}, é R$ {moeda.metade(preco, True)}')
print(f'O dobro de R$ {moeda.moeda(preco)} é R$ {moeda.dobro(preco, True)}')
print(f'Aumentando 25%, temos R$ {moeda.aumentar(preco, 25, True)}')
print(f'Diminuindo 20%, temos R$ {moeda.diminuir(preco, 20, True)}')