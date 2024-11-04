numeros = [1, 2, 3, ]  

menor = float('inf')  
maior = float('-inf')  

for num in numeros:
    if num < menor:
        menor = num  
    if num > maior:
        maior = num   

print("Menor valor:", menor)
print("Maior valor:", maior)