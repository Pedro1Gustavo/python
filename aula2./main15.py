def unir_conjuntos(*conjuntos):
    conjunto_resultante = set()
    for conjunto in conjuntos:
        conjunto_resultante = conjunto_resultante.union(conjunto)
    return conjunto_resultante

conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
conjunto3 = {7, 8, 9}

conjunto_unido = unir_conjuntos(conjunto1, conjunto2, conjunto3)

print("União dos conjutos:", conjunto_unido)
