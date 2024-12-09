vendas = {
    "produto1": 50,  
    "produto2": 75,  
    "produto3": 75,  
    "produto4": 30,  
    "produto5": 90   
}


def produto_mais_vendido(dicionario):
    
    max_vendas = max(dicionario.values())
    
    produtos_mais_vendidos = [produto for produto, vendas in dicionario.items() if vendas == max_vendas]
    
    return produtos_mais_vendidos, max_vendas

produtos_resultado, vendas_max = produto_mais_vendido(vendas)
print(f"Produto(s) mais vendido(s): {produtos_resultado} com {vendas_max} unidades vendidas.")
