def aumentar(n, tx):
    return n + (n * tx/100)


def diminuir(n, tx):
    return n - (n * tx/100)


def dobro(n):
    return n*2


def metade(n):
    return n/2


def moeda(n):
    val = f'{n:.2f}'.replace('.', ',')
    return val