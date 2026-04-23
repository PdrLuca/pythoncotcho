import os
os.system("cls")

idades = []

while True:
    idade = int(input("Digite a idade: "))
    idades.append(idade)

    if idade == -1:
        break

print(f"Idades digitadas: {idades}")
print(f"Quantidade de idades: {len(idades)}")
print(f"A média das idades é: {sum(idades) / len(idades) if idades else 0:.2f}")
print(f"Quantidade de idades maiores que 18: {len([idade for idade in idades if idade > 18])}")
