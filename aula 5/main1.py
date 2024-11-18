def calcular_media(notas):
    return sum(notas) / len(notas)

notas = []

for i in range(3):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = calcular_media(notas)

if media >= 6:
    classificacao = "Aprovado"
else:
    classificacao = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")