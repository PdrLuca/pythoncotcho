import os
os.system("cls")

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Maior número e sua posição: " + str(max(numeros)) + " na posição " + str(numeros.index(max(numeros))))
print("Menor número e sua posição: " + str(min(numeros)) + " na posição " + str(numeros.index(min(numeros))))