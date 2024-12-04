import conversoes

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n=== Conversor de Unidades ===")
    print("1. Metros para Pés")
    print("2. Quilogramas para Libras")
    print("3. Celsius para Fahrenheit")
    print("4. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            try:
                metros = float(input("Digite o valor em metros: "))
                resultado = conversoes.metros_para_pes(metros)
                print(f"{metros} metros é igual a {resultado:.2f} pés.")
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif escolha == "2":
            try:
                quilogramas = float(input("Digite o valor em quilogramas: "))
                resultado = conversoes.quilogramas_para_libras(quilogramas)
                print(f"{quilogramas} quilogramas é igual a {resultado:.2f} libras.")
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif escolha == "3":
            try:
                celsius = float(input("Digite o valor em graus Celsius: "))
                resultado = conversoes.celsius_para_fahrenheit(celsius)
                print(f"{celsius}°C é igual a {resultado:.2f}°F.")
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif escolha == "4":
            print("Encerrando o programa. Até logo!")
            break
        
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
