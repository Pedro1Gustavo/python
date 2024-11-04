# lista1 = [8, 2, 3, ]
# lista2 = [5, 6, 7, ]

#result = []
#for n1, n2 in zip(lista1, lista2):
#    result.append(n1 + n2)

#print(result)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]  


menor = float('inf')  
maior = float('-inf')  
soma = 0  

for num in numeros:
    if num < menor:
        menor = num  
    if num > maior:
        maior = num  
    soma += num  

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)
