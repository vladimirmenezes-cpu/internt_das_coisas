carrinho = []

while True:
    produto = float(input(f'Digite o valor do produto: '))
    if(produto ==0):
        break
    else:
        carrinho.append(produto)

total = sum(carrinho)
print(f"Valor total da compra foi: R${total:.2f}")