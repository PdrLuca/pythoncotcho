import os
os.system("cls")

numeros = []

for i in range(6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Números pares: " + str([num for num in numeros if num % 2 == 0]))
print("Números ímpares: " + str([num for num in numeros if num % 2 != 0]))
print("Números digitados: " + str(numeros))