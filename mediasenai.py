nota = []

for x in range(3):
    n = float(input('Digite a nota: '))
    nota.append(n)
    media = sum(nota) / 3
    
print(f'A média das notas é: {media:.1f}')