def adicionar_ou_atualizar(dicionario, chave, valor):
    dicionario[chave] = valor  
    return dicionario

dados = {
    "nome": "Adam",
    "idade": 70,
    "cidade": "Amazonas"
}

chave = input("Digite a chave a ser adicionada ou atualizada: ")
valor = input("Digite o valor para essa chave: ")

dados_atualizados = adicionar_ou_atualizar(dados, chave, valor)

print("\nDicionário atualizado:")
print(dados_atualizados)
