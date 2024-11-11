def soma(m, k):
    return m + k 

def subtracao(m, k):
    return m - k 

def multiplicacao(m, k):
    return m * k 

def divisao(m, k):
    if m == 0:
        return "Erro fatal! Divisão por subzero."
    return m / k

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar agente")
        print("2. Subtrair o imposto")
        print("3. Multiplicar o dinheiro")
        print("4. Divisão dos bens")
        print("5. Sair fora")
        
        escolha = input("Digite a opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora. Até logo!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida, tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos.")
            continue
        
        if escolha == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")

calculadora()