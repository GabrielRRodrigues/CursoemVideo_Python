from ex115 import menu, dado

opcoes = {
        1: menu.pessoas_cadastradas,
        2: menu.cadastrar_nova_pessoa,
        3: menu.sair
}

while True:
    escolha = menu.menu(opcoes)
    try:
        if escolha == 2:
            menu.cabecalho('NOVO CADASTRO', '38;5;227')
            nome = str(input('Digite o nome: ').title())
            idade = dado.leiaInt('Digite a idade: ')
            opcoes.get(escolha)(nome, idade)
        else:
            opcoes.get(escolha, menu.opcao_invalida)()
        if escolha == 3:
            break
    except KeyboardInterrupt:
        print('\n')
        opcoes.get(3)()
        break