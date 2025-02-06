def aumentar(n=0, tx=0,  formato=False):
    num = n + (n * tx/100)
    if formato:
        num = moeda(num)
    return num


def diminuir(n=0, tx=0, formato=False):
    num = n - (n * tx/100)
    if formato:
        num = moeda(num)
    return num


def dobro(n=0, formato=False):
    num = n*2
    if formato:
        num = moeda(num)
    return num


def metade(n=0, formato=False):
    num = n/2
    if formato:
        num = moeda(num)
    return num


def moeda(n):
    val = f'{n:.2f}'.replace('.', ',')
    return val

