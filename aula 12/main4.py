from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "O carro está acelerando."
    
    def frear(self):
        return "O carro está freando."

class Bicicleta(Veiculo):
    def acelerar(self):
        return "A bicicleta está ganhando velocidade."
    
    def frear(self):
        return "A bicicleta está reduzindo a velocidade."

def testar_veiculo(veiculo: Veiculo):
    print(veiculo.acelerar())
    print(veiculo.frear())

carro = Carro()
bicicleta = Bicicleta()

testar_veiculo(carro)
testar_veiculo(bicicleta)
