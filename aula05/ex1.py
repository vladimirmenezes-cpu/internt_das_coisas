# 1) Peça ao usuário para digitar 5 temperaturas (uma por uma) e guarde-as em uma lista.
# Use um laço para a entrada de dados.
# Após a leitura, exiba:
# A maior temperatura registrada (max).
# A menor temperatura registrada (min).
# A média das temperaturas.

temperatura = []

for x in range(5):
    temp = float(input(f"Digite a {x + 1} temperatura: "))
    temperatura.append(temp)

media = sum(temperatura)/len(temperatura)
menos = min(temperatura)
maior = max(temperatura)

print(f'A maior temperatura do dia foi {maior}°C \nA menor temperatura do dia foi {menos}°C \nA media de temperatura do dia foi {media}°C')