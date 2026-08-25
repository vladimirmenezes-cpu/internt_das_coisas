# 2) Crie um programa em Python que lê uma lista de 10 nomes e sorteia um
# nome entre eles.
import random, os
nome = []

for x in range(10):
    nomes = input(f"{x+1}° Digite os nomes dos participantes:")
    nome.append(nomes)
    os.system('cls')

vencendor = random.choice(nome)

print(f"O vencendor foi: {vencendor}")