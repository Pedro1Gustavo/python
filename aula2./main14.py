numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [int(n) for n in numeros.split()]

numeros_sem_duplicatas = list(set(numeros))

print(f"Lista original: {numeros}")
print(f"Lista sem duplicatas: {numeros_sem_duplicatas}")
