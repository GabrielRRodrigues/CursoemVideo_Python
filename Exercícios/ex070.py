# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato

print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 70 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;31m', ' ESTATÍSTICAS EM PRODUTOS ', '\033[m'))

total = menor = cont = 0
barato = ''
# produtos = []

while True:
    print('{}'.format('-'*20)) 
    nome = str(input('Nome: ')).strip().title()
    preco = float(input('Preço: R$ '))
    # produtos.append(preco)
    
    total += preco

    if barato == '':
        barato = nome
        menor = preco
    elif preco < menor:
        barato = nome
        menor = preco

    if preco > 1000:
        cont += 1
        
    while True:
        print('{}'.format('-'*20))
        op = str(input('Deseja continuar? [S/N] \n→ ')).strip()
        if op in 'SsNn':
            break
    if op in 'Nn':
        break

print('{}'.format('-'*20))
print(f'Total: R$ {total:.2f} \nProdutos acima de R$ 1000: {cont} \nProduto mais barato: {barato} (R$ {menor:.2f})')
    
