import index1funços

def menu():
    print("==== CALCULADORA ====")
    print("Escolha a operação que deseja realizar:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    escolha = input("Digite o número da operação: ")
    return escolha

def obter_valores():
    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            return a, b
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def calcular():
    while True:
        escolha = menu()

        if escolha == '1':
            a, b = obter_valores()
            resultado = index1funços.soma(a, b)
            print(f"O resultado da soma é: {resultado}")
        
        elif escolha == '2':
            a, b = obter_valores()
            resultado = index1funços.subtracao(a, b)
            print(f"O resultado da subtração é: {resultado}")
        
        elif escolha == '3':
            a, b = obter_valores()
            resultado = index1funços.multiplicacao(a, b)
            print(f"O resultado da multiplicação é: {resultado}")
        
        elif escolha == '4':
            a, b = obter_valores()
            resultado = index1funços.divisao(a, b)
            print(f"O resultado da divisão é: {resultado}")
        
        elif escolha == '5':
            print("Saindo... Até outro dia amigo(a)")
            break
        
        else:
            print("Opção inválida! Por favor, escolha direito fazendo favor.")

if __name__ == "__main__":
    calcular()
