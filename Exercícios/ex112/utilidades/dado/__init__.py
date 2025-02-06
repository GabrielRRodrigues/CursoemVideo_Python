def leiaDinheiro(msg):
    while True:
        txt = input(msg).replace(',', '.').strip()
        if not txt:
            print('\033[0;31m ERRO! Nenhum preço informado!\033[m')
        elif any (char.isalpha() for char in txt):
            print(f'\033[0;31m ERRO! "{txt}" não é um preço válido!\033[m')
        elif txt.count('.') > 1 or not txt.replace('.', ''):
            print(f'\033[0;31m ERRO! "{txt}" não é um preço válido!\033[m')
        else:
            valor = float(txt)
            if valor >= 0:
                return valor
            else:
                print(f'\033[0;31m ERRO! "Preço não pode ser negativo!\033[m')
