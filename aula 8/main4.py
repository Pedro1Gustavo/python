def eh_palindromo(s):
    
    return s == s[::-1]

def encontrar_palindromos(lista):
    palindromos = [string for string in lista if eh_palindromo(string)]
    return palindromos

lista_strings = ["radar", "python", "level", "world", "madam", "hello"]

palindromos_resultado = encontrar_palindromos(lista_strings)
print("Palíndromos encontrados:", palindromos_resultado)
