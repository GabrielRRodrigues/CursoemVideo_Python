def aumentar(n, perc=10, formato=False):
    num = n * (1 + perc / 100)
    return num if formato is False else moeda(num)


def diminuir(n, perc=10, formato=False):
    num = n * (1 - perc / 100)
    return num if formato is False else moeda(num)


def dobro(n, formato=False):
    num = n*2
    return num if formato is False else moeda(num)


def metade(n, formato=False):
    num = n/2
    return num if formato is False else moeda(num)


def moeda(n, moeda='R$ '):
    valor = f'{moeda} {n:8.2f}'.replace('.', ',')
    return valor


def resumo(n, aum, dim):
    print(f'\n{"~"*35}\n{"RESUMO DO VALOR":^35}\n{"~"*35}')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum:02} % de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim:02} % de redução: \t{diminuir(n, dim, True)}')
    print(f'{"~"*35}')
