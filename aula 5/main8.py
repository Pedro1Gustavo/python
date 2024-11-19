def calcular(numero1, numero2, operacao):
    operacoes = {
        "adição": lambda x, y: x + y,
        "subtração": lambda x, y: x - y,
        "multiplicação": lambda x, y: x * y,
        "divisão": lambda x, y: x / y if y != 0 else "Erro: divisão por zero"
    }

    if operacao in operacoes:
        return operacoes[operacao](numero1, numero2)
    else:
        return "Operação inválida"

resultado = calcular(10, 5, "multiplicação")
print(f"Resultado: {resultado}")  

resultado = calcular(10, 0, "divisão")
print(f"Resultado: {resultado}")  

resultado = calcular(10, 5, "exponenciação")
print(f"Resultado: {resultado}")  
