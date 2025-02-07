class Calculadora:
    def somar(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Os parâmetros devem ser ambos inteiros ou ambos strings")

calc = Calculadora()

resultado1 = calc.somar(5, 10)
print("Soma de inteiros:", resultado1)  # Saída: 15

resultado2 = calc.somar("Ola, ", "MUndo")
print("Concatenaçãoo de strings:", resultado2)
