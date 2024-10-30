def verificar_chaves(dicionario, lista_chaves):
    for chave in lista_chaves:
        if chave not in dicionario:
            return False
    return True

dados = {
    "nome": "Adam",
    "idade": 70,
    "cidade": "Amazonas"
}

lista_chaves = ["nome", "idade", "cidade"]  

resultado = verificar_chaves(dados, lista_chaves)
print(f"Todas as chaves estão presentes no dicionário? {resultado}")
