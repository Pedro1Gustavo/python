vendas = {
    'produto_a': [10, 20, 30],
    'produto_b': [5, 15, 25],
    'produto_c': [30, 10, 10],
}

somas_vendas = {produto: sum(vendas[produto]) for produto in vendas}

max_vendas = max(somas_vendas.values())

produtos_mais_vendidos = [produto for produto, soma in somas_vendas.items() if soma == max_vendas]

print("Produto(s) mais vendido(s):", produtos_mais_vendidos)
print("Total de vendas:", max_vendas)
