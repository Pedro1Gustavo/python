class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro late: Au Au!"

class Gato(Animal):
    def emitir_som(self):
        return "O gato mia: Miau!"

class Passaro(Animal):
    def emitir_som(self):
        return "O pássaro canta: Piu Piu!"

animais = [Cachorro(), Gato(), Passaro()]

def fazer_barulho(animais):
    for animal in animais:
        print(animal.emitir_som())

fazer_barulho(animais)