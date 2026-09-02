try:
    num = int(input("Digite um numero que deseja ver a tabuada: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except:
    print("Digite apenas numeros inteiros")