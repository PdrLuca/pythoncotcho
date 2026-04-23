import os
os.system("cls")

numeros = []
while True:

    for i in range(8):
        numero = int(input("Digite um número positivo ou negativo: "))
        numeros.append(numero)
        break
    


    for i in range(8):
        numeros = int(input("Digite um número positivo: "))
        numeros.append(numeros)
print("Números positivos: " + str([num for num in numeros if num > 0]))
print("Números negativos: " + str([num for num in numeros if num < 0]))
print("Números digitados: " + str(numeros))