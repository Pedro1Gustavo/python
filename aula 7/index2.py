import manipulacao_strings

def main():
    print("Bem-vindo ao Manipulador de Strings!")
    texto = input("Digite uma string: ")

    invertida = manipulacao_strings.inverter_string(texto)
    print(f"String invertida: {invertida}")

    num_palavras = manipulacao_strings.contar_palavras(texto)
    print(f"Número de palavras: {num_palavras}")

    eh_palindromo = manipulacao_strings.verificar_palindromo(texto)
    if eh_palindromo:
        print("A string é um palíndromo!")
    else:
        print("A string não é um palíndromo.")

if __name__ == "__main__":
    main()
