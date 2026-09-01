numeros = []

for i in range(6):
    num = int(input(f"Digite o número {i + 1} para incluir no cálculo: "))
    numeros.append(num)

soma = sum(numeros)
minimo = min(numeros)
maximo = max(numeros)

numeros.sort()

print(f"A soma dos números é: {soma}")
print(f"O menor número é: {minimo}")
print(f"O maior número é: {maximo}")
print(f"Em ordem crescente: {numeros}")