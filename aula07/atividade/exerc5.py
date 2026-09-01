convidados = []

while True:
    nome = input("Digite o nome do convidade (ou 'fim' para encerrar):")

    if nome.lower() == 'fim':
        break

    convidados.append(nome)

convidados.sort()

print(f"\nLista de convidados: {convidados}\nQuantidade de convidados: {len(convidados)}")