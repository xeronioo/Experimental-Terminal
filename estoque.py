import json

def carregar_estoque():
    try:
        with open('Estoque.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return {}

def salvar_estoque(estoque):
    with open('Estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo , indent=2)
