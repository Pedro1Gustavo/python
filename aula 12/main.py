import math

class Forma:
    def area(self):
        pass
    
    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

circulo = Circulo(1000)
print(f"Círculo - Área: {circulo.area()} | Perímetro: {circulo.perimetro()}")

retangulo = Retangulo(10, 6)
print(f"Retângulo - Área: {retangulo.area()} | Perímetro: {retangulo.perimetro()}")
