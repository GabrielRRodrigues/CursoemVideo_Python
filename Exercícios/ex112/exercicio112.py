# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from ex112.utilidades import moeda
from ex112.utilidades import dado

print('{} EX 28 {}'.format('>'*14, '<'*14))
print('\n{} ENTRADA DE DADOS MONETÁRIOS {}\n'.format('='*3, '='*3))

preco = dado.leiaDinheiro('Digite um preço: R$ ')
aumento = int(input('Digite o percentual de aumento: '))
diminuicao = int(input('Digite o percentual de redução: '))
moeda.resumo(preco, aumento, diminuicao)

