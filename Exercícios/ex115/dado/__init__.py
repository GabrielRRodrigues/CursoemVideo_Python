from colorama import Back, Fore, init, Style
init()


def leiaInt(msg):
    valido = False
    while not valido:
        try:
            num = int(input(msg))
            valido = True
            return num
        except ValueError:
            print('\t\033[31mInválido. Tente novamente.\033[m')
        # except KeyboardInterrupt:
        #     print(f'\n{Back.RED}{Fore.LIGHTWHITE_EX}O usuário preferiu não digitar esse número!{Style.RESET_ALL}')
        #     return 0


def leiaFloat(msg):
    valido = False
    while not valido:
        try:
            num = float(input(msg).replace(',', '.'))
            valido = True
            return f'{num:.2f}'.replace('.', ',')
        except ValueError:
            print(f'{Back.RED}{Fore.LIGHTWHITE_EX}{"Digite um valor válido!":^30}{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'\n{Back.RED}{Fore.LIGHTWHITE_EX}O usuário preferiu não digitar esse número!{Style.RESET_ALL}')
            return f'{0:.2f}'
