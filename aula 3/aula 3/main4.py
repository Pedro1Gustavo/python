idades = []

n = int(input("Quantas pessoas você gostaria de registrar as idades? "))


for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    idades.append(idade)  

soma_idades = sum(idades)
media_idades = soma_idades / len(idades) if idades else 0  

print(f"A média das idades: {media_idades:.2f}")

if media_idades <= 25:
    print("A turma é jovem.")
elif media_idades <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")
