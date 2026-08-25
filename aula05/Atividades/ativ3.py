#3) Escreva um programa que leia uma lista de 5 nomes e depois exiba esses
#nomes em ordem alfabética.

nome = []

for x in range(5):
    nomes = input(f"{x+1}° Digite os nomes dos participantes:")
    nome.append(nomes)


nome.sort
print(f"Nomes em ordem alfabetica: {nome}")

