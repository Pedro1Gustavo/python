notas_alunos = {
    "Alam": 8.5,
    "Douglas": 7.0,
    "Carla": 9.0,
    "Daniel": 6.5,
    "Eva": 8.0
}

soma_notas = sum(notas_alunos.values())
media = soma_notas / len(notas_alunos)

print(f"A média das notas: {media:.2f}")
