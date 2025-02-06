# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

print('{} EX 110 {}'.format('>'*10, '<'*10))

preco = float(input('Digite o preço: → R$ '))
aumento = int(input('Digite o percentual de aumento: '))
diminuicao = int(input('Digite o percentual de redução: '))
moeda.resumo(preco, aumento, diminuicao)