produtos = {
    "produto1": {"nome": "Notebook", "preco": 3500, "quantidade": 10},
    "produto2": {"nome": "Smartphone", "preco": 2000, "quantidade": 20},
    "produto3": {"nome": "Tablet", "preco": 1500, "quantidade": 15}
}

def adicionar_produto(dicionario, codigo, nome, preco, quantidade):
    if codigo in dicionario:
        print("Produto já existe.")
    else:
        dicionario[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
        print(f"Produto {nome} adicionado com sucesso.")

def remover_produto(dicionario, codigo):
    if codigo in dicionario:
        removed = dicionario.pop(codigo)
        print(f"Produto {removed['nome']} removido com sucesso.")
    else:
        print("Produto não encontrado.")

def atualizar_produto(dicionario, codigo, nome=None, preco=None, quantidade=None):
    if codigo in dicionario:
        if nome is not None:
            dicionario[codigo]["nome"] = nome
        if preco is not None:
            dicionario[codigo]["preco"] = preco
        if quantidade is not None:
            dicionario[codigo]["quantidade"] = quantidade
        print(f"Produto {codigo} atualizado com sucesso.")
    else:
        print("Produto não encontrado.")

print("Dicionário inicial de produtos:")
print(produtos)

adicionar_produto(produtos, "produto4", "Fone de Ouvido", 500, 50)

atualizar_produto(produtos, "produto1", preco=3200, quantidade=8)

remover_produto(produtos, "produto2")

print("\nDicionário após as operações:")
print(produtos)
