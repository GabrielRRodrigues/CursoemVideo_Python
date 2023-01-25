'''Faça um programa que leia uma frase pelo teclado e mostra:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição a última vez. '''

print('{} EX 26 {}'.format('>'*10, '<'*10))
print('\n{} PROCURANDO "A" {}\n'.format('▬'*3, '▬'*3))

frase = input('Digite uma frase: ').upper().strip()

print('{} \nQuantidade de \"A\": {}'.format('='*28, frase.count('A')))
print('Primeira aparição: {}'.format(frase.find('A')+1))
print('Última aparição: {}'.format(len(frase) - frase[::-1].find('A')))
