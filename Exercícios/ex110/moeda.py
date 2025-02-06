def aumentar(n, perc=10, valor=False):
    num = n * (1 + perc / 100)
    if valor:
        num = moeda(num)
    return num


def diminuir(n, perc=10, valor=False):
    num = n * (1 - perc / 100)
    if valor:
        num = moeda(num)
    return num


def dobro(n, valor=False):
    num = n*2
    if valor:
        num = moeda(num)
    return num


def metade(n, valor=False):
    num = n/2
    if valor:
        num = moeda(num)
    return num


def moeda(n, moeda='R$ '):
    val = f'{moeda} {n:.2f}'.replace('.', ',')
    return val


def resumo(n, aum, dim):
    print(f'\n{"~"*35}\n{"RESUMO DO VALOR":^35}\n{"~"*35}')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum:02}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim:02}% de redução: \t{diminuir(n, dim, True)}')
    print(f'{"~"*35}')
