vendas_trimestrais = [
    [1000, 1200, 1100],  
    [1300, 1400, 1500],  
    [1700, 1600, 1800],  
    [2000, 1900, 2100]   
]

media_vendas_trimestre = [sum(trimestre) / len(trimestre) for trimestre in vendas_trimestrais]

soma_vendas_trimestre = [sum(trimestre) for trimestre in vendas_trimestrais]
indice_max = soma_vendas_trimestre.index(max(soma_vendas_trimestre))
trimestre_max_vendas = indice_max + 1  

indice_min = soma_vendas_trimestre.index(min(soma_vendas_trimestre))
trimestre_min_vendas = indice_min + 1  

total_vendas_ano = sum(soma_vendas_trimestre)


print("Média de vendas por trimestre:", media_vendas_trimestre)
print("Trimestre com a maior soma de vendas: Trimestre", trimestre_max_vendas)
print("Trimestre com a menor soma de vendas: Trimestre", trimestre_min_vendas)
print("Total de vendas no ano inteiro:", total_vendas_ano)
