
import requests

print('{} {} {}\n'.format(('>'*10), 'EX 114', ('<'*10)))

url = 'http://www.pudim.com.br'
try:
    resposta = requests.get(url, timeout=5)
    if resposta.status_code == 200:
        print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')
except:
    print('\033[0;31mO site Pudim não está acessível no momento.')

