Prova 1

for numero in range(1,30):
  if numero % 3 == 0:
    print(numero) 

Prova 2 

numero = int(input("Digite um número para ver a tabuada: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1 
