import json
from tabulate import tabulate


def salvar_estoque(produtos, arquivo="estoque.json"):
    with open(arquivo, "w") as f:
        json.dump(produtos, f, indent=4)


def carregar_estoque(arquivo="estoque.json"):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def cadastrar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def remover_produto(produtos):
    nome = input("Digite o nome do produto que deseja remover: ")
    produto_encontrado = False
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            produto_encontrado = True
            print(f"Produto '{nome}' removido com sucesso!")
            break
    if not produto_encontrado:
        print(f"Produto '{nome}' não encontrado.")

def editar_produto(produtos):
    nome = input("Digite o nome do produto que deseja editar: ")
    produto_encontrado = False
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produto_encontrado = True
            novo_nome = input(f"Novo nome (atual: {produto['nome']}): ") or produto['nome']
            novo_preco = input(f"Novo preço (atual: R$ {produto['preco']}): R$ ") or produto['preco']
            nova_quantidade = input(f"Nova quantidade (atual: {produto['quantidade']}): ") or produto['quantidade']
            
            produto["nome"] = novo_nome
            produto["preco"] = float(novo_preco)
            produto["quantidade"] = int(nova_quantidade)
            print(f"Produto '{novo_nome}' editado com sucesso!")
            break
    if not produto_encontrado:
        print(f"Produto '{nome}' não encontrado.")


def visualizar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    headers = ["Nome", "Preço (R$)", "Quantidade"]
    table = [[produto["nome"], f"R$ {produto['preco']:.2f}", produto["quantidade"]] for produto in produtos]
    
    print(tabulate(table, headers=headers, tablefmt="pretty"))


def menu():
    produtos = carregar_estoque()
    
    while True:
        print("\n--- Gerenciador de Estoque ---")
        print("1. Cadastrar produto")
        print("2. Remover produto")
        print("3. Editar produto")
        print("4. Visualizar produtos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            remover_produto(produtos)
        elif opcao == "3":
            editar_produto(produtos)
        elif opcao == "4":
            visualizar_produtos(produtos)
        elif opcao == "5":
            salvar_estoque(produtos)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
