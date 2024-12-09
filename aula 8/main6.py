def contar_pares_e_impares(lista):
    
    pares = sum(1 for num in lista if num % 2 == 0)
    
    impares = len(lista) - pares
    
    return pares, impares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares, impares = contar_pares_e_impares(lista_numeros)
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
