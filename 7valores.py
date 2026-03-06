numeros = []

for x in range(7):
    n = int(input('Digite um número: '))
    numeros.append(n)
    
total = sum(numeros)
print(f'A soma dos números é: {total}')