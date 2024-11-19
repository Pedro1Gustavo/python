def dobrar_numeros(lista):
    return list(map(lambda x: x * 2, lista))

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = dobrar_numeros(numeros)
print(numeros_dobrados)  
