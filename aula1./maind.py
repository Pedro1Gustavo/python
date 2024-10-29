
resultados = [
    ("Equipe j", [8, 7, 9, 10]),
    ("Equipe d", [6, 8, 7, 5]),
    ("Equipe a", [9, 8, 10, 9]),
    ("Equipe f", [7, 6, 8, 7])
]

medias = [(equipe[0], sum(equipe[1]) / len(equipe[1])) for equipe in resultados]

medias.sort(key=lambda x: x[1], reverse=True)

classificacao = medias

print("Classificação Final:")
for equipe, media in classificacao:
    print(f"Equipe: {equipe}, Média de Pontos: {media:.2f}")
