# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
# e mantenha tudo funcionando.

from ex111.utilidades import moeda

print('{} EX 111 {}'.format('>'*10, '<'*10))

preco = float(input('Digite o preço: → R$ '))
aumento = int(input('Digite o percentual de aumento: '))
diminuicao = int(input('Digite o percentual de redução: '))
moeda.resumo(preco, aumento, diminuicao)