from functools import reduce

def encontrar_maior_string(lista):
    return reduce(lambda x, y: x if len(x) > len(y) else y, lista)

strings = ["tomate", "abacaxi", "banana", "uva", "melancia"]
maior_string = encontrar_maior_string(strings)
print(f"A maior string é: {maior_string}")  
