import os
os.system("cls")

nota = []

while len(nota) < 5:
    try:
        n = float(input("Digite uma nota entre 0 e 10: "))

        if n >= 0 and n <= 10:
            nota.append(n)
        else:
            print("Nota inválida. Por favor, digite um número entre 0 e 10.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número entre 0 e 10.")

print(f"Média das notas:", sum(nota) / len(nota))
print(f"Notas acima da média:", [n for n in nota if n >= 7])
print(f"Todas as notas:", nota)