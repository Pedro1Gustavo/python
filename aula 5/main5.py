def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filtrar_pares(numeros)
print(numeros_pares)  
