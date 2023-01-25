# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jgador vai tantar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint
print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 58 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;32m', ' JOGO DE ADIVINHAÇÃO ', '\033[m'))

pc = randint(0, 10)
tentativa = 1

num = int(input('Vou pensar em um número entre 0 e 10, tente adivinhar: '))
while num != pc:
    num = int(input('\nResposta errada :( \nTente novamente: '))
    tentativa += 1

print('{} \nVocê ganhou!! :\') \nEu pensei mesmo no número {} \nTentativas: {}'.format('↔'*25, pc, tentativa))