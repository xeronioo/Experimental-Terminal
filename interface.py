from teste import adicionar, listar, alterar
from estoque import salvar_estoque
while True:
    print("opcao 1: adicionar item")
    print("opcao 2: listar item")
    print("opcao 3: alterar a quantidade")
    print("opcao 4: sair")
    op = input("digite sua escolha")

    if op =="1":
        nome = input("Nome do produto:")
        quantidade = input("Quantidade desejada:")
        adicionar(nome , quantidade)
    elif op == "2":
        listar()
    elif op == "3":
        nome = input("digite o nome do produto:") 
        quantidade = input("digite a nova quantidade desejada:") 
        alterar(nome , quantidade)      
    elif op == "4":
       salvar_estoque()
       break
      
