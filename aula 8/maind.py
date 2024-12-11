import pandas as pd

dados = {
    'Ano': [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
    'Fazenda': ['Fazenda A', 'Fazenda B', 'Fazenda C', 'Fazenda A', 'Fazenda B', 'Fazenda C', 'Fazenda A', 'Fazenda B', 'Fazenda C'],
    'Cultura': ['Milho', 'Soja', 'Trigo', 'Milho', 'Soja', 'Trigo', 'Milho', 'Soja', 'Trigo'],
    'Produção': [500, 300, 400, 600, 200, 350, 450, 250, 500]
}

df = pd.DataFrame(dados)

producao_por_ano = df.groupby('Ano')['Produção'].sum()
ano_max_producao = producao_por_ano.idxmax()
ano_min_producao = producao_por_ano.idxmin()

producao_por_cultura = df.groupby('Cultura')['Produção'].sum()
cultura_max_producao = producao_por_cultura.idxmax()
cultura_min_producao = producao_por_cultura.idxmin()

ano_especifico = 2021
producao_no_ano = df[df['Ano'] == ano_especifico]
fazenda_max_producao = producao_no_ano.loc[producao_no_ano['Produção'].idxmax(), 'Fazenda']
fazenda_min_producao = producao_no_ano.loc[producao_no_ano['Produção'].idxmin(), 'Fazenda']

print(f"Ano com maior produção total: {ano_max_producao}")
print(f"Ano com menor produção total: {ano_min_producao}")
print(f"Cultura com maior produção total: {cultura_max_producao}")
print(f"Cultura com menor produção total: {cultura_min_producao}")
print(f"No ano {ano_especifico}, a fazenda com maior produção foi: {fazenda_max_producao}")
print(f"No ano {ano_especifico}, a fazenda com menor produção foi: {fazenda_min_producao}")
