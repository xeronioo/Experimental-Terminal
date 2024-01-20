from estoque import carregar_estoque

estoque = carregar_estoque()


def adicionar(nome , quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
       estoque [nome] = quantidade


def listar():
    for item in estoque:
        print(f" Prod: {item} e Qtd: {estoque[item]}")


def alterar(nome , quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
    else:
        print("Produto nao localizado")


