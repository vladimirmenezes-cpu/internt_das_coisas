# 1) Crie um programa que lê uma lista de 10 números e conta a quantidade de
# números positivos e a quantidade de números negativos, e mostra o vetor
# com os negativos e o a soma dos positivos?

numeros_positivos = []
numeros_negativos = []

for x in range(10):
    numero = int(input(f"Digite o {x + 1}º número: "))

    if numero > 0:
        numeros_positivos.append(numero)
    elif numero < 0:
        numeros_negativos.append(numero)

print(f"A quantidade de numeros positivos são: {len(numeros_positivos)}\nA quantidade de numeros negativos são: {len(numeros_negativos)}\nTodos os numeros negativos são: {numeros_negativos}\nA soma de numeros positivos são: {sum(numeros_positivos)}") 





