opcoes = {
    "1": "Marçal",
    "2": "Datena",
    "3": "Boulos"
}

resultados = {opcao: 0 for opcao in opcoes}

print("Sistema de Votação")
print("Escolha uma das opções abaixo para votar:")
for chave, candidato in opcoes.items():
    print(f"{chave} - {candidato}")
print("Digite 0 para encerrar a votação.")

while True:
    voto = input("\nDigite o número da sua opção de voto: ")
    
    if voto == "cabo":
        print("\nVotação encerrada!\n")
        break
    elif voto in resultados:
        resultados[voto] += 1
        print(f"Voto computado para {opcoes[voto]}.")
    else:
        print("Opção inválida! Tente novamente.")

print("Resultados finais da votação:")
for chave, total in resultados.items():
    print(f"{opcoes[chave]}: {total} votos")
