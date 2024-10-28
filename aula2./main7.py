lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

result = []
for n1, n2 in zip(lista1, lista2):
    result.append(n1 + n2)

print(result)