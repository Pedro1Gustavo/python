
quantidade_pares = 0
quantidade_impares = 0

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))  

    
    if num % 2 == 0:
        quantidade_pares += 1  
    else:
        quantidade_impares += 1  

print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
