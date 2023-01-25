#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro o último nome separadamente.


print('{} EX 27 {}'.format('>'*10, '<'*10))
print('\n{} NOME - SOBRENOME {}\n'.format('■'*4, '■'*4))

nome = input('Nome completo: ').title()

print('{} \nPrimeiro nome: {} \nÚltimo Nome: {}'.format('=' * 28, nome.split()[0], nome.split()[::-1][0]))
