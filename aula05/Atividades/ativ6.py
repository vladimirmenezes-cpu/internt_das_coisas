# 6) Filtragem e Média de Dados (Processamento de Vetores)
# Enunciado: Desenvolva um programa que peça ao usuário para digitar a nota de 8
# alunos e armazene-as em uma lista. O programa deve:
# 1. Calcular e mostrar a média aritmética da turma.
# 2. Criar e exibir uma nova lista contendo apenas as notas que ficaram acima
# da média calculada.

notas = []

for x in range(8):
    nota = float(input(f"Digite a nota dos alunos {x + 1}°: "))
    notas.append(nota)

media = sum(notas)/len(notas)

notas_acima = []
for nota in notas:
    if nota > media:
        notas_acima.append(nota)

print(f"\nA média aritmética da turma foi: {media:.2f}")
print(f"Notas acima da média: {notas_acima}")