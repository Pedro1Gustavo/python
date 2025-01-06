produtos = [("Arroz", 20.50), ("Feijão", 10.30), ("Óleo", 8.0)]

def exibir_produtos():
    total = 0
    for produto, preco in produtos:
        print(f"Produto: {produto} | Preço: R$ {preco}")
        total += preco
    print(f"Total gasto: R$ {total}")

def alterar_preco(nome_produto, novo_preco):
    global produtos
    for i, (produto, preco) in enumerate(produtos):
        if produto.lower() == nome_produto.lower():  
            produtos[i] = (produto, novo_preco)
            print(f"O preço de {produto} foi alterado para R$ {novo_preco}")
            return
    print(f"Produto {nome_produto} não encontrado.")


exibir_produtos()

produto_escolhido = input("Digite o nome do produto que deseja alterar o preço: ")
novo_preco = float(input("Digite o novo preço: "))

alterar_preco(produto_escolhido, novo_preco)

exibir_produtos()
