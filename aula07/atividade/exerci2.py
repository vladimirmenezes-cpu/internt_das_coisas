compras = []

for i in range(5):
    compra = input(f"Digite o {i + 1}° produto:")
    compras.append(compra)
print(f"\nLista de produtos cadastrados {compras}\nA quantidade de produtos cadastrados foi:{len(compras)} ")