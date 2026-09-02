num = []

while True:
    try:
        for i in range(2):
            numeros = int(input("Digite um numero inteiro: "))
            num.append(numeros)

        total = sum(num)
        print(f"A soma dos numeros é: {total}")
        break

    except:
        print("Você digitou um valor inválido, tente novamente.")