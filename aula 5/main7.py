def criar_lista_de_compras(*args):
    lista_de_compras = list(args)
    return lista_de_compras

compras = criar_lista_de_compras("maçã", "banana", "arroz", "feijão", "leite")
print(f"Lista de compras: {compras}")  
