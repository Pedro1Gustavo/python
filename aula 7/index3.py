import math

def quadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

def retangulo(largura, altura):
    area = largura * altura
    perimetro = 2 * (largura + altura)
    return area, perimetro

def circulo(raio):
    area = math.pi * raio ** 2
    perimetro = 2 * math.pi * raio
    return area, perimetro

def calcular():
    print("Bem-vindo ao programa de cálculo de áreas e de perímetros!")
    print("Escolha uma forma geométrica:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Círculo")
    
    escolha = input("Digite o número da forma escolhida (1, 2 ou 3): ")

    if escolha == "1":
        lado = float(input("Digite o tamanho do lado do quadrado: "))
        area, perimetro = quadrado(lado)
        print(f"A área do quadrado é: {area:.2f} unidades quadradas.")
        print(f"O perímetro do quadrado é: {perimetro:.2f} unidades.")
        
    elif escolha == "2":
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area, perimetro = retangulo(largura, altura)
        print(f"A área do retângulo é: {area:.2f} unidades quadradas.")
        print(f"O perímetro do retângulo é: {perimetro:.2f} unidades.")
        
    elif escolha == "3":
        raio = float(input("Digite o raio do círculo: "))
        area, perimetro = circulo(raio)
        print(f"A área do círculo é: {area:.2f} unidades quadradas.")
        print(f"A circunferência do círculo é: {perimetro:.2f} unidades.")
        
    else:
        print("Opção inválida. Tente novamente.")

calcular()
