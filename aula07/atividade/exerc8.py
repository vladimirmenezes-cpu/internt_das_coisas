notas = []

while True:
    nota = float(input("Digite uma nota ou -1 para encerrar: "))

    if nota == -1:
        break

    notas.append(nota)

print("\nNotas cadastradas:")

for nota in notas:
    print(nota)

quantidade = len(notas)
media = sum(notas) / quantidade
maior = max(notas)
menor = min(notas)

notas.sort()
notas.reverse()

print(f"\nQuantidade de notas: {quantidade}\nMédia das notas: {media}\nMaior nota: {maior}\nMenor nota: {menor}\nNotas em ordem decrescente: {notas}")

