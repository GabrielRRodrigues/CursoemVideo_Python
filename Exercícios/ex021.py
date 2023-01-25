#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import playsound
print('{} EX 21 {}'.format('>'*10, '<'*10))
print('\n{} REPRODUÇÃO MP3 {}\n'.format('♫'*4, '♫'*4))

print('Reproduzindo: Super Mario Bros Theme ♪♪♪')
playsound.playsound('Super Mario Bros.mp3')