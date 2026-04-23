import os
os.system("cls")

numeros = []

for i in range(7):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("n\Lista de números: " + str(numeros))

busca = int(input("Digite um número para buscar: "))
if busca in numeros:
    print("Número encontrado na posição: " + str(numeros.index(busca)))
else:
    print("Número não encontrado na lista.")

