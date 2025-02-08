from ex115 import dado
from time import sleep
import json

CADASTROS = 'dados.json'


def linha(num=40):
    return f'{"—"*num}'


def cabecalho(msg, cor='31'):
    print(f'\033[{cor}m{linha()}')
    print(msg.center(40))
    print(f'{linha(40)}\033[m')


def menu(lista):
    cabecalho('MENU', '38;5;82')
    c = 1
    for key, value in lista.items():
        print(f'\t\t\033[34m{key} -\033[97m {value.__name__.replace("_", " ").title()}\033[m')
        c += 1
    print(f'\033[38;5;82m{linha()}\033[m')
    escolha = dado.leiaInt('\t\t\t Sua Opção → ')

    return escolha


def opcao_invalida():
    return '\t\033[31mOpção inválida. Tente novamente.\033[m'


def pessoas_cadastradas():
    cabecalho('PESSOAS CADASTRADAS', '94')
    # print(f'\n\033[94m{"—"*40}\n{"PESSOAS CADASTRADAS":^40}\n{"—"*40}\033[m')
    try:
        with open(CADASTROS, 'r') as arquivo:
            dados_carregados = json.load(arquivo)
        if not dados_carregados:
            print('❌ Nenhum cadastro encontrado!')
        else:
            for nome, idade in dados_carregados.items():
                print(f'  \033[97m{nome:<25}{idade:>5} {"ano" if idade == 1 else "anos"}\033[m')
            print(f'\033[94m{linha(40)}\033[m')
    except FileNotFoundError:
        print('❌ Arquivo de cadastros não encontrado!')
    except json.JSONDecodeError:
        print('❌ Erro ao carregar os dados. O arquivo pode estar corrompido oou vazio.')

    sleep(2)


def cadastrar_nova_pessoa(nome, idade):
    try:
        with open(CADASTROS, 'r') as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = {}

    dados[nome] = idade

    with open(CADASTROS, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f'\033[38;5;227m{linha(len(nome)+33)}\033[m')
    print(f'✅ Novo registro de {nome} adicionado')
    print(f'\033[38;5;227m{linha(len(nome)+33)}\033[m')


def sair():
    cabecalho("SAINDO... ATÉ LOGO ^^", '31')
    # print(f'\n\033[31m{"—"*40}\n{"SAINDO...":^40}\n{"ATÉ LOGO ^^":^40}\n{"—"*40}\033[m')
