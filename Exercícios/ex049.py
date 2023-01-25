
print('{}{:↔^40}{}\n'.format('\033[7m', ' EX 49 ', '\033[m'))
print('{}{:↔^40}{}\n'.format('\033[7;1;34m', ' TABUADA ', '\033[m'))

num = int(input('Digite um número: '))

print('\n{}\n\033[1mTABUADA DO {}{}{}\n'.format('='*20, '\033[1;4;32m', num, '\033[m'))
for i in range(1, 11):
    print('{} × {:2} = {}'.format(num, i, num*i))

print('='*20)